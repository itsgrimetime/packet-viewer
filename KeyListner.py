#listen to key presses, dont know how to do this concurrently.
#also dont know if it should be done that way.
import pythoncom, pyHook, time

print('program will quit on q press or after 3 seconds')

def OnKeyboardEvent(event):
    print("Key: ", chr(event.Ascii))
    if chr(event.Ascii) == 'q': exit()
    return True
    
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
while time.clock() < 3:
    pythoncom.PumpWaitingMessages()