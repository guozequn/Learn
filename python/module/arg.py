#-*- coding:utf-8 -*-
import sys
import argparse


def argparse_basic():
    """
    普通添加参数
    """
    descp='With migration or delete function\'s tool for redis.'
    parser = argparse.ArgumentParser(description=descp)
    parser.add_argument("-s", dest="from_redis", help="source redis-cluster")
    parser.add_argument("-d", dest="dest_redis", help="destnation redis-cluster")
    args = parser.parse_args()
    return args

def argparse_group():
    """
    普通添加组
    """
    descp='With migration or delete function\'s tool for redis.'
    parser = argparse.ArgumentParser(description=descp)
    # normal argument group
    args_group = parser.add_argument_group()
    args_group.add_argument("--duro", help="multi process to handle")
    args_group.add_argument("--sing", help="single process to handle")
    # mutually exclusive group
    func_group = parser.add_mutually_exclusive_group()
    func_group.add_argument("--delete", action="store_true", help="migrate keys from A to B, leave a copy in a.")
    func_group.add_argument("--migrate", action="store_true", help="migrate keys from A to B , no keys left in a.")
    func_group.add_argument("--move", action="store_true", help="delete keys with specified prefix.")
    
    args = parser.parse_args()
    return args

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
    parser_a.add_argument("-p", dest="prefix", help="prefix of keys")

    parser_b = subparsers.add_parser('delete', help='delete keys with xxx prefix.')
    # parser_b.set_defaults(option="delete") add option="move" to the results
    parser_b.set_defaults(option="delete")
    parser_b.add_argument("-s", dest="src_redis", help="redis src")
    parser_b.add_argument("-p", dest="prefix", help="prefix of keys")

    parser_c = subparsers.add_parser('migrate', help='migrate keys from A to B, leave a copy in a.')
    # parser_b.set_defaults(option="migrate") add option="move" to the results
    parser_c.set_defaults(option="migrate")
    parser_c.add_argument("-s", dest="src_redis", help="redis src")
    parser_c.add_argument("-d", dest="dst_redis", help="redis src")
    parser_c.add_argument("-p", dest="prefix", help="prefix of keys")
   
    args = parser.parse_args()
    # args return like Namespace(prefix=None, src_redis='',option='move')
    # for example: test = argparsed_mixed() , use test.prefix to get value.
    return args

def argparse_huge():
    """
    如果涉及大量的重复性参数，需要用到parents
    """
    descp='With migration or delete function\'s tool for redis.'
    parser = argparse.ArgumentParser(description=descp, conflict_handler='resolve')
    subparsers = parser.add_subparsers()

    # add father parent parser template 
    src_parser = argparse.ArgumentParser(add_help=False)
    dst_parser = argparse.ArgumentParser(add_help=False)
    pre_parser = argparse.ArgumentParser(add_help=False)
    src_parser.add_argument("-s", dest="src_redis", help="redis src addr")
    src_parser.add_argument("--sps", dest="src_pass", help="redis src password")
    src_parser.add_argument("--sport", dest="src_port", help="redis src port")
    dst_parser.add_argument("-d", dest="dst_redis", help="redis dst addr")
    dst_parser.add_argument("--dps", dest="dst_pass", help="redis dst password")
    dst_parser.add_argument("--dport", dest="dst_port", help="redis dst port")
    pre_parser.add_argument("-p", dest="keyprefix", help="prefix of keys")

    parser_move = subparsers.add_parser("move", parents=[src_parser, dst_parser, pre_parser],
                                        help = 'migrate keys from A to B , no keys left in a.')
    parser_move.set_defaults(option="move")
    parser_delete = subparsers.add_parser("delete", parents=[src_parser, pre_parser],
                                        help = 'delete keys by matching prefix')
    parser_delete.set_defaults(option="delete")
    parser_migrate = subparsers.add_parser("migrate", parents=[src_parser, dst_parser, pre_parser],
                                        help = 'migrate keys from A to B , no keys left in a.')
    parser_migrate.set_defaults(option="migrate")

    args = parser.parse_args()
    # Notice: args is an object like NameSpace(xx=xx,yy=zz)
    # use vars() change it to dict
    return vars(args)


#test = argparse_mixed()
test = argparse_group()
print(test)
