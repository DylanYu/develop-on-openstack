# SDK for Ceilometer ReSTful API

import requests, json

class Ceilometer:

    def __init__(self, keystone):
        self.keystone = keystone

