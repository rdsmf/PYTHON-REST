#!/usr/local/bin/python
# Print Chassis info, Hostname and software version of a given switch

# Importing necessary modules
import requests
import sys
import json
import os

# Disable warnings (SSL self signed cert)
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

print "enter ip address"
ip=raw_input()

print "enter vlan to be configured"
vlanId=raw_input()

# Put the IP address of your switch in this URL
url = "http://"+ip+"/ins"

# The username and password to access the switch
username=’<username>'
password=’<password>'

# Content type must be included in the header
myheaders={'content-type':'application/json-rpc'}

# Content - REST API COMMAND
payload=[
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "vlan "+vlanId+,"version": 1},"id": 2},
  {"jsonrpc": "2.0","method": "cli","params": {"cmd": "exit","version": 1},"id": 3}
]

# Perform a POST on the specified url
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()

