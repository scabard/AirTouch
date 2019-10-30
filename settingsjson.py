import json
import configParsing as conf
import array as arr
settings_json = json.dumps([
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
    ])

new_json = json.dumps([
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
        'type': 'title',
        'title': 'Restart to use the new application'
    }
])

add_json1 = json.dumps([
    {
        'type': 'title',
        'title': 'Configure your application here'
    },
    {
        'type': 'string',
        'title': 'Name of your application',
        'section': 'vlc',
        'key': 'app'
    },
    {
        'type': 'string',
        'title': 'Xlib Name of your application',
        'section': 'vlc',
        'key': 'name'
    },
    {'type': 'string',
     'title': 'Four finger Up',
     'desc': 'Which button will be triggered',
     'section': 'vlc',
     'key': 'gesture1',
    }, 
    {'type': 'string',
     'title': 'Three finger Up',
     'desc': 'Which button will be triggered',
     'section': 'vlc',
     'key': 'gesture2',
    },
    {'type': 'string',
     'title': 'Two fingers Swipe Right',
     'desc': 'Which button will be triggered',
     'section': 'vlc',
     'key': 'gesture3',
    },
    {'type': 'string',
     'title': 'Two fingers Swipe Left',
     'desc': 'Which button will be triggered',
     'section': 'vlc',
     'key': 'gesture4',
    },
    {'type': 'string',
     'title': 'One finger Swipe Up',
     'desc': 'Which button will be triggered',
     'section': 'vlc',
     'key': 'gesture5',
    },
    {'type': 'string',
     'title': 'One finger Swipe Down',
     'desc': 'Which button will be triggered',
     'section': 'vlc',
     'key': 'gesture6',
    }
    ])    

add_json2 = json.dumps([
    {
        'type': 'title',
        'title': 'Configure your application here'
    },
    {
        'type': 'string',
        'title': 'Name of your application',
        'section': 'google-chrome',
        'key': 'app'
    },
    {
        'type': 'string',
        'title': 'Xlib Name of your application',
        'section': 'google-chrome',
        'key': 'name'
    },
    {'type': 'string',
     'title': 'Four finger Up',
     'desc': 'Which button will be triggered',
     'section': 'google-chrome',
     'key': 'gesture1',
    }, 
    {'type': 'string',
     'title': 'Three finger Up',
     'desc': 'Which button will be triggered',
     'section': 'google-chrome',
     'key': 'gesture2',
    },
    {'type': 'string',
     'title': 'Two fingers Swipe Right',
     'desc': 'Which button will be triggered',
     'section': 'google-chrome',
     'key': 'gesture3',
    },
    {'type': 'string',
     'title': 'Two fingers Swipe Left',
     'desc': 'Which button will be triggered',
     'section': 'google-chrome',
     'key': 'gesture4',
    },
    {'type': 'string',
     'title': 'One finger Swipe Up',
     'desc': 'Which button will be triggered',
     'section': 'google-chrome',
     'key': 'gesture5',
    },
    {'type': 'string',
     'title': 'One finger Swipe Down',
     'desc': 'Which button will be triggered',
     'section': 'google-chrome',
     'key': 'gesture6',
    }
    ])     


