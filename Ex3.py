#!/usr/bin/env python

TELNET_PORT = 23
TELNET_TIMEOUT = 6

import time
import telnetlib
import socket
import sys

class TelnetHelper:
  def __init__(self, ip_addr, username, password):
    self.ip_addr = ip_addr
    self.username = username
    self.password = password

    try:
      self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
      sys.exit("Connection Timed Out")

  def logon(self):
    self.remote_conn.read_until('sername:', TELNET_TIMEOUT)
    self.remote_conn.write(self.username + '\n')
    self.remote_conn.read_until('ssword:', TELNET_TIMEOUT)
    self.remote_conn.write(self.password + '\n')
    time.sleep(1)
    self.remote_conn.read_very_eager()
    
  def send_command(self, command):
    self.remote_conn.write(command + '\n')
    time.sleep(1)
    return self.remote_conn.read_very_eager()

  def disable_paging(self):
    self.send_command('terminal length 0')

  def close_conn(self):
    self.remote_conn.close()
    self.remote_conn = None

def main():
  ip_addr = 'cisco1.twb-tech.com'
  username = 'pyclass'
  password = '88newclass'

  th = TelnetHelper(ip_addr, username, password)
  th.logon()
  th.disable_paging()
  output = th.send_command('show ip int brief')
  
  print output
  th.close_conn()

if __name__ == "__main__":
  main()
