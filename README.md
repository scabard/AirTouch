# AirTouch


---
## About

AirTouch is an application software which will recognize human hand gestures from webcam and will perform media player actions like play and pause in various supported media players like VLC.

AirTouch is a gesture based application control module which maps certain gestures to various hot keys. This is achieved by using OpenCV library which has various built in functions to do image processing from video feed. OpenCV is used with python to recognize gestures and then PyAutoGUI (another popular python library) is used to create keyboard events. The application interface is created by using kivy which is a popular python based GUI library.

## Requirements
1. **Hardware**
  * Python 3.7
  * Pip 19.3.1
  * PyAutoGUI 1.0.0
  * Kivy 1.11.0
  * XLib

## Building and Running

[Clone the repository] (git clone https://github.com/scabard/AirTouch "AirTouch")

1. **Terminal**
  * Open the Terminal window. Go into the cloned folder.
  * Run `python3 App.py`

2. **Interface**
  * Start the application and open the required application.
  * Switching between the applications can be done while the program is running.
  * If user wants to change the gesture of an application, he/she has to stop the program and run again with the selected application.
  * While mapping a certain keyboard event to a gesture, the event needs to be provided in the following format:
    * (Key to be held)+(Key to be pressed) :-
    Example: If the event is pressing right arrow while Shift and Ctrl keys are held down, the command would be `shift+ctrl+right`. Refer to PyAutoGUI for more Keyboard event names.
