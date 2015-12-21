#listen to key presses, dont know how to do this concurrently.
#also dont know if it should be done that way.
import pythoncom, pyHook, time

def OnKeyboardEvent(event):
    print("Key: ", chr(event.Ascii) + str(event.IsTransition()))
    if chr(event.Ascii) == 'q': exit()
    return True
    
def OnMouseEvent(event):
    if event.MessageName != 'mouse move':
        print(event.MessageName)
    return True
    

    
def listen(sec=5):
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.KeyUp = OnKeyboardEvent
    hm.MouseAll = OnMouseEvent
    hm.HookMouse()
    hm.HookKeyboard()
    
    with open('{}.txt'.format(time.clock(), 'w+') as f):
        while time.clock() > sec:
            pythoncom.PumpWaitingMessages()
            
    hm.UnhookMouse()
    hm.UnhookKeyboard()

