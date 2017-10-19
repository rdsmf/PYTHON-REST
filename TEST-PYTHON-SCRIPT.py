#!/usr/local/bin/python
# Print ACI Fabric Mmembership of a given APIC

# Importing necessary modules
import requests
import sys
import json
import os

base_url = 'https://<apic ip address>/api/'

# create credentials structure
name_pwd = {'aaaUser': {'attributes': {'name': '<username>', 'pwd': '<password>'}}}
json_credentials = json.dumps(name_pwd)

# log in to APIC
login_url = base_url + '/api/aaaLogin.json'
post_response = requests.post(login_url, data=json_credentials)

# get token from login response structure
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']

# create cookie array from token
cookies = {}
cookies['APIC-Cookie'] = auth_token

# read a sensor health, incorporating token in request
sensor_url = base_url + 'node/mo/topology/pod-1/node-1/av.json?query-target=children&target-subtree-class=infraWiNode'
get_response = requests.get(sensor_url, cookies=cookies, verify=False)

# display sensor data structure
print get_response.json()


