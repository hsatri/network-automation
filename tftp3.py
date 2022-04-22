#!/usr/bin/env python3
#-*- conding: utf-8 -*-

from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException
from netmiko import AuthenticationException
from netmiko import SSHException

SERV_TFTP = "43.15.24.2"

R1 = {'device_type': 'cisco_ios', 'host': '10.15.6.2', 'username': 'hatim', 'password': 'cisco', 'secret': 'cisco'}
R2 = {'device_type': 'cisco_ios', 'host': '11.1.6.2', 'username': 'hatim', 'password': 'cisco', 'secret': 'cisco'}
R3 = {'device_type': 'cisco_ios', 'host': '16.15.6.2', 'username': 'hatim', 'password': 'cisco', 'secret': 'cisco'}
R4 = {'device_type': 'cisco_ios', 'host': '13.15.14.2', 'username': 'hatim', 'password': 'cisco', 'secret': 'cisco'}
R5 = {'device_type': 'cisco_ios', 'host': '24.1.24.1', 'username': 'hatim', 'password': 'cisco', 'secret': 'cisco'}
R6 = {'device_type': 'cisco_ios', 'host': '19.1.19.2', 'username': 'hatim', 'password': 'cisco', 'secret': 'cisco'}

my_devices = [R1, R2, R3, R4, R5, R6]

for device in my_devices:
    i += 1
    name = f"R{str(i)}"
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    copy_command = f"copy start tftp://{SERV_TFTP}/{name}.conf"
    output = net_connect.send_command_timing(copy_command)
    if "Address or name" in output:
        output += net_connect.send_command_timing("\n")
    if "Destination filename" in output:
        output += net_connect.send_command_timing("\n")
    print(output)
    net_connect.exit_enable_mode()



