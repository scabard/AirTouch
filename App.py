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

from settingsjson import settings_json

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

    def build_settings(self, settings):
        settings.add_json_panel('AirTouch',
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section,
                         key, value):
        if key == 'boolexample' and value == '1':
            print('Working Fine\n')
            Popen(['python main.py'], shell=True)
        if key == 'boolexample' and value == '0':
            print('Working fine\n')
            Popen(['pkill -9 -f main.py'], shell=True)
            


AirTouch().run()
