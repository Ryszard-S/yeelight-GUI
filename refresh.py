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
    i=0
    for bulb in bulbList:
        if bulb.get_properties().get('name') is not None:
            bn.append(bulb.get_properties().get('name'))
        else:
            bn.append(f'name{i}')
        i+=1

    return bn
