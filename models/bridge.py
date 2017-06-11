import requests
import asyncio
import json
from uuid import uuid4
from models import config

class Bridge:
    def __init__(self, *args):
        if len(args) > 0:
            self.__dict__ = args[0]
        else:
            self.ip = self.get_ip()
            self.url = "http://" + self.ip + '/api/'
            self.username = None
            self.make_user()
            self.id = str(uuid4())
            config.new(self)

    def save(self):
        config.save()

    def connect(self):
        bridge_config = self.url + self.username
        request = requests.get(bridge_config)


    def get_ip(self):
        url = 'http://www.meethue.com/api/nupnp'
        request = requests.get(url)
        response = request.json()
        for item in response:
            for key in item:
                if key == 'internalipaddress':
                    return (item.get(key))
    
    @asyncio.coroutine
    def attempt_user(self):
        new_user = {"devicetype": "hue_haus#device"}
        while self.username is None:
            request = requests.post(self.url, data=json.dumps(new_user))
            response = request.json()
            for item in response:
                if 'error' in item.keys():
                    print("push button within 30 seconds")
                else:
                    self.username = item["success"]["username"]
                yield from asyncio.sleep(1)

    def make_user(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.attempt_user())
        loop.close()

    def to_json(self):
        return self.__dict__
