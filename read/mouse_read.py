import sys
import time
import win32api
import win32con

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)


    if a != state_left:  # Button state changed
        state_left = a
        x, y = win32api.GetCursorPos()
        if a < 0:
            print(str(x) + ', ' + str(y))
        '''
        else:
            print('Left Button Released')
        '''
    '''
    if b != state_right:  # Button state changed
        state_right = b
        print(b)
        if b < 0:
            print('Right Button Pressed')
        else:
            print('Right Button Released')
    '''
    time.sleep(0.001)
    '''
    #print (win32con.MOUSEEVENTF_LEFTDOWN)
    #print (win32api.GetAsyncKeyState(win32api.win32con.MOUSEEVENTF_LEFTDOWN))
    x, y = win32api.GetCursorPos()
    print ('MX : ' + str(x) + '\tMY: ' + str(y))
    time.sleep(2)
    '''