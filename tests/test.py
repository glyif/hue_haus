from models.bridge import Bridge
from models import config

new = Bridge()

new.save()
new_json = new.to_json()
print(new_json)
