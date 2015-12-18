"""
Applet User Interface
--------------------------------
                                |
              |                 |
fine keyboard |   fine packet   |
view ??       |   view          |
                                |
                                |
                                |
                                |
                                |
    packet/keypress bar         |
         slider bar             |
---------------------------------
"""



#initialzie things
import tkinter as tk
app = tk.Tk()
app.title('Packets 4 lyfe')
app.grid_columnconfigure(index=0, weight=1)
app.grid_columnconfigure(index=1, weight=1)
app.grid_columnconfigure(index=2, weight=20)


#slider bar
start = 0 
end = 100
slider = tk.Scale(app, from_=start, to=end, orient=tk.HORIZONTAL, length=1000)
slider.grid(row=3, column=0, columnspan=3)



#packet/keypress bar 
keypressbar = tk.Canvas(app, width=1000, height=30, background='white')
keypressbar.grid(row=2, column=0, columnspan=3)

def make_line_at(xcoord, color):
    #different colors for different packet types/keypresses
    keypressbar.create_line(xcoord,0,xcoord,100,fill=color,width=5)

make_line_at(10, 'red')
make_line_at(500, 'blue')



#menu bar
def closewindow():
    exit()

menubar = tk.Menu(app)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Close", command = closewindow)
menubar.add_cascade(label = "File", menu = filemenu)
app.config(menu = menubar)



#ip number entry
textbox = tk.Entry(app)
textbox.grid(column=0, row=0)



#packet info button
button = tk.Button(app, text = 'Enter info', command = closewindow)
button.grid(row=0, column=1)


#Packet selection
packetlistbox = tk.Listbox(app, width = 40)
packetlistbox.grid(column=0, row=1, columnspan=2)

for i in range(100):
    packetlistbox.insert(0,"{}.{}.{}.{}".format(i//4,i//2,i,i%3))




#Packet comparison
listbox = tk.Listbox(app, width=120)
listbox.grid(column=2, row=1, columnspan=2)

for i in range(4):
    listbox.insert(tk.END, "weiner" + str(i))
listbox.insert(tk.END, "i dont really know how to do this part yet lewl.")

if __name__ == '__main__':
    app.mainloop()