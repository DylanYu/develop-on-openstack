import os
import sys

reldir = os.path.join(os.path.dirname(__file__), '..', '..')
absdir = os.path.abspath(reldir)
sys.path.append(absdir)

from keystone.keystone import *
from nova.nova import *
from neutron.neutron import *
from template.flat_net import *
from template.instance_launcher import *

keystone_task = Keystone('114.212.189.132', '5000', 'admin', 'admin', 'ADMIN_PASS')
neutron_task = Neutron(keystone_task)
nova_task = Nova(keystone_task)

flat_network = FlatNet(neutron_task)
print flat_network.get_network_id()

launcher = InstanceLauncher(nova_task, flat_network)
launcher.launch_ubuntus()

