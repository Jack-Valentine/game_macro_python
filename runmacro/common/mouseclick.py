import win32api
import win32con

class MouseClick:
    def __init__(self, x, y):
        self.position_x = int(x)
        self.position_y = int(y)
        print (self.position_x)
        print (self.position_y)

    def set_mouse_position(self, x, y):
        self.position_x = int(x)
        self.position_y = int(y)

    def mouse_click(self):
        win32api.SetCursorPos((self.position_x, self.position_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.position_x, self.position_y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.position_x, self.position_y, 0, 0)
