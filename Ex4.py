#!/usr/bin/env python

SNMP_PORT = 161
OID_NAME = '.1.3.6.1.2.1.1.5.0'
OID_DESC = '.1.3.6.1.2.1.1.1.0'

import snmp_helper

pynet_rtr1 = ('cisco1.twb-tech.com', 'galileo', SNMP_PORT)
pynet_rtr2 = ('cisco2.twb-tech.com', 'galileo', SNMP_PORT)

def print_details(router):
  router_name = snmp_helper.snmp_get_oid(router, OID_NAME, False)
  router_desc = snmp_helper.snmp_get_oid(router, OID_DESC, False)

  print 'Name: ' + snmp_helper.snmp_extract(router_name)
  print 'Description: ' + snmp_helper.snmp_extract(router_desc)

def main():
  print_details(pynet_rtr1)
  print ''
  print_details(pynet_rtr2)

if __name__ == '__main__':
  main()
