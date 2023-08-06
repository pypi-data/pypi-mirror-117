#!/bin/env python3
# coding:utf-8
"""
通过subcommand合并hostgrp-poc， discoverd-hosts-name-back， zabbix-vmware-host-inventory三个项目

subcommand:

    vmware-host-inventory: 更新 Zabbix 中 Hypervisors 组中 inventory 信息。

    host-group-poc: 读取ldap人员信息, 更新 Zabbix 中各组主机的 inventory

    host-name-back：消除 Zabbix 中 Discovered Hosts 组中hostname 末尾的下划线+数字

"""
import os
import sys
import argparse

def main():
    """
    设定子命令所需共同参数, 并将参数传给被调用的模块。
    如被调用模块有独有参数, 则通过 subcmd_args 变量传入其中。
    """
    # 子命令共同参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--zbx-server', required=True, help='URL of zabbix server')
    parser.add_argument('-u', '--zbx-user', required=True, help='Zabbix server login username')
    parser.add_argument('-p', '--zbx-passwd', required=True, help='Zabbix server login password')
    subparsers = parser.add_subparsers()

    # 添加 vmware-host-inventory 子命令
    subparser = subparsers.add_parser('vmware-host-inventory', help="update vmware hosts' inventory")
    subparser.set_defaults(module_name='update_vmware_host_inventory')

    # 添加 host-group-poc 子命令
    subparser = subparsers.add_parser('host-group-poc', help="get informations from ldap and update hosts' inventory poc")
    subparser.set_defaults(module_name='update_hostgrp_poc')

    # 添加 host-name-back 子命令
    subparser = subparsers.add_parser('host-name-back', help="update Discovered Hosts' hostname which names are end with _x")
    subparser.set_defaults(module_name='update_host_name')

    # 添加 service 子命令
    subparser = subparsers.add_parser('service', help="create or delete service tree")
    subparser.set_defaults(module_name='it_service_tool')

    # 添加 es-zabbix 子命令
    subparser = subparsers.add_parser('es-zabbix', help="Import ZABBIX's inventory into ES")
    subparser.set_defaults(module_name='es_index_zbxhost')

    args, subcmd_args = parser.parse_known_args()

    if not hasattr(args, 'module_name'):
        # 未指定子命令时, 输出 help 信息
        args = parser.parse_args(['-h'])


    # 调用对应的模块
    module_dir = os.path.abspath(__file__).rsplit('/', maxsplit=2)[0]
    module = __import__('.'.join(['lib', args.module_name]), fromlist=(module_dir))
    module.main(args, subcmd_args)

if __name__ == '__main__':
    main()
