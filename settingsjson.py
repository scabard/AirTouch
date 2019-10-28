import json
import configParsing as conf
settings_json = json.dumps([
    {'type': 'title',
     'title': 'A settings panel for AirTouch'},
    {'type': 'bool',
     'title': 'Start the Application',
     'desc': 'Toggle the button to start/stop application',
     'section': 'example',
     'key': 'boolexample'},
    {'type': 'numeric',
     'title': 'Set sensivity of swipe',
     'desc': 'Set sensvity from 10 to 20',
     'section': 'example',
     'key': 'numericexample'},
    {'type': 'title',
     'title': 'Configure gestures for AirTouch'}, 
    {'type': 'options',
     'title': 'Two finger Up',
     'desc': 'Select action to perform',
     'section': 'example',
     'key': 'optionsexample1',
     'options': ['Play/Pause', 'Volume Up', 'Volume Down', 'None']},
    {'type': 'options',
     'title': 'Three finger Up',
     'desc': 'Select action to perform',
     'section': 'example',
     'key': 'optionsexample2',
     'options': ['Play/Pause', 'Volume Up', 'Volume Down', 'None']},
    {'type': 'options',
     'title': 'Two fingers Swipe Right/Left',
     'desc': 'Select action to perform',
     'section': 'example',
     'key': 'optionsexample3',
     'options': ['Play/Pause', 'Volume Up/Down', 'Seek', 'None']},
    {'type': 'options',
     'title': 'One finger Swipe Up/Down',
     'desc': 'Select action to perform',
     'section': 'example',
     'key': 'optionsexample4',
     'options': ['Play/Pause', 'Volume Up/Down', 'None']}])

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
    {'type': 'options',
     'title': 'Two finger Up',
     'desc': 'Select which button will be triggered',
     'section': 'add',
     'key': 'gesture1',
     'options': ['Play/Pause', 'Volume Up', 'Volume Down', 'None']},
    {'type': 'options',
     'title': 'Three finger Up',
     'desc': 'Select which button will be triggered',
     'section': 'add',
     'key': 'gesture2',
     'options': ['Play/Pause', 'Volume Up', 'Volume Down', 'None']},
    {'type': 'options',
     'title': 'Two fingers Swipe Right/Left',
     'desc': 'Select which button will be triggered',
     'section': 'add',
     'key': 'gesture3',
     'options': ['Play/Pause', 'Volume Up/Down', 'Seek', 'None']},
    {'type': 'options',
     'title': 'One finger Swipe Up/Down',
     'desc': 'Select which button will be triggered',
     'section': 'add',
     'key': 'gesture4',
     'options': ['Play/Pause', 'Volume Up/Down', 'None']}
])
