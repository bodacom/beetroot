# import Xlib
# import Xlib.display
import time

# for i in range(20):

#     disp = Xlib.display.Display()
#     window = disp.get_input_focus().focus

#     # Get active window class and name
#     print(window.get_wm_class())
#     print(window.get_wm_name())
#     time.sleep(1)

import os, re, sys
# from subprocess import PIPE, Popen

# def get_active_window_title():

#     root = Popen( ['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout = PIPE )
#     stdout, stderr = root.communicate()

#     m = re.search( b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout )

#     if m is not None:
#         window_id = m.group( 1 )
#         window = Popen( ['xprop', '-id', window_id, 'WM_NAME'], stdout = PIPE )
#         stdout, stderr = window.communicate()

#         match = re.match( b'WM_NAME\(\w+\) = (?P<name>.+)$', stdout )
#         if match is not None:
#             return match.group( 'name' ).decode( 'UTF-8' ).strip( '"' )

#     return 'Active window not found'

# if __name__ == '__main__':
#     print( get_active_window_title() )

for i in range(120):

    xdo_window_id = os.popen('xdotool getwindowfocus getwindowname getactivewindow getmouselocation').read()
    print('xdo_window_name:', xdo_window_id)
    time.sleep(1)
