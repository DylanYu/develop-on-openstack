import os                                                                              
import sys

reldir = os.path.join(os.path.dirname(__file__), '..', '..')
absdir = os.path.abspath(reldir)
sys.path.append(absdir)

from keystone.keystone import *
from nova.nova import *

keystone_task = Keystone('114.212.189.132', '5000', 'admin', 'admin', 'ADMIN_PASS')
nova_task = Nova(keystone_task)
print nova_task.list_servers()
print nova_task.list_flavors()
print nova_task.list_images()
print nova_task.create_server(name='from_sdk_server', flavorRef='2', imageRef='0d192c86-1a92-4ac5-97da-f3d95f74e811', network_id='909b5bff-9ac6-4470-a5b0-07b7df51a08c')
