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
from settingsjson import loadJSON
# from settingsjson import settings_all
# from settingsjson import titles
# from settingsjson import configs
# from settingsjson import settings_json
# from settingsjson import new_json
# from settingsjson import add_json1,add_json2
from kivy.config import ConfigParser
from kivy.uix.settings      import SettingItem
from kivy.uix.button import Button
import configparser
configP = configparser.ConfigParser()


class SettingButtons(SettingItem):

    def __init__(self, **kwargs):
        self.register_event_type('on_release')
        # For Python3 compatibility we need to drop the buttons keyword when calling super.
        kw = kwargs.copy()
        kw.pop('buttons', None)
        super(SettingItem, self).__init__(**kw)
        for aButton in kwargs["buttons"]:
            oButton=Button(text=aButton['title'], font_size= '15sp')
            oButton.ID=aButton['id']
            self.add_widget(oButton)
            oButton.bind (on_release=self.On_ButtonPressed)
    def set_value(self, section, key, value):
        # set_value normally reads the configparser values and runs on an error
        # to do nothing here
        return
    def On_ButtonPressed(self,instance):
        # self.panel.settings.dispatch('on_config_change',self.panel.config, self.section, self.key, instance.ID)
        # print(self.panel.config['add']['name'])
        conv.addFile(self.panel.config['add']['name'],self.panel.config['add']['app'])

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
            
            
             

    def build_settings(self, settings):
        titles,configs,settings_all = loadJSON()
        # print(titles)
        # print(configs)
        # print(len(settings_all))
        settings.register_type('buttons', SettingButtons)

        for i in range(len(settings_all)):
            # if(configs[i] == 'none'):
            settings.add_json_panel(titles[i],self.config,data=settings_all[i])
            # else:
            #     self.config.read(configs[i])
            #     settings.add_json_panel(titles[i],self.config,data=settings_all[i])
            #     self.config = ConfigParser()
            #     self.config.read('airtouch.ini')
        # settings.add_json_panel('AirTouch',self.config,data=settings_json)
        # settings.add_json_panel('Vlc Media Player',self.config,data=add_json1)
        # settings.add_json_panel('Google Chrome',self.config,data=add_json2)
        # settings.add_json_panel('Add Application',self.config,data=new_json)
        # settings.add_panel(panel,'Add Application',1)
    
    def on_config_change(self, config, section,key, value):
        if key == 'boolexample' and value == '1':
            print('Working Fine\n')
            Popen(['python3 main.py'], shell=True)
        if key == 'boolexample' and value == '0':
            print('Working fine\n')
            Popen(['pkill -9 -f main.py'], shell=True)

AirTouch().run()
