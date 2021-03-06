import os                                                                              
import sys

from osdk.keystone import keystone
from osdk.nova import nova

keystone_task = keystone.Keystone('114.212.189.132', '5000', '5000', 
                            '35357', 'admin', 'admin', 'ADMIN_PASS')
nova_task = nova.Nova(keystone_task)
print nova_task.list_servers()
print nova_task.list_flavors()
print nova_task.list_images()
print nova_task.create_server(name='from_sdk_server', flavorRef='2', 
                            imageRef='0d192c86-1a92-4ac5-97da-f3d95f74e811', 
                            network_id='da002e34-57bb-492f-897b-6ed317b97cfc')
