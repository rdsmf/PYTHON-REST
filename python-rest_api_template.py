#!/usr/local/bin/python

# Importing necessary modules
import requests
import sys
import json
import os

#Disable warnings
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Put the IP address of your switch in this URL
url = 'https://<switch ip address>/inst.json'

# The username and password to access the APIC/switch
payload = {"username":"<username>","password":"<password>"}

# Content type must be included in the header
header = {"content-type": "application/json"}

# Perform a POST on the specified url.
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

# Print the JSON that is returned
print(response.text)

