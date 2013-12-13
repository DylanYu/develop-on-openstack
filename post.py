import json, requests

url = "http://114.212.189.132:5000/v2.0/tokens"
post_data = {"auth":{"tenantName":"admin", "passwordCredentials":{"username":"admin","password":"ADMIN_PASS"}}}
headers = {"Content-type": "application/json","Accept": "application/json"}
response = requests.post(url, data=json.dumps(post_data), headers=headers)
data = response.json()

token_id = str(data['access']['token']['id'])
token_issued_at = str(data['access']['token']['issued_at'])
token_expires = str(data['access']['token']['expires'])
#print 'Issused at:%s\nExpires:%s\nToken:%s' % (token_issued_at, token_expires, token_id)

service_catalog_list = data['access']['serviceCatalog']
nova_url = ''
neutron_url = ''
for service in service_catalog_list:
    if service['name'] == 'nova':
        nova_url = service['endpoints'][0]['publicURL']
    if service['name'] == 'neutron':
        neutron_url = service['endpoints'][0]['publicURL']

# list
url = neutron_url + '/v2.0/networks'
url = url.replace('controller', '114.212.189.132')
print url
headers = {"Content-type": "application/json","Accept": "application/json", 'X-Auth-Token':token_id}
response = requests.get(url, headers=headers)
print 'status code: ', response.status_code
print 'reason: ', response.reason
print response.text

# create
post_data = {
 "network":
  {
    "name": "sample_network", 
    "admin_state_up": 'true'
  }
}
response = requests.post(url, data=json.dumps(post_data), headers=headers)
print 'status code: ', response.status_code
print 'reason: ', response.reason
print response.text

# delete
"""
url = url + '/35ca32bd-c050-401d-a5c6-55f06a5392ca'
response = requests.delete(url, headers=headers)
print 'status code: ', response.status_code
print 'reason: ', response.reason
print response.text
"""
