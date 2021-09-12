# Yeelight-GUI
## About
Control Xiaomi smart lights from your computer.

## Requirements
1. Python 3.9
2. Yeelight library

### **How to install library ?**
Use the python package manager.
### Windows:

```
pip install yeelight 
```

### Mac os: 

```
pip3 install yeelight
```

### Linux:
1. Install pip for linux: 

    ```
    sudo apt-get install python3-pip
    ```
2. Install tkinter for python:
    ```
    sudo apt-get install python3-tk
    ```
3. Using the pip install yeelight package
    ```
    pip3 install yeelight
    ```

## Configuration file
```json
{"discover": "on",
"ip_bulbs":[
  "182.161.3.1",
  "182.161.3.1"
],
  "auto_on": "True"
}
```



| Setting    | Options     | Description |
| ---- | :----: | ---- |
|*discover*  |   on        |Discover lights over ssdp protocol every time you launch application. (default setting)|
|            |  off        |If you want fixed ip numbers of your lights. You can configure static address ip of lights in your router, and write it in "ip_bulbs" section.|
|*ip_bulbs*| |Write here bulb's ip address.|
|*auto_on*|True|Turn on bulb before running a command.|
| |False|Before running command you have to turn on bulb.|


## Run app
Copy files to user directory, create desktop shortcut from python "main.pyw" script.
You can change the icon of the shortcut by right-clicking on it -> properties -> change icon. Select the "icon.ico" file from the directory and click ok.

Lights are not detected: 

1. Check if LAN control is enabled. 
    * https://www.yeelight.com/faqs/lan_control

2. After relaunch app list of lights is empty.
    * Try to configure static ip, and add ip addresses to config file.


## Credits
* [python yeelight library](https://gitlab.com/stavros/python-yeelight)
* [Open Moji](https://openmoji.org/)


Enjoy :partying_face: !

