
class InstanceLauncher:

    def __init__(self, nova, network):
        self.nova = nova
        self.network = network
        self.set_flavors()
        self.set_images()

    def set_flavors(self):
        # TODO
        self.flavor_id_tiny = '1'
        self.flavor_id_small = '2'
        self.flavor_id_medium = '3'
        self.flavor_id_large = '4'
        self.flavor_id_xlarge = '5'

    def set_images(self):
        # TODO
        self.image_id_ubuntu = 'b8575247-a42a-479e-af88-172222d64f70'
        self.image_id_cirros = '0d192c86-1a92-4ac5-97da-f3d95f74e811'

    def launch_ubuntus(self, flavor='2', number=5):
        for i in range(number):
            print self.launch_ubuntu(flavor)

    def launch_ubuntu(self, flavor='2'):
        return self.nova.create_server('ubuntu', flavor, self.image_id_ubuntu, self.network.get_network_id())

