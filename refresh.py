from yeelight import *


def bulb_list():
    bl = []
    for bulb in discover_bulbs():
        bl.append(Bulb(bulb.get('ip')))

    return bl


def bulb_names(bulbList):
    if bulbList == None:
        bulbList = bulb_list()
    bn = []
    for bulb in bulbList:
        bn.append(bulb.get_properties().get('name'))

    return bn
