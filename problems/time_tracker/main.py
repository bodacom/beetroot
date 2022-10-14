# legacy code section

# import Xlib
# import Xlib.display

# for i in range(20):

#     disp = Xlib.display.Display()
#     window = disp.get_input_focus().focus

#     # Get active window class and name
#     print(window.get_wm_class())
#     print(window.get_wm_name())
#     time.sleep(1)

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

import time
import os
import re
import sys
from datetime import datetime

# getwindowfocus == getactivewindow

# 'xdotool getwindowfocus getwindowname getactivewindow getmouselocation'
xdo_command = 'xdotool getactivewindow getwindowname getmouselocation '
data = ''
file_name = 'tracker_log.txt'

# for i in range(10):
while True:

    xdo = os.popen(xdo_command).read()
    now = datetime.now().time()
    time_ = time.time()
    # print(xdo_command, xdo, now, sep='\n', end='\n\n')
    data = data + str(time_)+ '\n' + xdo + '\n'
    
    try:
        with open(file_name, 'a') as data_file:
            data_file.write(str(time_) + '\n' + xdo + '\n')
        data = ''
    except:
        print('Eror writing to file. Data will be collected in buffer and written while write operation will be available.')

    time.sleep(1)

