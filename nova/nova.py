# SDK for Nova ReSTful API

import requests, json

class Nova:

    def __init__(self, keystone_host, keystone_port, tenant_name, username, password):
        self.set_keystone_endpoint(keystone_host, keystone_port)
        self.set_user(tenant_name, username, password)
        self.authenticate()
        self.get_info_from_auth_data()
        """treat keystone host as neutron host, typically"""
        """TODO: set neutron host"""
        self.amend_url(keystone_host)

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
        status_code = response.status_code
        if status_code == 200:
            self.auth_data = response.json()
        else:
            """deal with faults"""
            print 'deal with faults'

    def get_info_from_auth_data(self):
        if not hasattr(self, 'auth_data'):
            return
        self.token_id = str(self.auth_data['access']['token']['id'])
        self.headers = {
            "Content-type": "application/json",
            "Accept": "application/json", 
            'X-Auth-Token':self.token_id
        }
        service_catalog_list = self.auth_data['access']['serviceCatalog']
        self.public_urls = []
        for service in service_catalog_list:
            if service['name'] == 'nova':
                for endpoint in service['endpoints']:
                    self.public_urls.append(endpoint['publicURL'])

    def amend_url(self, correct_host_name):
        if not hasattr(self, 'public_urls'):
            return
        urls = []
        for url in self.public_urls:
            urls.append(url.replace('controller', correct_host_name))
            self.public_urls = urls


    """Server related operations"""

    def list_flavors(self):
        public_url = self.public_urls[0]
        url = public_url + '/flavors'
        response = requests.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def list_images(self):
        public_url = self.public_urls[0]
        url = public_url + '/images'
        response = requests.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def list_servers(self):
        public_url = self.public_urls[0]
        url = public_url + '/servers'
        response = requests.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def show_server(self):
        pass

    def create_server(self, name, flavorRef, imageRef, network_id):
        public_url = self.public_urls[0]
        url = public_url + '/servers'
        server_info = {
            'server': {
                'name': name,
                'flavorRef': public_url + '/flavors/' + flavorRef,
                'imageRef': public_url + '/images/' + imageRef,
                'networks': [
                    {
                        'uuid': network_id
                    }
                ]
            }
        }
        response = requests.post(url, data=json.dumps(server_info), headers=self.headers)
        status_code = response.status_code
        if status_code == 202:
            data = response.json()
            return data
        else:
            return None

    def update_server(self):
        pass

    def delete_server(self):
        pass

