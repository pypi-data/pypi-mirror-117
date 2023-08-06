#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
import time
import re
from datetime import datetime
from functools import reduce
from collections.abc import Iterable
from zabbix_api import ZabbixAPI
from elasticsearch import Elasticsearch


class ItemFilterAndAccumulator(object):

    def __init__(self, keywords):
        if not isinstance(keywords, Iterable):
            raise ValueError('keyworks must be iterabled')
        self.keywords = keywords

    def is_keywords(self, item):
        for word in self.keywords:
            if word not in item['key_']:
                return False
        return True

    @staticmethod
    def accumulator(a, b):
        return a+b

    def get_result(self, items):
        filtered_items = filter(self.is_keywords, items)
        result = reduce(self.accumulator, [
                        item['lastvalue'] for item in filtered_items], 0)
        return result if result > 0 else None


def format_items(hi):
    if hi['flags'] != "4":
        for item in hi['items']:
            item['lastvalue'] = float(
                item['lastvalue']) if (item['value_type'] == '0' or item['value_type'] == '3') else item['lastvalue']
        hi['filesystems_total'] = ItemFilterAndAccumulator(
            ['vfs.fs.size', 'total']).get_result(hi['items'])
        hi['filesystems_used'] = ItemFilterAndAccumulator(
            ['vfs.fs.size', 'used']).get_result(hi['items'])
        hi['memory_total'] = ItemFilterAndAccumulator(
            ['vm.memory.size', 'total']).get_result(hi['items'])
        hi['memory_used'] = ItemFilterAndAccumulator(
            ['vm.memory.size', 'used']).get_result(hi['items'])
    hi.pop('items')


def get_hosts(zapi, es):
    hostids = zapi.host.get({
        "output":  ["hostid"]
    })
    dt = time.strftime('%Y.%m.%d', time.localtime())
    for item in hostids:
        his = zapi.host.get({
            'hostids': item['hostid'],
            'output': 'extend',
            'selectGroups': 'extend',
            'selectInterfaces': 'extend',
            'selectInventory': 'extend',
            'selectItems': ['name', 'lastvalue', 'value_type', 'key_'],
        })
        for hi in his:
            hi['@timestamp'] = datetime.utcfromtimestamp(time.time())
            format_items(hi)

            hi['group_names'] = [group['name'] for group in hi['groups']]

            linux_match = re.compile(
                r'^ *inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*$', re.M)
            win_match = re.compile(
                r'^Ethernet *enabled *(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*$', re.M)
            ipv4_addresses = linux_match.findall(
                hi['inventory'].get('host_networks', ''), re.M)
            if not ipv4_addresses:
                ipv4_addresses = win_match.findall(
                    hi['inventory'].get('host_networks', ''), re.M)

            if "127.0.0.1" in ipv4_addresses:
                ipv4_addresses.remove("127.0.0.1")
            hi['ipv4_addresses'] = ipv4_addresses

            es.index(index='zabbix-raw-host-info-' +
                     dt, id=item['hostid'], body=hi)

            body_data = {
                '主机名称':  hi['inventory'].get('name', hi['host']),
                '主机别名': hi['inventory'].get('alias', hi['host']),
                '接口地址': [aif['ip'] for aif in hi['interfaces']],
                '主机组': [grp['name'] for grp in hi['groups']],
                'OS': hi['inventory'].get('os', None),
                'OS_FULL': hi['inventory'].get('os_full', None),
                'OS_SHORT': hi['inventory'].get('os_short', None),
                '资产标签': hi['inventory'].get('asset_tag', None),
                '主负责人': hi['inventory'].get('poc_1_name', None),
                '次负责人': hi['inventory'].get('poc_2_name', None),
                '机架': hi['inventory'].get('chassis', None),
                '子网掩码': hi['inventory'].get('host_netmask', None),
                '主机网络': hi['inventory'].get('host_networks', None),
                '机房': hi['inventory'].get('location', None),
                '机柜': hi['inventory'].get('site_rack', None),
                '序列号一': hi['inventory'].get('serialno_a', None),
                '序列号二': hi['inventory'].get('serialno_b', None),
                'MAC_A': hi['inventory'].get('macaddress_a', None),
                'MAC_B': hi['inventory'].get('macaddress_b', None),
                '硬件架构': hi['inventory'].get('hw_arch', None),
                '标签':  hi['inventory'].get('tag', None),
                '类型': hi['inventory'].get('type', None),
                '具体类型': hi['inventory'].get('type_full', None),
                '型号': hi['inventory'].get('model', None),
                '供应商': hi['inventory'].get('vendor', None),
                '@timestamp': datetime.utcfromtimestamp(time.time())
            }
            es.index(index='zabbix-host-info-' + dt,
                     id=item['hostid'], body=body_data)


def main(args, subcmd_args):
    parser = argparse.ArgumentParser("Handle aggregation item")
    parser.add_argument('--es_url', required=True, help="ElasticSearch server ip")
    parser.add_argument('--es_user', default='', help="ElasticSearch server login user")
    parser.add_argument('--es_passwd', default='', help="ElasticSearch server login password")

    local_args = parser.parse_args(subcmd_args)

    zapi = ZabbixAPI(args.zbx_server, timeout=60)
    zapi.validate_certs = False
    zapi.login(user=args.zbx_user, password=args.zbx_passwd)

    es = Elasticsearch(local_args.es_url, http_auth=(local_args.es_user, local_args.es_passwd))
    get_hosts(zapi, es)
