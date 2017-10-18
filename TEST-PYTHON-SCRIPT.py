import json
import requests

base_url = 'https://192.168.250.50/api/'

# create credentials structure
name_pwd = {'aaaUser': {'attributes': {'name': 'admin', 'pwd': 'Pl3xeCu73!'}}}
json_credentials = json.dumps(name_pwd)

# log in to API
login_url = base_url + 'aaaLogin.json'
post_response = requests.post(login_url, data=json_credentials)

# get token from login response structure
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']

# create cookie array from token
cookies = {}
cookies['APIC-Cookie'] = auth_token

# read a sensor, incorporating token in request
sensor_url = base_url + 'node/mo/topology/pod-1/node-1/av.json?query-target=children&target-subtree-class=infraWiNode'
get_response = requests.get(sensor_url, cookies=cookies, verify=False)

# display sensor data structure
print get_response.json()


