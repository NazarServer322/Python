# pip install pypiwin32 before start script 
from ast import Expression
from dataclasses import replace
from logging import exception
import platform
import win32serviceutil
import time
hostname = platform.uname()[1]
host = "Hostname="
changehost = "Hostname=hostname"
willreplece = host + hostname
Server = "Server=127.0.0.1"
ServerWillReplece = "Server=10.7.0.209"
ServerActive = "ServerActive=127.0.0.1"

try:
    with open(r'zabbix_agentd.win.conf', 'r') as file:
        data = file.read()
        data = data.replace(changehost, willreplece)
except Exception as f :
    print("Already changed", f)
with open(r'zabbix_agentd.win.conf', 'w') as file:
    file.write(data)
with open(r'zabbix_agentd.win.conf', 'r') as file:
    data = file.read()
    data = data.replace(Server, ServerWillReplece)
with open(r'zabbix_agentd.win.conf', 'w') as file:
    file.write(data)
with open(r'zabbix_agentd.win.conf', 'r') as file:
    data = file.read()
    data = data.replace(ServerActive, ServerWillReplece)
with open(r'zabbix_agentd.win.conf', 'w') as file:
    file.write(data)
ZabbixAgentService = "Zabbix Agent"
win32serviceutil.RestartService(ZabbixAgentService)
time.sleep(5)
start = win32serviceutil.StartService(ZabbixAgentService)
