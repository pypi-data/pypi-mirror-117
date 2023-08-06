#!/usr/bin/python3
"""
在zabbix上依据zabbix主机组生成it-service树
"""
import argparse
from zabbix_api import ZabbixAPI

class CreateItService:
    def __init__(self, zapi, service_name, group_name):
        self.zapi = zapi
        self.service_name = service_name
        self.group_name = group_name

    def create(self):
        # Get root service
        rootsrv = self.zapi.service.get({'filter': {'name': self.service_name}, 'parentids': None})
        if len(rootsrv):
            print(f'The root service {self.service_name} already exists, exit with nothing to do')
            return

        # Create root it service
        rootsrv = self.zapi.service.create({
                    'name': self.service_name,
                    'algorithm': 1,
                    'showsla': 1,
                    'goodsla': 99.99,
                    'sortorder': 0
                 })
        groups = self.zapi.hostgroup.get({
                    'filter': {'name': self.group_name},
                    'output': ['groupid']
                 })
        hosts = self.zapi.host.get({
                    'groupids': [group['groupid'] for group in groups],
                    'selectTriggers': 'extend'
                })
        for host in hosts:
            # Create host level it service
            hostsrv = self.zapi.service.create({
                        'name': '{0} {1}'.format(self.service_name, host['name']),
                        'algorithm': 1,
                        'showsla': 0,
                        'goodsla': 99.99,
                        'sortorder': 0,
                        'parentid': rootsrv['serviceids'][0]
                      })

            for trigger in host.get('triggers'):
                # Create trigger level it service
                self.zapi.service.create({
                    'name': trigger['description'],
                    'triggerid': trigger['triggerid'],
                    'algorithm': 1,
                    'showsla': 1,
                    'goodsla': 99.99,
                    'sortorder': 0,
                    'parentid': hostsrv['serviceids'][0]
                })


class DeleteItService:

    def __init__(self, zapi, service_name):
        # super().__init__(zapi)
        self.zapi = zapi
        self.service_name = service_name

    def hard_service_delete(self, service):
        """
        Delete it service and it's dependencies recursively
        """
        # First delete the dependencies of the service
        for dependency in service.get('dependencies', []):
            tmpsrvs = self.zapi.service.get({
                        'serviceids': dependency['serviceid'],
                        'selectDependencies': 'extend'
                      })
            for tmpsrv in tmpsrvs:
                self.hard_service_delete(tmpsrv)

        # The dependencies of the service had deleted, Now delete the servie
        self.zapi.service.delete([service['serviceid']])

    def delete(self):
        # Get the root it service with specifed service name
        rootsrvs = self.zapi.service.get({
                    'filter': {'name': self.service_name},
                    'parentids': None,
                    'selectDependencies': 'extend'
                   })
        for rootsrv in rootsrvs:
            print(f'The root it service {self.service_name} and all of dependencies will be deleted')
            self.hard_service_delete(rootsrv)


def main(args, subcmd_args):

    parser = argparse.ArgumentParser('it_service_tool.py')
    parser.add_argument('action', choices=['create', 'delete'], help="Create\Delete IT service Tre")
    parser.add_argument('-n', '--service-name', required=True, help="The Name of IT service Tree's root")
    parser.add_argument('-g', '--group-name', help="Create IT service tree from the Group")
    local_args = parser.parse_args(subcmd_args)

    zapi = ZabbixAPI(args.zbx_server, timeout=60)
    zapi.validate_certs = False
    zapi.login(user=args.zbx_user, password=args.zbx_passwd)

    def create(local_args):
        CreateItService(zapi, local_args.service_name, local_args.group_name).create()

    def delete(local_args):
        DeleteItService(zapi, local_args.service_name).delete()

    f = locals().get(local_args.action)
    f(local_args)

    zapi.logout()


if __name__ == '__main__':
    main(args, subcmd_args)
