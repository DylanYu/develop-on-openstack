import os
import sys

from osdk.keystone import keystone
from osdk.neutron import neutron
from osdk.model.neutron import network

keystone_task = keystone.Keystone('114.212.189.132', '5000', '5000', 
                                '35357', 'admin', 'admin', 'ADMIN_PASS')
neutron_task = neutron.Neutron(keystone_task)

network = network.Network('sdk_test_network') 
print neutron_task.create_network(network)
networks = neutron_task.list_networks()
for e in networks:
    print e
    print

#print neutron_task.delete_network(network)
#print neutron_task.list_subnets()
#print neutron_task.create_subnet(name='net_sub', 
#                        network_id='7745f621-9463-4a0b-afcd-d3859e0477b4', 
#                        ip_version=4,cidr='10.50.0.0/24', 
#                        allocation_start='10.50.0.2', 
#                        allocation_end='10.50.0.254')
