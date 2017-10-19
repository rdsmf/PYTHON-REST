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

# Put the IP address of your switch in this URL
url = "http://"+ip+"/ins"

# The username and password to access the switch
username=’<username>'
password=’<password>'

# Content type must be included in the header
myheaders={'content-type':'application/json-rpc'}

# Content - REST API COMMAND
payload=[
{
"jsonrpc": "2.0",
"method": "cli",
"params": {
"cmd": "show version",
"version": 1
},
"id": 1
}
]

# Perform a POST on the specified url
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()

#Now Process the response
kick_start_image = response['result']['body']['kickstart_ver_str']
chassis_id = response['result']['body']['chassis_id']
hostname =  response['result']['body']['host_name']

print "ip : {0} is a \"{1}\" with hostname: {2} running software version : {3}".format(ip , chassis_id, hostname, kick_start_image)
