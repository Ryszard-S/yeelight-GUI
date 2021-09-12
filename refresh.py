import json

from yeelight import *

from tkinter import messagebox

try:
    with open('config.json', 'r') as file:
        x = file.read()
    y = json.loads(x)

except Exception as e:
    print(e, "\nConfig file not found!")
    messagebox.showinfo("!", "Check your config file")


def bulb_list():
    bl = []
    auto_on = y.get('auto_on')
    if y.get('discover').lower() == "off":
        ips = y.get('ip_bulbs')
        for ip in ips:
            bl.append(Bulb(ip, auto_on=auto_on))

    elif y.get('discover').lower() == "on":
        try:
            for bulb in discover_bulbs(timeout=1):
                bl.append(Bulb(bulb.get('ip'), auto_on=auto_on))
        except OSError as e:
            messagebox.showinfo(" ", "Check your internet connection")

    return bl


def bulb_names(bulbList):
    if bulbList == None:
        bulbList = bulb_list()
    bn = []

    for i, bulb in enumerate(bulbList):
        try:
            if bulb.get_properties().get('name') is not None:
                bn.append(bulb.get_properties().get('name'))
            else:
                bn.append(f'name{i}')
        except BulbException as e:
            messagebox.showinfo("timed out", "A socket error occurred when sending the command. \n"
                                             "Check you connection or IP addresses in config.json")

    return bn
