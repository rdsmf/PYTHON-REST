#!/usr/local/bin/python
# Print ACI Fabric Mmembership of a given APIC

# Importing necessary modules
import requests
import sys
import json
import os

# Disable warnings (SSL self signed cert)
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Variable for the APIC controller IP or DNS
apic_url = "http://<ip address or dns>/"

# This function allows you to view the fabric membership
url = apic_url + ''

# The username and password to access the APIC
username=’<username>'
password=’<password>'

# Content type must be included in the header
myheaders={'content-type':'application/json-rpc'}

# Perform a GET on the specified url
response = requests.get(url,headers=myheaders,auth=(username,password),verify=False).json()

# This last line prints output to the screen.
print json.dumps (response, indent=4, separators=(',', ': '))