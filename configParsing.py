import configparser
config = configparser.ConfigParser()

def addFile(name, xlibname):
    for section in config.sections():
        config.remove_section(section)
    config.read('config/list.ini')
    if (config.has_section(xlibname)==False):
        config.add_section(xlibname)
    config.set(xlibname, 'name', name)
    config.set(xlibname, 'xlibname', xlibname)    
    with open('config/list.ini', 'w+') as configfile:
        config.write(configfile)
    
    config.read('airtouch.ini')

    items = config.items(xlibname)

    config.add_section(xlibname+'desc')

    for item in items:
        config.set(xlibname+'desc', item[0], item[1])

    config.remove_section(xlibname)

    if (config.has_section(xlibname+'gestures')==False):
        config.add_section(xlibname+'gestures')
    config.set(xlibname+'gestures', 'hold1', 'None')
    config.set(xlibname+'gestures', 'up1', 'None')
    config.set(xlibname+'gestures', 'down1', 'None')
    config.set(xlibname+'gestures', 'right1', 'None')
    config.set(xlibname+'gestures', 'left1', 'None')
    config.set(xlibname+'gestures', 'hold2', 'None')
    config.set(xlibname+'gestures', 'up2', 'None')
    config.set(xlibname+'gestures', 'down2', 'None')
    config.set(xlibname+'gestures', 'right2', 'None')
    config.set(xlibname+'gestures', 'left2', 'None')
    config.set(xlibname+'gestures', 'hold3', 'None')
    config.set(xlibname+'gestures', 'up3', 'None')
    config.set(xlibname+'gestures', 'down3', 'None')
    config.set(xlibname+'gestures', 'right3', 'None')
    config.set(xlibname+'gestures', 'left3', 'None')
    config.set(xlibname+'gestures', 'hold4', 'None')
    config.set(xlibname+'gestures', 'up4', 'None')
    config.set(xlibname+'gestures', 'down4', 'None')
    config.set(xlibname+'gestures', 'right4', 'None')
    config.set(xlibname+'gestures', 'left4', 'None')
    config.set(xlibname+'gestures', 'hold5', 'None')
    config.set(xlibname+'gestures', 'up5', 'None')
    config.set(xlibname+'gestures', 'down5', 'None')
    config.set(xlibname+'gestures', 'right5', 'None')
    config.set(xlibname+'gestures', 'left5', 'None')
    
    # config.read('config/'+xlibname+'.ini')

    # items = config.items(xlibname)

    # config.add_section('desc')

    # for item in items:
    #     config.set('desc', item[0], item[1])

    # config.remove_section(xlibname)

    # if (config.has_section('gestures')==False):
    #     config.add_section('gestures')
    # config.set('gestures', 'hold1', 'None')
    # config.set('gestures', 'up1', 'None')
    # config.set('gestures', 'down1', 'None')
    # config.set('gestures', 'right1', 'None')
    # config.set('gestures', 'left1', 'None')
    # config.set('gestures', 'hold2', 'None')
    # config.set('gestures', 'up2', 'None')
    # config.set('gestures', 'down2', 'None')
    # config.set('gestures', 'right2', 'None')
    # config.set('gestures', 'left2', 'None')
    # config.set('gestures', 'hold3', 'None')
    # config.set('gestures', 'up3', 'None')
    # config.set('gestures', 'down3', 'None')
    # config.set('gestures', 'right3', 'None')
    # config.set('gestures', 'left3', 'None')
    # config.set('gestures', 'hold4', 'None')
    # config.set('gestures', 'up4', 'None')
    # config.set('gestures', 'down4', 'None')
    # config.set('gestures', 'right4', 'None')
    # config.set('gestures', 'left4', 'None')
    # config.set('gestures', 'hold5', 'None')
    # config.set('gestures', 'up5', 'None')
    # config.set('gestures', 'down5', 'None')
    # config.set('gestures', 'right5', 'None')
    # config.set('gestures', 'left5', 'None')
    
    with open('airtouch.ini', 'w+') as configfile:
        config.write(configfile)

def getAppList():
    config.read('config/list.ini')
    list = []
    i = 0
    for section in config.sections():
        list.append([])
        list[i].append(config[section]['name'])
        list[i].append(config[section]['xlibname'])
        i=i+1
    return list

def getGestureInfo(name):
    config.read('config/'+name+'.ini')
    list = []
    i = 0
    if (config.has_section('gestures')==True):
        for name,value in config.items('gestures'):
            list.append([name,value])
    return list

def addGesture(name,gesture,event):
    config.read('config/'+name+'.ini')
    if (config.has_section('gestures')==False):
        config.add_section('gestures')
    config.set('gestures', gesture, event)
    
    with open('config/'+name+'.ini', 'w+') as configfile:
        config.write(configfile)

# print(getGestureInfo('vlc'))
# addGesture('vlc','right3','shift+right')
# getAppList()
# addFile('code', 'VS code', 'abc')