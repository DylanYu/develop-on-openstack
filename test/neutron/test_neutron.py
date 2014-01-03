import os
import sys

reldir = os.path.join(os.path.dirname(__file__), '..', '..')
absdir = os.path.abspath(reldir)
sys.path.append(absdir)

from keystone.keystone import *
from neutron.neutron import *
from model.neutron.network import *

keystone_task = Keystone('114.212.189.132', '5000', '5000', '35357', 'admin', 'admin', 'ADMIN_PASS')
neutron_task = Neutron(keystone_task)

network = Network('sdk_test_network') 
print neutron_task.create_network(network)
networks = neutron_task.list_networks()
for e in networks:
    print e
    print

#print neutron_task.delete_network(network)
#print neutron_task.list_subnets()
#print neutron_task.create_subnet(name='net_sub', network_id='909b5bff-9ac6-4470-a5b0-07b7df51a08c', 
#            ip_version=4,cidr='10.50.0.0/24', 
#            allocation_start='10.50.0.2', allocation_end='10.50.0.254')
