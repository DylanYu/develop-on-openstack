import os
import sys

reldir = os.path.join(os.path.dirname(__file__), '..', '..')
absdir = os.path.abspath(reldir)
sys.path.append(absdir)

from keystone import keystone
from nova import nova
from neutron import neutron
from template import flat_net
from template import instance_launcher

keystone_task = keystone.Keystone('114.212.189.132', '5000', '5000', '35357', 
                        'admin', 'admin', 'ADMIN_PASS')
neutron_task = neutron.Neutron(keystone_task)
nova_task = nova.Nova(keystone_task)

flat_network = flat_net.FlatNet(neutron_task)
print flat_network.get_network_id()

launcher = instance_launcher.InstanceLauncher(nova_task, flat_network)
launcher.launch_ubuntus()

