#!/usr/local/bin/python
# Print interface and IP address of a given switch

# Importing necessary modules
import requests
import sys
import json
import os

# Disable warnings (SSL self signed cert)
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Host information
hosts = [
    "10.1.1.1",
    "10.1.1.2"
]

# Put the IP address of your switch in this URL
url='http://"+hosts+"/ins'

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
"cmd": "sh ip interface br",
"version": 1
},
"id": 1
}
]

# Perform a POST on the specified url
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password), verify=False).json()

#this last line is not included in NXAPI output. Prints output to the screen.
print json.dumps (response)
