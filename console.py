import cmd
from pathlib import Path
from models import config
from models import bridge
import requests
import json


class hue_house(cmd.Cmd):
    prompt = "(hue) "

    file_path = Path('./.config')
    if file_path.is_file():
        bridge = config.reload()
    else:
        bridge = bridge.Bridge()
    
    def do_test(self, arg):
        print(self.bridge.username)

    def do_quit(self, arg):
        return True

    def do_emptyline(self, arg):
        return
    
    def do_lights(self, arg):
        args = arg.split()
        light_group = {
                "livingroom" : "1",
                "walkway" : "2",
                "bedroom" : "3",
                "outside" : "5"
                }
        body = {
               "on" : True
                }
        
        if args[1] == "off":
            body["on"] = False

        lights_url = self.bridge.url + self.bridge.username + "/groups/" + light_group.get(args[0]) + "/" + "action"
        request = requests.put(lights_url, data=json.dumps(body))        


if __name__ == "__main__":
    hue_house().cmdloop()
