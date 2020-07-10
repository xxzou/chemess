

'''
pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
'''

from PIL import ImageGrab
import win32api,win32con
import time
import win32clipboard
import os,shutil
time0 = time.time()

root_path = '..\\\data\\temp\\ROUND3_TOFREQ_v3\\'
gjf_namelist = [item for item in os.listdir(root_path) if item.endswith('.gjf')]
print(gjf_namelist)

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

def PasteKeyWithSleep():
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.5)

def DeleteAllKeyWithSleep():
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(65, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(0x8, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(0x8, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.3)

def FailSafe():
    if GetPixel(5,5) == (51,53,57):
        return False
    return True

def GetClipBoard():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()
    return text

def SetClipBoard(aString):
    "写入剪贴板"
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    win32clipboard.CloseClipboard()


start_num = 101
end_num = 199
print('start num: '+str(start_num)+'; end num: '+ str(end_num))
input('!!!WARNING, CONFIRM START AND END NUM!!!')
time.sleep(3)
while time.time() < time0 + 24000 and FailSafe() and GetPixel(450,550) == (218,236,255) and start_num <= end_num:
    LeftClickWithSleep(767,384)
    DeleteAllKeyWithSleep()
    SetClipBoard(gjf_namelist[start_num])
    start_num += 1
    PasteKeyWithSleep()
    LeftClickWithSleep(916,484)
    while GetPixel(943,527) != (255,255,255) and FailSafe():
        time.sleep(0.5)
    while GetPixel(943,527) != (255,255,255) and FailSafe():
        time.sleep(0.1)
    LeftClickWithSleep(999,616)
    time.sleep(0.5)

while False:
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
    LeftClickWithSleep(285,180,0.5)
    LeftClickWithSleep(765,387)
    LeftClickWithSleep(765,403)
    LeftClickWithSleep(765,420)
    LeftClickWithSleep(765,437)
    LeftClickWithSleep(765,454)
    LeftClickWithSleep(1090,710)

    while GetPixel(144,1006) != (0,0,0) and FailSafe():
        time.sleep(0.5)
    while GetPixel(144,1006) != (0,0,0) and FailSafe():
        time.sleep(0.1)

    RightClickWithSleep(144,1006)
    LeftClickWithSleep(240,965)
    RightClickWithSleep(144, 1006)
    LeftClickWithSleep(240,890)
    RightClickWithSleep(144, 1006)
    LeftClickWithSleep(240, 935)
    output = GetClipBoard()
    output = output.decode()
    # print(output)

    if not FailSafe():
        break

    # time.sleep(2)
    RightClickWithSleep(190,110)
    LeftClickWithSleep(230,165)
    # input('waiting-----')

    os.remove('..\\data\\temp\\trial\\'+filename+'.mol2')
    output_file = open('..\\data\\temp\\trial\\'+filename+'.txt','a')
    #print(output,file=output_file,end='')
    output_file.writelines(output)
    output_file.close()


print('FailSafe triggered!!!')


