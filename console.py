import cmd
from pathlib import Path
from models import config
from models import bridge

class hue_house(cmd.Cmd):
    prompt = "(hue) "

    file_path = Path('./.config')
    if file_path.is_file():
        bridge = config.reload()
    else:
        bridge = Bridge()
    
    def do_test(self, arg):
        print(self.bridge.username)

    def do_quit(self, arg):
        return True

    def do_emptyline(self, arg):
        return
if __name__ == "__main__":
    hue_house().cmdloop()
