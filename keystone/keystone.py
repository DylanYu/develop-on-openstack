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
            self.token_id = str(self.auth_data['access']['token']['id'])
            return True
        else:
            """deal with faults"""
            print 'Authentication failed.'
            return False

    def get_token_id(self):
        if self.status_code != 200:
            return None
        else:
            return self.token_id

