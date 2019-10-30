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