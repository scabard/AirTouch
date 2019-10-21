from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
 
Builder.load_file('gui.kv')


class Test(TabbedPanel):
    pass

class AirTouch(App):
 
    def build(self):
        return Test()
        # return Button(text="Hello Kivy!",pos=(300,350), size_hint = (.25, .18))
 
AirTouch().run()