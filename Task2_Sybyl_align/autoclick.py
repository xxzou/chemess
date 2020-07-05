'''
pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
'''

from PIL import ImageGrab
import win32api,win32con
import time
time0 = time.time()

def LeftClick(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

time.sleep(3)
while time.time() < time0 + 20:
    LeftClick(610,550)
    time.sleep(0.3)