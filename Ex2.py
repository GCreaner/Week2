#!/usr/bin/env python

TELNET_PORT = 23
TELNET_TIMEOUT = 6

import time
import telnetlib

ip_addr = 'cisco1.twb-tech.com'
username = 'pyclass'
password = '88newclass'

def logon(ip_addr, username, password):
  remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
  remote_conn.read_until('sername:', TELNET_TIMEOUT)
  remote_conn.write(username + '\n')
  remote_conn.read_until('ssword:', TELNET_TIMEOUT)
  remote_conn.write(password + '\n')

  time.sleep(1)
  remote_conn.read_very_eager()

  return remote_conn

def send_command(remote_conn, command):
  remote_conn.write(command + '\n')
  time.sleep(1)
  return remote_conn.read_very_eager()

def main():
  remote_conn = logon(ip_addr, username, password)  
  print send_command(remote_conn, 'show ip int brief')

if __name__ == "__main__":
  main()
