import configparser
config = configparser.ConfigParser()

def addFile(app, name):
    config.read('config/list.ini')
    if (config.has_section(app)==False):
        config.add_section(app)
    config.set(app, 'name', name)
    config.set(app, 'xlibname', app)
    config.set(app, 'file', app+'.ini')

    
    with open('config/list.ini', 'w+') as configfile:
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

print(getGestureInfo('vlc'))
# addGesture('vlc','right3','shift+right')
# getAppList()
# addFile('code', 'VS code', 'abc')