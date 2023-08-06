#!/bin/env python3
# coding:utf-8
"""
    修正Zabbix 中 Discovered hosts 组中以下划线和数字结尾的 Hostname
"""

import sys
import re
from zabbix_api import ZabbixAPI

def main(args, subcmd_args):

    pattern = re.compile(r'_\d+$')
    
    zapi = ZabbixAPI(args.zbx_server, timeout=60)
    zapi.validate_certs = False
    zapi.login(args.zbx_user, args.zbx_passwd)

    #获取 Discovered hosts 组的group id
    group = zapi.hostgroup.get({
        'output': ['groupid'], 
        'filter': {'name': 'Discovered hosts'}
    })

    if group:
        group_id = group[0]['groupid']
    else:
        sys.exit(-1)

    # 获取属于 Discovered hosts 组的 Host
    hosts = zapi.host.get({
        'output': ['hostid', 'host'],
        'groupids': [group_id]
    })

    for host in hosts:

        # 过滤出Host name是_x 结尾, 并修改 Host name
        if pattern.search(host['host']):

            new_host_name = pattern.sub('', host['host'])
            zapi.host.update({
                'hostid': host['hostid'],
                'host': new_host_name
            })
            print(f'update host name success: hostid={host["hostid"]}, hostname {host["host"]} => {new_host_name}')

    zapi.logout()
