import pyautogui
import altEventMapping as eventMap
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.fullscreen = False
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar
from subprocess import Popen
import configParsing as conv
from settingsjson import settings_json
from settingsjson import new_json

Builder.load_string('''
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'Welcome to AirTouch'
        font_size: 150
        on_release: app.open_settings()
''')

class Interface(BoxLayout):
    pass

class AirTouch(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        self.config.get('example', 'boolexample')
        
        return Interface()
    
    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': False,
            'numericexample': 10,
            'optionsexample1': 'None',
            'optionsexample2': 'Play/Pause',
            'optionsexample3': 'Seek',
            'optionsexample4': 'Volume Up/Down',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})
        config.setdefaults('add',{
            'app': 'None',
            'name': 'None',
            'gesture1': 'None',
            'gesture2': 'None',
            'gesture3': 'None',
            'gesture4': 'None'
        })      

    def build_settings(self, settings):
        settings.add_json_panel('AirTouch',self.config,data=settings_json)
        st = conv.getAppList()
        i = 0
        while i < len(st):
            settings.add_json_panel(st[i][0],self.config,data=new_json)
            i = i+1
        settings.add_json_panel('Add Application',self.config,data=new_json)

    
    def on_config_change(self, config, section,key, value):
        global string1
        if key == 'boolexample' and value == '1':
            print('Working Fine\n')
            Popen(['python main.py'], shell=True)
        if key == 'boolexample' and value == '0':
            print('Working fine\n')
            Popen(['pkill -9 -f main.py'], shell=True)
        if section == 'add':
            if key == 'name':
                string1 = value
                print(string1)
                print("hurrah")
            if key == 'app':
                conv.addFile(value,string1)
                print(value+" "+string1+"gogo")
                string1 = ''        
            


AirTouch().run()
