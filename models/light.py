from models.bridge import Bridge
from models import light_config
import json
import requests

class Light():
    def __init__(self, bridge, *args):
        if len(args) > 0:
            self.__dict__ = args[1]
        self.light_url = bridge.url + bridge.username + '/' + 'lights/' + args[0]
        light_config.new() 
        light_config.save()

    @staticmethod
    def import_obj(bridge):
        lights_url = bridge.url + bridge.username + '/' + 'lights'
        request = requests.get(lights_url)
        response = request.json()
    
        eval("Light")(bridge, item, response.get(item))


