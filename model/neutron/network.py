
class Network:
    def __init__(self, name, admin_state_up=True, shared=False, tenant_id=None):
        self.name = name
        self.admin_state_up = admin_state_up
        self.shared = shared
        self.tenant_id = tenant_id
        # TODO: elegant attribute setter
        """
        self.data = {}
        self['name'] = name
        self['admin_state_up'] = admin_state_up
        self['shared'] = shared
        self['tenant_id'] = tenant_id
        """
    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def show(self):
        """
        print self['name']
        print self['admin_state_up']
        print self['shared']
        print self['tenant_id']
        """
        print self.name
        print self.admin_state_up
        print self.shared
        print self.tenant_id

    def show_all(self):
        print self.uuid
        print self.name
        print self.admin_state_up
        print self.status
        print self.subnets
        print self.shared
        print self.tenant_id
