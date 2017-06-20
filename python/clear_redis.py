#!venv/bin/python
import sys
import time
import logging
import argparse
from datetime import datetime
from rediscluster import StrictRedisCluster


nodes = [{"host": "10379.redis.lecloud.com", "port": "6002"}]
rc = StrictRedisCluster(startup_nodes=nodes, decode_responses=True,password='9C2HRT2PJI')
#nodes1 = [{"host": "10.183.101.81", "port": "6003"}]
#nodes2 = [{"host": "10316m.redis.lecloud.com", "port": "6006"}]
#rc1 = StrictRedisCluster(startup_nodes=nodes1, decode_responses=True,password='T2QP0GEVLD')
#rc2 = StrictRedisCluster(startup_nodes=nodes2, decode_responses=True,password='ORXYLDENPO')
LOG='/home/guozequn/shell/kit/redis.log'

def move(results):
    print(results)
    print(type(results))
def delete(rc,prefix):
    num=0
    for key in rc.scan_iter(match=''.join([prefix,'*']), count=500):
        rc.delete(key)
        num+=1
        if num%500 == 0:
            print(num)
    print(num)
def migrate():
    return "migrate"
def caculate(rc,prefix):
    num=0
    for key in rc.scan_iter(match=''.join([prefix,'*']), count=500):
        num+=1
    print(num)

def log_init():
    logging.basicConfig(filename=LOG,
                        level=logging.DEBUG,
                        format="%(asctime)s  %(levelname)s  %(message)s")

def mv_hashkey(from_rc, to_rc, prefix):
    n=0
    starttime=time.time()
    try:
        for key in from_rc.scan_iter(match=''.join([prefix,'*']), count=500):
            starttime=time.time()
            #print(key)
            hk = from_rc.hkeys(key)
            hv = from_rc.hmget(key,hk)
            tmp = dict(zip(hk,hv))
            to_rc.hmset(key,tmp)
            n+=1
            if n%500 == 0:
                logging.info(' '.join(['Migrate', prefix, str(n)]))
    except ValueError as e:
        logging.error("User KeyboardInterrupt")
    except Exception as e:
        logging.error(e)

def test():
    prefix='cn_deal_merchant_xxxxxx'
    while True:
        nowtime=time.time()
        key = prefix + 'haha'
        rc.set(key,'kkk', ex=2)
        endtime=time.time()
        logtime=str(round(endtime-nowtime,6))
        with open(LOG,'a') as f:
            f.write(str(datetime.now())+ '\t'+ logtime+'\n')
        time.sleep(1)

def argparse_mixed():
    """
    根据参数不同返回不同参数
    """
    descp='With migration or delete function\'s tool for redis.'
    parser = argparse.ArgumentParser(description=descp, conflict_handler='resolve')
    subparsers = parser.add_subparsers()

    parser_a = subparsers.add_parser('move', help='migrate keys from A to B , no keys left in a.')
    # parser_a.set_defaults(option="move") add option="move" to the results
    parser_a.set_defaults(option="move")
    parser_a.add_argument("-s", dest="src_redis", help="redis src")
    parser_a.add_argument("-d", dest="dst_redis", help="redis src")
    parser_a.add_argument("-p", dest="keyprefix", help="prefix of keys")
    parser_a.add_argument("--dps", dest="dst_pass", help="redis dest password")
    parser_a.add_argument("--sps", dest="src_pass", help="redis source password")

    parser_b = subparsers.add_parser('delete', help='delete keys with xxx prefix.')
    # parser_b.set_defaults(option="delete") add option="delete" to the results
    parser_b.set_defaults(option="delete")
    parser_b.add_argument("-s", dest="src_redis", help="redis src")
    parser_b.add_argument("-p", dest="prefix", help="prefix of keys")
    parser_b.add_argument("--pwd", dest="password", help="redis password")

    parser_c = subparsers.add_parser('migrate', help='migrate keys from A to B, leave a copy in a.')
    # parser_c.set_defaults(option="migrate") add option="migrate" to the results
    parser_c.set_defaults(option="migrate")
    parser_c.add_argument("-s", dest="src_redis", help="redis src")
    parser_c.add_argument("-d", dest="dst_redis", help="redis src")
    parser_c.add_argument("-p", dest="prefix", help="prefix of keys")
    parser_c.add_argument("--dps", dest="dst_pass", help="redis dest password")
    parser_c.add_argument("--sps", dest="src_pass", help="redis source password")

    args = parser.parse_args()
    # args return like Namespace(prefix=None, src_redis='',option='move')
    # for example: test = argparse_mixed() , use test.prefix to get value.

    # return a dict result
    return vars(args)

def judge_args(argv):
    """
    检查获取参数
    """
    if 'option' not in argv:
        print("Use %s -h to get help." % sys.argv[0])
        exit(1)

    func = {"move": move,
            "delete": delete,
            "migrate": migrate}

    current_func = func[argv['option']]
    current_func(argv)





if __name__ == '__main__':
    argv = argparse_mixed()
    judge_args(argv)
