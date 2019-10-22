# from gi.repository import Gtk, Wnck

# Gtk.init([])  # necessary only if not using a Gtk.main() loop
# screen = Wnck.Screen.get_default()
# screen.force_update()  # recommended per Wnck documentation

# # loop all windows
# for window in screen.get_windows():
#     print(window.get_name())
#     # ... do whatever you want with this window

# # clean up Wnck (saves resources, check documentation)
# window = None
# screen = None
# Wnck.shutdown()

# import pyautogui
# import time

time.sleep(2)
pyautogui.typewrite('aknfncan ada',interval=0.1)
import gi
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk,Wnck

while True:
    if __name__ == '__main__':
        screen = Wnck.Screen.get_default()
        screen.force_update()
        while True:
            while Gtk.events_pending():
                Gtk.main_iteration()
            #time.sleep(0.5)
            x = screen.get_active_window().get_name()
            print (x)
