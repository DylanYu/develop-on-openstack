# SDK for Neutron ReSTful API

import requests, json

class Neutron:

    def __init__(self, keystone):
        self.keystone = keystone
        self.public_urls = keystone.get_neutron_public_urls()
        self.create_headers()
        """treat keystone host as neutron host, typically"""
        """TODO: set neutron host"""
        self.amend_url(keystone.get_keystone_host())

    def amend_url(self, correct_host_name):
        if not hasattr(self, 'public_urls'):
            return
        urls = []
        for url in self.public_urls:
            urls.append(url.replace('controller', correct_host_name))
            self.public_urls = urls

    def create_headers(self):
        token_id = self.keystone.get_token_id()
        self.headers = {
            "Content-type": "application/json",
            "Accept": "application/json", 
            'X-Auth-Token':token_id,
        }


    """Network related operations"""

    def list_networks(self):
        public_url = self.public_urls[0]
        url = public_url + '/v2.0/networks'
        response = requests.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def show_network(self):
        pass

    def create_network(self, name, admin_state_up=True):
        public_url = self.public_urls[0]
        url = public_url + '/v2.0/networks'
        net_info = {
            'network': {
                'name': name,
                'admin_state_up': 'true' if admin_state_up else 'false',
            },
        }
        response = requests.post(url, data=json.dumps(net_info), headers=self.headers)
        status_code = response.status_code
        if status_code == 201:
            data = response.json()
            return data
        else:
            return None

    def update_network(self):
        pass

    def delete_network(self):
        pass


    """Subnet related operations"""

    def list_subnets(self):
        public_url = self.public_urls[0]
        url = public_url + '/v2.0/subnets'
        response = requests.get(url, headers=self.headers)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            return data
        else:
            return None

    def show_subnet(self):
        pass

    def create_subnet(self, name, network_id, cidr, allocation_start, allocation_end, ip_version=4):
        public_url = self.public_urls[0]
        url = public_url + '/v2.0/subnets'
        subnet_info = {
            'subnet': {
                'name': name,
                'network_id': network_id,
                'ip_version': ip_version,
                'cidr': cidr,
                'allocation_pools':[
                    {
                        'start': allocation_start,
                        'end': allocation_end,
                    }
                ]
            },
        }
        response = requests.post(url, data=json.dumps(subnet_info), headers=self.headers)
        status_code = response.status_code
        if status_code == 201:
            data = response.json()
            return data
        else:
            return None

    def create_sample_subnet(self, network_id):
        # TODO: set typical config
        name = 'sample_subnet'
        cidr = '100.0.0.0/24'
        allocation_start = '100.0.0.2'
        allocation_end = '100.0.0.254'
        ip_version = 4
        return self.create_subnet(name=name, network_id=network_id, 
                        cidr=cidr, allocation_start=allocation_start, 
                        allocation_end=allocation_end, ip_version=ip_version)

    def update_subnet(self):
        pass

    def delete_subnet(self):
        pass


    """Port related operations"""

    def list_ports(self):
        pass

    def show_port(self):
        pass

    def create_port(self):
        pass

    def update_port(self):
        pass

    def delete_port(self):
        pass

