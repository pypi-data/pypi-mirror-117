# zbxtool

通过subcommand合并hostgrp-poc， discoverd-hosts-name-back， zabbix-vmware-host-inventory, it_service_tool
四个项目, 包含上述四个项目的功能。

# 说明
- 子命令:

    **vmware-host-inventory**: 通过Api读取vCenter信息，更新 Zabbix 中 Hypervisors 组中Host的 inventory 信息。

    **host-group-poc**: 读取ldap人员信息, 更新 Zabbix 中各组主机的 inventory。

    **host-name-back**: 消除 Zabbix 中 Discovered Hosts 组中hostname 末尾的下划线+数字的情况。

    **service**: 在 Zabbix 中 依据主机组生成it-service树

    **es-zabbix**: 将 Zabbix 中各主机的inventory信息采集至ElasticSearch的Index中


# 使用
* `python setup.py install`


* 各子命令参数:

`zbxtool -s ZBX_URL -u ZBX_USER -p ZBX_PWD  (host-name-back|vmware-host-inventory|vmware-host-inventory|service|es-zabbix) --other-params value `

# 示例
- zbxtool -s http://10.189.67.39/zabbix -u liusong -p password host-name-back

- zbxtool -s http://10.189.67.39/zabbix -u liusong -p password vmware-host-inventory

- zbxtool -s http://10.189.67.39/zabbix -u liusong -p password service delete --service-name test

- zbxtool -s http://10.189.67.39/zabbix -u liusong -p password service create --service-name test --group-name Orabbix

- zbxtool -s http://10.189.67.39/zabbix -u liusong -p password es-zabbix --es_url 10.189.67.26 [--es_user] [--es_passwd]

- zbxtool -s http://10.189.67.39/zabbix -u liusong -p password host-group-poc -c Contacts.json --ldap-server 10.189.67.14 --ldap-user cn=Manager,dc=shchinafortune,dc=local --ldap-password password
