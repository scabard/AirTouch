import json
import configParsing as conf
import array as arr

titles = [
    'AirTouch',
    'Add Application'
]

configs = [ 'none', 'none']

settings_all = [
    json.dumps([
        {'type': 'title',
        'title': 'A settings panel for AirTouch'},
        {'type': 'bool',
        'title': 'Start the Application',
        'desc': 'Toggle the button to start/stop application',
        'section': 'example',
        'key': 'boolexample'},
        {
            'type': 'title',
            'title': 'Please Restart the Application after config change'
        }
    ]),json.dumps([
        {
        'type': 'title',
        'title': 'Add your new application here'
        },
        {
            'type': 'string',
            'title': 'Name of your application',
            'section': 'add',
            'key': 'name'
        },
        {
            'type': 'string',
            'title': 'Xlib name of your application',
            'section': 'add',
            'key': 'app'
        },
        {
            "type": "buttons",
            "title": "",
            "desc": "",
            "section": "$var(InterfaceConfigSection)",
            "key": "configchangebuttons",
            "buttons":[{"title":"Add","id":"button_add"}]},
        {
            'type': 'title',
            'title': 'Restart to use the new application'
        }
    ])]

def loadJSON():
    apps = conf.getAppList()
    for appInf in apps:
        titles.append(appInf[0])
        configs.append('config/'+appInf[1]+'.ini')
        addJSON = json.dumps([
            {
                'type': 'title',
                'title': 'Configure your application here'
            },
            {
                'type': 'string',
                'title': 'Name of your application',
                'section': appInf[1]+'desc',
                'key': 'name'
            },
            {
                'type': 'string',
                'title': 'Xlib Name of your application',
                'section': appInf[1]+'desc',
                'key': 'xlibname'
            },
            {
                'type': 'string',
                'title': 'One Finger Hold',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'hold1',
            },
            {
                'type': 'string',
                'title': 'One Finger Swipe Up',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'up1',
            },
            {
                'type': 'string',
                'title': 'One Finger Swipe Down',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'down1',
            },
            {
                'type': 'string',
                'title': 'One Finger Swipe Right',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'right1',
            },
            {
                'type': 'string',
                'title': 'One Finger Swipe Left',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'left1',
            },
            {
                'type': 'string',
                'title': 'Two Fingers Hold',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'hold2',
            },
            {
                'type': 'string',
                'title': 'Two Fingers Swipe Up',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'up2',
            },
            {
                'type': 'string',
                'title': 'Two Fingers Swipe Down',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'down2',
            },
            {
                'type': 'string',
                'title': 'Two Fingers Swipe Right',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'right2',
            },
            {
                'type': 'string',
                'title': 'Two Fingers Swipe Left',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'left2',
            },
            {
                'type': 'string',
                'title': 'Three Fingers Hold',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'hold3',
            },
            {
                'type': 'string',
                'title': 'Three Fingers Swipe Up',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'up3',
            },
            {
                'type': 'string',
                'title': 'Three Fingers Swipe Down',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'down3',
            },
            {
                'type': 'string',
                'title': 'Three Fingers Swipe Right',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'right3',
            },
            {
                'type': 'string',
                'title': 'Three Fingers Swipe Left',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'left3',
            },
            {
                'type': 'string',
                'title': 'Four Fingers Hold',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'hold4',
            },
            {
                'type': 'string',
                'title': 'Four Fingers Swipe Up',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'up4',
            },
            {
                'type': 'string',
                'title': 'Four Fingers Swipe Down',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'down4',
            },
            {
                'type': 'string',
                'title': 'Four Fingers Swipe Right',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'right4',
            },
            {
                'type': 'string',
                'title': 'Four Fingers Swipe Left',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'left4',
            },
            {
                'type': 'string',
                'title': 'Five Fingers Hold',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'hold5',
            },
            {
                'type': 'string',
                'title': 'Five Fingers Swipe Up',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'up5',
            },
            {
                'type': 'string',
                'title': 'Five Fingers Swipe Down',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'down5',
            },
            {
                'type': 'string',
                'title': 'Five Fingers Swipe Right',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'right5',
            },
            {
                'type': 'string',
                'title': 'Five Fingers Swipe Left',
                'desc': 'Which button will be triggered',
                'section': appInf[1]+'gestures',
                'key': 'left5',
            }
        ])
        settings_all.append(addJSON)
    return titles,configs,settings_all

