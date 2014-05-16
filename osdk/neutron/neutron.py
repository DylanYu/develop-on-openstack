# SDK for Neutron ReSTful API

import os
import sys

import requests
import json

from osdk.model.neutron.network import *

class Neutron:

    def __init__(self, keystone):
        self.keystone = keystone
        self.public_urls = keystone.get_neutron_public_urls()
        self.create_headers()
        # treat keystone host as neutron host, typically
        # TODO: set neutron host
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
            networks = []
            for e in data['networks']:
                network = Network(e['name'], e['admin_state_up'], e['shared'], e['tenant_id'])
                network.status = e['status']
                network.uuid = e['id']
                network.subnets = []
                for subnet_id in e['subnets']:
                    network.subnets.append(subnet_id)
                networks.append(network)
            return networks
        else:
            return None

    def show_network(self):
        pass

    def create_network(self, network):
        """Create a network defined by model

        The network model only provides attributes name, admin_state_up and 
        shared. After we successfully create the network and get the uuid 
        responsed by server, we set uuid into the network object.

        :param network: network object, with name, admin_state_up and shared 
                        attributes already set.
        """
        public_url = self.public_urls[0]
        url = public_url + '/v2.0/networks'
        net_info = {
            'network': {
                'name': network.name,
                'admin_state_up': 'true' if network.admin_state_up else 'false',
                'shared': 'true' if network.shared else 'false',
                'tenant_id': self.keystone.get_tenant_id(),
            },
        }
        response = requests.post(url, data=json.dumps(net_info), headers=self.headers)
        status_code = response.status_code
        if status_code == 201:
            data = response.json()
            network.uuid = data['network']['id']
            print data
            return True
        else:
            return False

    def update_network(self):
        pass

    def delete_network(self, network):
        return self.delete_network_by_id(network.uuid)

    def delete_network_by_id(self, network_id):
        public_url = self.public_urls[0]
        url = public_url + '/v2.0/networks/' + network_id
        response = requests.delete(url, headers=self.headers)
        status_code = response.status_code
        if status_code == 204:
            return True
        else:
            print 'Delete Network Failed.'
            return False


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

