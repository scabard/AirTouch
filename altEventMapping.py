# import pyautogui
# import time

# time.sleep(2)
# pyautogui.typewrite('aknfncan ada',interval=0.1)
# import gi
# gi.require_version('Wnck', '3.0')
# from gi.repository import Gtk,Wnck

# while True:
#     if __name__ == '__main__':
#         screen = Wnck.Screen.get_default()
#         screen.force_update()
#         while True:
#             while Gtk.events_pending():
#                 Gtk.main_iteration()
#             #time.sleep(0.5)
#             x = screen.get_active_window().get_name()
            # print (x)
import Xlib
import Xlib.display
import time

# run = True
# while run:
#     try:
#         time.sleep(5)

#         display = Xlib.display.Display()
#         root = display.screen().root
#         windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
#         window = display.create_resource_object('window', windowID)

#         print (window.get_wm_name())
#         print (window.get_full_property(display.intern_atom('_NET_WM_PID'), Xlib.X.AnyPropertyType).value[0])
#         print (window.get_full_property(display.intern_atom('_NET_WM_NAME'), Xlib.X.AnyPropertyType).value[0])
#         print (window.get_full_property(display.intern_atom('_NET_WM_VISIBLE_NAME'), Xlib.X.AnyPropertyType))
#         print (window.get_wm_class())
            
#     except KeyboardInterrupt:
#         run = False
def retActiveWin():
    display = Xlib.display.Display()
    root = display.screen().root
    windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
    window = display.create_resource_object('window', windowID)
    actWin = window.get_wm_class()

    return actWin[0]