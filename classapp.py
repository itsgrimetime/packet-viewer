#example:
#from classapp import a
#a()

import tkinter as tk
from tkinter import filedialog
from viewer.PacketTimeline import PacketTimeline


class applet:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title('Packets 4 lyfe')  
        self.the_int = 0
        
        
        #slider bar
        self.start = 0 
        self.end = 1000
        
        def callback(x):
            self.the_int = x
        
        slider = tk.Scale(self.app, from_=self.start, to=self.end, orient=tk.HORIZONTAL, length=1000, command = lambda x: callback(slider.get()))
        slider.pack(side=tk.BOTTOM, fill=tk.X)
                
                
        #packet/keypress bar    
        self.keypressbar = tk.Canvas(self.app, width=1000, height=30, background='white')
        self.keypressbar.pack(side=tk.BOTTOM, fill=tk.X)


        #menu bar
        ##exit
        closewindow = lambda: exit()
        menubar = tk.Menu(self.app)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Close", command = closewindow)
        menubar.add_cascade(label = "File", menu = filemenu)
        self.app.config(menu = menubar)
        ##open pcap
        filemenu.add_command(label = "Open PCap File", command = self.load_pcap_from_file)


        #Packet list
        self.listbox = tk.Listbox(self.app, height=30)
        self.listbox.pack(fill=tk.BOTH, expand=1, pady=(0,20))
        self.listbox.insert(tk.END, "i dont really know how to do this part yet lewl.")


        #update dynamically
        #This needs to be run once before main loop
        self.update() 
        
        
        #Start and End time text boxes        
        self.startlabel = tk.Label(self.app, text=str(self.start))
        self.startlabel.pack(side=tk.LEFT)
        self.endlabel = tk.Label(self.app, text=str(self.end))
        self.endlabel.pack(side=tk.RIGHT)
                #Key pressed at textboxes
                
        
    def load_pcap_from_file(filename):
        filename = filedialog.askopenfilename()
        print("got file {}".format(filename))
        packets = PacketTimeline(filename)

        
    #Example of how to update dynamically
    def update(self):
        self.make_line_at(self.the_int, 'red')
        self.app.after(1000, self.update) #time in ms, func to run
    
    def make_line_at(self, xcoord, text='None', color='green'):
        #different colors for different packet types/keypresses
        self.keypressbar.create_line(xcoord,15,xcoord,35,fill=color,width=1)
        self.keypressbar.create_text((xcoord, 5), text='a')
        
    def __call__(self):
        return self.app.mainloop()

if __name__ == '__main__':
    a = applet()
    a.make_line_at(30)
    a()