# def loadJSON():
#     apps = conf.getAppList()
#     for appInf in apps:
#         titles.append(appInf[0])
#         configs.append('config/'+appInf[1]+'.ini')
#         addJSON = json.dumps([
#             {
#                 'type': 'title',
#                 'title': 'Configure your application here'
#             },
#             {
#                 'type': 'string',
#                 'title': 'Name of your application',
#                 'section': 'desc',
#                 'key': 'name'
#             },
#             {
#                 'type': 'string',
#                 'title': 'Xlib Name of your application',
#                 'section': 'desc',
#                 'key': 'xlibname'
#             },
#             {
#                 'type': 'string',
#                 'title': 'One Finger Hold',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'hold1',
#             },
#             {
#                 'type': 'string',
#                 'title': 'One Finger Swipe Up',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'up1',
#             },
#             {
#                 'type': 'string',
#                 'title': 'One Finger Swipe Down',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'down1',
#             },
#             {
#                 'type': 'string',
#                 'title': 'One Finger Swipe Right',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'right1',
#             },
#             {
#                 'type': 'string',
#                 'title': 'One Finger Swipe Left',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'left1',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Two Fingers Hold',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'hold2',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Two Fingers Swipe Up',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'up2',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Two Fingers Swipe Down',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'down2',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Two Fingers Swipe Right',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'right2',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Two Fingers Swipe Left',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'left2',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Three Fingers Hold',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'hold3',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Three Fingers Swipe Up',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'up3',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Three Fingers Swipe Down',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'down3',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Three Fingers Swipe Right',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'right3',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Three Fingers Swipe Left',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'left3',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Four Fingers Hold',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'hold4',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Four Fingers Swipe Up',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'up4',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Four Fingers Swipe Down',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'down4',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Four Fingers Swipe Right',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'right4',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Four Fingers Swipe Left',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'left4',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Five Fingers Hold',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'hold5',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Five Fingers Swipe Up',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'up5',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Five Fingers Swipe Down',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'down5',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Five Fingers Swipe Right',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'right5',
#             },
#             {
#                 'type': 'string',
#                 'title': 'Five Fingers Swipe Left',
#                 'desc': 'Which button will be triggered',
#                 'section': 'gestures',
#                 'key': 'left5',
#             }
#         ])
#         settings_all.append(addJSON)
#     return titles,configs,settings_all

# settings_json = json.dumps([
#     {'type': 'title',
#      'title': 'A settings panel for AirTouch'},
#     {'type': 'bool',
#      'title': 'Start the Application',
#      'desc': 'Toggle the button to start/stop application',
#      'section': 'example',
#      'key': 'boolexample'},
#     {
#         'type': 'title',
#         'title': 'Please Restart the Application after config change'
#     }
#     ])

# new_json = json.dumps([
#     {
#         'type': 'title',
#         'title': 'Add your new application here'
#     },
#     {
#         'type': 'string',
#         'title': 'Name of your application',
#         'section': 'add',
#         'key': 'name'
#     },
#     {
#         'type': 'string',
#         'title': 'Xlib name of your application',
#         'section': 'add',
#         'key': 'app'
#     },
#     {
#         'type': 'title',
#         'title': 'Restart to use the new application'
#     }
# ])

# add_json1 = json.dumps([
#     {
#         'type': 'title',
#         'title': 'Configure your application here'
#     },
#     {
#         'type': 'string',
#         'title': 'Name of your application',
#         'section': 'vlc',
#         'key': 'app'
#     },
#     {
#         'type': 'string',
#         'title': 'Xlib Name of your application',
#         'section': 'vlc',
#         'key': 'name'
#     },
#     {'type': 'string',
#      'title': 'Four finger Up',
#      'desc': 'Which button will be triggered',
#      'section': 'vlc',
#      'key': 'gesture1',
#     }, 
#     {'type': 'string',
#      'title': 'Three finger Up',
#      'desc': 'Which button will be triggered',
#      'section': 'vlc',
#      'key': 'gesture2',
#     },
#     {'type': 'string',
#      'title': 'Two fingers Swipe Right',
#      'desc': 'Which button will be triggered',
#      'section': 'vlc',
#      'key': 'gesture3',
#     },
#     {'type': 'string',
#      'title': 'Two fingers Swipe Left',
#      'desc': 'Which button will be triggered',
#      'section': 'vlc',
#      'key': 'gesture4',
#     },
#     {'type': 'string',
#      'title': 'One finger Swipe Up',
#      'desc': 'Which button will be triggered',
#      'section': 'vlc',
#      'key': 'gesture5',
#     },
#     {'type': 'string',
#      'title': 'One finger Swipe Down',
#      'desc': 'Which button will be triggered',
#      'section': 'vlc',
#      'key': 'gesture6',
#     }
#     ])    

# add_json2 = json.dumps([
#     {
#         'type': 'title',
#         'title': 'Configure your application here'
#     },
#     {
#         'type': 'string',
#         'title': 'Name of your application',
#         'section': 'google-chrome',
#         'key': 'app'
#     },
#     {
#         'type': 'string',
#         'title': 'Xlib Name of your application',
#         'section': 'google-chrome',
#         'key': 'name'
#     },
#     {'type': 'string',
#      'title': 'Four finger Up',
#      'desc': 'Which button will be triggered',
#      'section': 'google-chrome',
#      'key': 'gesture1',
#     }, 
#     {'type': 'string',
#      'title': 'Three finger Up',
#      'desc': 'Which button will be triggered',
#      'section': 'google-chrome',
#      'key': 'gesture2',
#     },
#     {'type': 'string',
#      'title': 'Two fingers Swipe Right',
#      'desc': 'Which button will be triggered',
#      'section': 'google-chrome',
#      'key': 'gesture3',
#     },
#     {'type': 'string',
#      'title': 'Two fingers Swipe Left',
#      'desc': 'Which button will be triggered',
#      'section': 'google-chrome',
#      'key': 'gesture4',
#     },
#     {'type': 'string',
#      'title': 'One finger Swipe Up',
#      'desc': 'Which button will be triggered',
#      'section': 'google-chrome',
#      'key': 'gesture5',
#     },
#     {'type': 'string',
#      'title': 'One finger Swipe Down',
#      'desc': 'Which button will be triggered',
#      'section': 'google-chrome',
#      'key': 'gesture6',
#     }
#     ])     
