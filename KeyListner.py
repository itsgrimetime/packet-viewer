import pythoncom, pyHook
import time
from datetime import datetime
import sys

def OnKeyboardEvent(event):
    print("key",chr(event.Ascii), "up" if event.IsTransition() else "down", event.Time)
    return True
    
def OnMouseEvent(event):
    if event.MessageName != 'mouse move':
        print(event.MessageName, event.Time)
    return True
    
def listen(sec=5):
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.KeyUp = OnKeyboardEvent
    hm.MouseAll = OnMouseEvent
    hm.HookMouse()
    hm.HookKeyboard()

    date = datetime.strftime(datetime.now(), 'Keypresses %b%d %H.%M%p')

    with open('{}.txt'.format(date), 'w+') as f:
        sys.stdout = f
        while time.clock() < sec:
            pythoncom.PumpWaitingMessages()
            
    hm.UnhookMouse()
    hm.UnhookKeyboard()

if __name__ == '__main__':
    listen()