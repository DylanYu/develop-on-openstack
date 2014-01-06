
import json

class OpenStackException(Exception):
    def __init__(self, response):
        self.status = response.status

