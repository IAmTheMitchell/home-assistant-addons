import logging
import json
from datetime import datetime
from os import access, R_OK
from os.path import isfile
from typing import Dict
# from renogybt import InverterClient, RoverClient, RoverHistoryClient, BatteryClient, DataLogger, Utils


def is_readable(file):
    return isfile(file) and access(file, R_OK)

def load_user_config():
    try:
        with open('/data/options.json') as f:
            conf = dotdict(json.load(f))
    except Exception as e:
        print('error reading /data/options.json, trying options.json', e)
        with open('options.json') as f:
            conf = dotdict(json.load(f))
    return conf

class dotdict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError as e:
            raise AttributeError(e)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

# Set up logger 
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Load config
addon_config: Dict[str, any] = load_user_config()

# Test logging
logger.info(f"Starting renogybtaddon.py - {datetime.now()}")
logger.info(addon_config["mqtt"]["port"])

# # Set logger level 
# data_logger: DataLogger = DataLogger(addon_config)

# # Hard code certain values to config
# addon_config["data"]["enable_polling"] = False
# addon_config["data"]["fields"] = ""  # Leave empty to log all fields
# addon_config["remote_logging"]["enabled"] = False
# addon_config["remote_logging"]["url"] = "https://example.com/post.php"
# addon_config["remote_logging"]["auth_header"] = "auth_header"
# addon_config["pvoutput"]["enabled"] = False
# addon_config["pvoutput"]["api_key"] = ""
# addon_config["pvoutput"]["system_id"] = ""

# # the callback func when you receive data
# def on_data_received(client, data):
#     filtered_data = Utils.filter_fields(data, addon_config['data']['fields'])
#     logging.debug("{} => {}".format(client.device.alias(), filtered_data))
#     if addon_config['remote_logging'].getboolean('enabled'):
#         data_logger.log_remote(json_data=filtered_data)
#     if addon_config['mqtt'].getboolean('enabled'):
#         data_logger.log_mqtt(json_data=filtered_data)
#     if addon_config['pvoutput'].getboolean('enabled') and addon_config['device']['type'] == 'RNG_CTRL':
#         data_logger.log_pvoutput(json_data=filtered_data)
#     if not addon_config['data'].getboolean('enable_polling'):
#         client.disconnect()

# # start client
# if addon_config['device']['type'] == 'RNG_CTRL':
#     RoverClient(addon_config, on_data_received).connect()
# elif addon_config['device']['type'] == 'RNG_CTRL_HIST':
#     RoverHistoryClient(addon_config, on_data_received).connect()
# elif addon_config['device']['type'] == 'RNG_BATT':
#     BatteryClient(addon_config, on_data_received).connect()
# elif addon_config['device']['type'] == 'RNG_INVT':
#     InverterClient(addon_config, on_data_received).connect()
# else:
#     logging.error("unknown device type")
