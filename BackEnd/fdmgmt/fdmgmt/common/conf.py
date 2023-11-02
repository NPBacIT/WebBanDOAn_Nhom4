import os
from configobj import ConfigObj

CONF_FILE = os.path.abspath(os.path.join(
                            os.path.dirname(os.path.abspath(__file__)),
                            "../../etc/default.conf"))
                            
def load_config():
    config = ConfigObj(CONF_FILE, list_values=True)
    return config

CONF = load_config()