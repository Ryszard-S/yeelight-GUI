import json

from yeelight import *

try:
    with open('config.json', 'r') as file:
        x = file.read()
    y = json.loads(x)

except Exception as e:
    print(e, "\nConfig file not found!")



def bulb_list():
    bl = []
    auto_on = y.get('auto_on')
    if y.get('discover').lower() == "off":
        ips = y.get('ip_bulbs')
        for ip in ips:
            bl.append(Bulb(ip, auto_on=auto_on))

    elif y.get('discover').lower() == "on":
        for bulb in discover_bulbs(timeout=1):
            bl.append(Bulb(bulb.get('ip'), auto_on=auto_on))

    return bl


def bulb_names(bulbList):
    if bulbList == None:
        bulbList = bulb_list()
    bn = []

    for i, bulb in enumerate(bulbList):
        if bulb.get_properties().get('name') is not None:
            bn.append(bulb.get_properties().get('name'))
        else:
            bn.append(f'name{i}')

    return bn
