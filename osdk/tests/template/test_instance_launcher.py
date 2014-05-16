import os
import sys

from osdk.keystone import keystone
from osdk.nova import nova
from osdk.neutron import neutron
from osdk.template import flat_net
from osdk.template import instance_launcher

keystone_task = keystone.Keystone('114.212.189.132', '5000', '5000', '35357', 
                        'admin', 'admin', 'ADMIN_PASS')
neutron_task = neutron.Neutron(keystone_task)
nova_task = nova.Nova(keystone_task)

flat_network = flat_net.FlatNet(neutron_task)
print flat_network.get_network_id()

launcher = instance_launcher.InstanceLauncher(nova_task, flat_network)
launcher.launch_ubuntus()

