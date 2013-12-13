import json, requests

url = "http://114.212.189.132:5000/v2.0/tokens"
post_data = {"auth":{"tenantName":"admin", "passwordCredentials":{"username":"admin","password":"ADMIN_PASS"}}}
headers = {"Content-type": "application/json","Accept": "application/json"}
response = requests.post(url, data=json.dumps(post_data), headers=headers)
data = response.json()

token_id = data['access']['token']['id']
token_issued_at = data['access']['token']['issued_at']
token_expires = data['access']['token']['expires']
#print 'Issused at:%s\nExpires:%s\nToken:%s' % (token_issued_at, token_expires, token_id)
service_catalog_list = data['access']['serviceCatalog']
nova = dict()
neutron = dict()
nova_url = ''
neutron_url = ''
for service in service_catalog_list:
    #print service['type'], service['name']
    if service['name'] == 'nova':
        nova_url = service['endpoints'][0]['publicURL']
    if service['name'] == 'neutron':
        neutron_url = service['endpoints'][0]['publicURL']

#print nova_url, neutron_url

#print service_catalog_list
url = nova_url + '/servers'
url = url.replace('controller', '114.212.189.132')
print url
post_data = {'X-Auth-Token':token_id}
response = requests.post(url, data=json.dumps(post_data), headers=headers)
#data = response.json()
#servers = data['servers']
#print servers
