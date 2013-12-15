# SDk for Keytron ReSTful API


import requests, json

class Keystone:

    def __init__(self, keystone_host, keystone_port, tenant_name, username, password):
        self.set_keystone_endpoint(keystone_host, keystone_port)
        self.set_user(tenant_name, username, password)
        self.authenticate()

    def set_keystone_endpoint(self, keystone_host, keystone_port):
        self.keystone_host = keystone_host
        self.keystone_port = keystone_port

    def set_user(self, tenant_name, username, password):
        self.tenant_name = tenant_name
        self.username = username
        self.password = password

    def authenticate(self):
        url = 'http://' + self.keystone_host + ':' + self.keystone_port + '/v2.0/tokens'
        user_info ={
            "auth":{
                "tenantName":self.tenant_name, 
                "passwordCredentials":{
                    "username":self.username,
                    "password":self.password
                }
            }
        }
        headers = {"Content-type": "application/json","Accept": "application/json"}
        response = requests.post(url, data=json.dumps(user_info), headers=headers)
        self.status_code = response.status_code
        if self.status_code == 200:
            self.auth_data = response.json()
            self.parse_auth_data(self.auth_data)
            return True
        else:
            """deal with faults"""
            print 'Authentication failed.'
            return False

    def parse_auth_data(self, auth_data):
        self.token_id = str(self.auth_data['access']['token']['id'])
        service_catalog_list = self.auth_data['access']['serviceCatalog']
        self.nova_public_urls = []
        self.neutron_public_urls = []
        for service in service_catalog_list:
            if service['name'] == 'nova':
                for endpoint in service['endpoints']:
                    self.nova_public_urls.append(endpoint['publicURL'])
            if service['name'] == 'neutron':
                for endpoint in service['endpoints']:
                    self.neutron_public_urls.append(endpoint['publicURL'])

    def is_authenticated(self):
        return self.status_code == 200

    def get_token_id(self):
        if not self.is_authenticated():
            return None
        else:
            return self.token_id

    def get_nova_public_urls(self):
        if not self.is_authenticated():
            return None
        else:
            return self.nova_public_urls

    def get_neutron_public_urls(self):
        if not self.is_authenticated():
            return None
        else:
            return self.neutron_public_urls

    def get_keystone_host(self):
        return self.keystone_host

