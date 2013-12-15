import os
import sys

reldir = os.path.join(os.path.dirname(__file__), '..')
absdir = os.path.abspath(reldir)
sys.path.append(absdir)

from neutron.neutron import *

class FlatNet:

    def __init__(self, neutron_task):
        self.neutron_task = neutron_task
        self.create_flat_networking()

    def create_flat_networking(self):
        # TODO: name
        network = self.neutron_task.create_network(name='My_Flat_Network')
        self.network_id = str(network['network']['id'])
        # TODO: update create_sample_subnet
        subnet = self.neutron_task.create_sample_subnet(self.network_id)
        return self.network_id

    def get_network_id(self):
        return self.network_id

