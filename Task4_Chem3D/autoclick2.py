'''
pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
'''

from PIL import ImageGrab
import win32api,win32con
import time
import win32clipboard
import os
time0 = time.time()

def GetPixel(x,y):
    im = ImageGrab.grab()
    pix = im.load()
    return(pix[x, y])

def LeftClickWithSleep(x,y,t=0.3):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(t)

def RightClickWithSleep(x,y,t=0.3):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(t)

def CopyKeyWithSleep():
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(67, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)

def FailSafe():
    if GetPixel(5,5) == (51,53,57):
        return False
    return True

def GetClipBoard():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()
    return text

time.sleep(3)
while time.time() < time0 + 24000 and FailSafe() and GetPixel(72,6) == (121,23,97):

    LeftClickWithSleep(105,60,1)
    LeftClickWithSleep(860,425,1)
    LeftClickWithSleep(860,425,1)
    CopyKeyWithSleep()
    filename = GetClipBoard()
    filename = filename.decode()
    print(filename)
    LeftClickWithSleep(1220,690)
    LeftClickWithSleep(1220, 690)

    if not FailSafe():
        break

    LeftClickWithSleep(285,35)
    LeftClickWithSleep(285,180)
    LeftClickWithSleep(765,387)
    LeftClickWithSleep(765,403)
    LeftClickWithSleep(765,420)
    LeftClickWithSleep(765,437)
    LeftClickWithSleep(765,454)
    LeftClickWithSleep(1090,710)

    time.sleep(3)

    # input('waiting-----')

    RightClickWithSleep(144,1000)
    LeftClickWithSleep(240,955)
    RightClickWithSleep(144, 1000)
    LeftClickWithSleep(240,885)
    RightClickWithSleep(144, 1000)
    LeftClickWithSleep(240, 930)
    output = GetClipBoard()
    output = output.decode()
    # print(output)

    # input('waiting-----')

    if not FailSafe():
        break

    # time.sleep(2)
    RightClickWithSleep(190,110)
    LeftClickWithSleep(230,165)
    # input('waiting-----')

    os.remove('..\\data\\temp\\trial\\'+filename+'.gjf')
    output_file = open('..\\data\\temp\\trial\\'+filename+'.txt','a')
    #print(output,file=output_file,end='')
    output_file.writelines(output)
    output_file.close()

print('FailSafe triggered!!!')

while False:
    while (GetPixel(144,1007) != (0,0,0) and GetPixel(146,1007) != (0,0,0)) and not FailSafe():
        time.sleep(0.5)
        print('a')
    time.sleep(0.2)
    while (GetPixel(144,1007) != (0,0,0) and GetPixel(146,1006) != (0,0,0)) and not FailSafe():
        time.sleep(0.5)
        print('b')
