import sys
import time
import win32api
import win32con

def MouseClick(x, y) :
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def KeyboardClick(vk) :
    vk = int(vk)
    win32api.keybd_event(vk, 0)

def Delay(sec) :
    msec = float(sec) / 1000
    time.sleep(msec)

def main(lines, globalDelay, loop) :
    while loop > 1 or loop == -1 :
        for line in lines:
            line = line.split(' ')
            if(line[0].startswith('m')) :
                # Mouse Event
                MouseClick(line[1], line[2])
            elif(line[0].startswith('k')) :
                # Keyboard Event
                KeyboardClick(line[1])
            elif (line[0].startswith('d')) :
                # Delay Event
                Delay(line[1])
            Delay(globalDelay)
            if loop != -1 : loop -= 1

if(len(sys.argv) == 2) :
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    f.close()
    main(lines, 0, 1)
elif(len(sys.argv) == 4) :
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    f.close()
    gd = int(sys.argv[2])
    loop = int(sys.argv[3])
    # set mouse offset
    main(lines, gd, loop)
else :
    print("must run with macro file")