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
from settingsjson import add_json1,add_json2
from kivy.config import ConfigParser


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
            })
        config.setdefaults('add', {
            'app': 'None',
            'name': 'None'
        })    
        config.setdefaults('vlc',{
            'app': 'None',
            'name': 'None',
            'gesture1': 'None',
            'gesture2': 'None',
            'gesture3': 'None',
            'gesture4': 'None',
            'gesture5': 'None',
            'gesture6': 'None'})
        config.setdefaults('google-chrome',{
            'app': 'None',
            'name': 'None',
            'gesture1': 'None',
            'gesture2': 'None',
            'gesture3': 'None',
            'gesture4': 'None',
            'gesture5': 'None',
            'gesture6': 'None'})    
            
            
             

    def build_settings(self, settings):
        settings.add_json_panel('AirTouch',self.config,data=settings_json)
        settings.add_json_panel('Vlc Media Player',self.config,data=add_json1)
        settings.add_json_panel('Google Chrome',self.config,data=add_json2)
        settings.add_json_panel('Add Application',self.config,data=new_json)

    
    def on_config_change(self, config, section,key, value):
        if key == 'boolexample' and value == '1':
            print('Working Fine\n')
            Popen(['python3 main.py'], shell=True)
        if key == 'boolexample' and value == '0':
            print('Working fine\n')
            Popen(['pkill -9 -f main.py'], shell=True)
               
            


AirTouch().run()
