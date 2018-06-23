#!venv/bin/python
import sys
import time, json
import random
import logging
import argparse
from datetime import datetime
from rediscluster import StrictRedisCluster, connection
from multiprocessing import Queue, Process, Pool


LOG='/home/guozequn/shell/kit/redis.log'

def log_init():
    logging.basicConfig(filename=LOG,
                        level=logging.DEBUG,
                        format="%(asctime)s  %(levelname)s  %(message)s")

def get_rc(addr, pwd, port):
    nodes = [{"host":addr, "port":port}]
    rc = StrictRedisCluster(startup_nodes=nodes,
                            decode_responses=True,
                            password=pwd)
    logging.info("%s:%s is connected." % (addr, port))
    return rc

def get_keys(argv, queue):
    rc = get_rc(argv['src_redis'],argv['src_pass'],argv['src_port'])
    pattens = ''.join([argv['prefix'],'*'])
    for keys in rc.scan_iter(match=pattens, count=500):
        queue.put(keys)
        if queue.qsize() > 10000:
            print(queue.qsize())
            time.sleep(random.random())

def move(argv, key):
    pass

def delete(argv, queue):
    rc = get_rc(argv['src_redis'],argv['src_pass'],argv['src_port'])
    i = 0
    while True:
        key = queue.get(True)
        i += 1
        if i % 500 == 0:
            print(i)
        rc.delete(key)
        logging.info("Delete %d keys" % i )

def migrate(rc, key):
    pass

def mv_hashkey(argv, queue):
    src = get_rc(argv['src_redis'],argv['src_pass'],argv['src_port'])
    dst = get_rc(argv['dst_redis'],argv['dst_pass'],argv['dst_port'])
    i = 0
    while True:
        #print(key)
        key = queue.get(True)
        hk = from_rc.hkeys(key)
        hv = from_rc.hmget(key,hk)
        tmp = dict(zip(hk,hv))
        to_rc.hmset(key,tmp)
        n+=1
        if n%500 == 0:
            logging.info(' '.join(['Migrate', prefix, str(n)]))

def argparse_mixed():
    """
    根据参数不同返回不同参数
    """
    descp='With migration or delete function\'s tool for redis.'
    parser = argparse.ArgumentParser(description=descp, conflict_handler='resolve')
    subparsers = parser.add_subparsers()

    # add father parent parser template 
    src_parser = argparse.ArgumentParser(add_help=False)
    dst_parser = argparse.ArgumentParser(add_help=False)
    pre_parser = argparse.ArgumentParser(add_help=False)

    src_parser.add_argument("-s", dest="src_redis", required=True, help="redis src addr")
    src_parser.add_argument("--spass", dest="src_pass", required=True, help="redis src password")
    src_parser.add_argument("--sport", dest="src_port", required=True, help="redis src port")
    dst_parser.add_argument("-d", dest="dst_redis", required=True, help="redis dst addr")
    dst_parser.add_argument("--dpass", dest="dst_pass", required=True, help="redis dst password")
    dst_parser.add_argument("--dport", dest="dst_port", required=True, help="redis dst port")
    pre_parser.add_argument("--prefix", dest="prefix", required=True, help="prefix of keys")

    # add option="move" to the results
    parser_move = subparsers.add_parser("move", parents=[src_parser, dst_parser, pre_parser],
                                        help = 'migrate keys from A to B , no keys left in a.')
    parser_move.set_defaults(option="move")
    # add option="delete" to the results
    parser_delete = subparsers.add_parser("delete", parents=[src_parser, pre_parser],
                                          help = 'delete keys by scan prefix')
    parser_delete.set_defaults(option="delete")
    # add option="migrate" to the results
    parser_migrate = subparsers.add_parser("migrate", parents=[src_parser, dst_parser, pre_parser],
                                           help = 'migrate keys from A to B , no keys left in a.')
    parser_migrate.set_defaults(option="migrate")

    # args return like Namespace(prefix=None, src_redis='',option='move')
    # for example: test = argparse_mixed() , use test.prefix to get value.
    args = parser.parse_args()

    # return a dict result
    return vars(args)

def run(argv, queue):
    """
    检查获取参数
    """
    global lock, counter
    argv = argparse_mixed()
    func = {"move": move,
            "delete": delete,
            "migrate": migrate}
    current_func = func[argv['option']]
    current_func(argv, queue)
        

if __name__ == '__main__':
    argv = argparse_mixed()
    if 'option' not in argv:
        print("Use %s -h to get help." % sys.argv[0])
        exit(1)
    log_init()
    q = Queue()
    p = Pool(5)
    pget = Process(target=get_keys, args=(argv, q))
    pdel = Process(target=run, args=(argv, q))
    pget.start()
    pdel.start()
    pget.join()
    pdel.terminate()
