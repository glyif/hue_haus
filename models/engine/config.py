import json

class Config:
    def __init__(self):
        self.__file_path = "./.config"
        self.__config = {}

    def new(self, obj):
        self.__config[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        json_obj = {}
        for key in self.__config.keys():
            json_obj[key] = self.__config[key].to_json()
        with open(self.__file_path, mode='w') as fd:
            fd.write(json.dumps(json_obj))
    
    def reload(self):
        try:
            with open(self.__file_path, mode='r') as fd:
                read = fd.read()
                dump = json.loads(read)
                from models.bridge import Bridge
                for key, value in dump.items():
                    return (eval("Bridge")(dump[key]))
        except FileNotFoundError:
            pass
