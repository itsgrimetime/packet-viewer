import binascii
import tkinter as tk
from tkinter import filedialog
from viewer.PacketTimeline import PacketTimeline


class applet:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title('Packets 4 lyfe')
        self.packet_timeline = None
        self.input_timeline = None
        self.start_time = 0
        self.end_time = 0


        #slider bars, top and bot. Each call onScroll when moved.
        self.sliderbot = tk.Scale(self.app, from_=0, to=0, orient=tk.HORIZONTAL, command=self.onScroll)
        self.sliderbot.pack(side=tk.BOTTOM, fill=tk.X)
        self.slidertop = tk.Scale(self.app, from_=0, to=0, orient=tk.HORIZONTAL, command=self.onScroll)
        self.slidertop.pack(side=tk.BOTTOM, fill=tk.X)


        #packet/keypress bar
        self.keypressbar = tk.Canvas(self.app, width=1000, height=30, background='white')
        self.keypressbar.pack(side=tk.BOTTOM, fill=tk.X)


        #menu bar
        ##exit
        closewindow = lambda: exit()
        menubar = tk.Menu(self.app)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label="Close", command=closewindow)
        menubar.add_cascade(label="File", menu=filemenu)
        self.app.config(menu=menubar)
        ##open pcap
        filemenu.add_command(label = "Open PCap File", command = self.load_pcap_from_file)


        # #Packet list
        self.text = tk.Text(self.app)
        self.text.pack(fill=tk.BOTH, expand=1)


        #Start and End time text boxes
        frame = tk.Frame()
        self.startlabel = tk.Label(frame, text=str(self.start_time))
        self.startlabel.pack(side=tk.LEFT, fill=tk.NONE)
        self.endlabel = tk.Label(frame, text=str(self.end_time))
        self.endlabel.pack(side=tk.RIGHT, fill=tk.NONE)
        frame.pack(side=tk.BOTTOM, fill=tk.X)


        #update dynamically
        #This needs to be run once before main loop
        #self.update()
        #this isnt necessary right now, things are called atm when a file is selected
        # or the scroll bar is scrolled


        #this is called when the window is resized.
        self.app.bind('<Configure>', self.draw)


    def load_pcap_from_file(self):
        filename = filedialog.askopenfilename()
        print("got file {}".format(filename))
        self.packet_timeline = PacketTimeline(filename)
        self.draw()

    def draw(self, *args):
        #Update global start and stop times
        if self.input_timeline and self.packet_timeline:
            self.start_time = min(self.packet_timeline.start_time, self.input_timeline.start_time)
            self.end_time = max(self.packet_timeline.end_time, self.input_timeline.end_time)
        elif self.packet_timeline:
            self.start_time = self.packet_timeline.start_time
            self.end_time = self.packet_timeline.end_time
        elif self.input_timeline:
            self.start_time = self.input_timeline.start_time
            self.end_time = self.input_timeline.end_time

        span = self.end_time - self.start_time

        #update labels and slider
        self.startlabel.configure(text=self.start_time)
        self.endlabel.configure(text=self.end_time)
        self.sliderbot.configure(from_=self.start_time, to=self.end_time)
        self.slidertop.configure(from_=self.start_time, to=self.end_time)

        #clear current packet info
        self.keypressbar.delete('all')

        #make lines to show where inputs occur
        #problem when multiple things occur in same milisecond? idk if this matters but the
        #pcap testfile has alot like that
        #needs to be redrawn when the window is resized but idk if thats important

        if self.input_timeline:
            for input in self.input_timeline:
                xcoord = (input.timestamp - self.start_time) * self.keypressbar.winfo_width() / span
                self.make_line_at(xcoord, text_to_write=input.text, color='blue')

        if self.packet_timeline:
            for packet in self.packet_timeline:
                xcoord = (packet.timestamp - self.start_time) * self.keypressbar.winfo_width() / span
                self.make_line_at(xcoord, text_to_write='p', color='red')

    def get_current_packets_hex(self, coord):
        if self.packet_timeline is None:
            return ""

        output = ''
        for packet in self.packet_timeline.packets_at(coord):
            output += binascii.hexlify(packet.raw()).decode('utf-8')
            output += '\n\n\n'
        spaced_output = ""
        count = 0
        # theres def a better way to do this
        for c in output:
            if count is 2:
                spaced_output += " "
                count = 0
            else:
                spaced_output += c
                count += 1
        return spaced_output


    #Example of how to update dynamically
    def update(self):
        self.make_line_at(self.the_int, 'red')
        self.app.after(1000, self.update) #time in ms, func to run
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.INSERT, self.get_current_packets_hex())
        # Example of coloring the text box
        self.text.tag_add("here", "1.0", "1.4")
        self.text.tag_add("start", "1.8", "1.13")
        self.text.tag_config("here", background="yellow", foreground="blue")
        self.text.tag_config("start", background="black", foreground="green")

    def onScroll(self, scroll_value):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.INSERT, self.get_current_packets_hex(int(scroll_value)))

    def make_line_at(self, xcoord, text_to_write='None', color='green'):
        #different colors for different packet types/keypresses
        self.keypressbar.create_line(xcoord,15,xcoord,35,fill=color,width=1)
        self.keypressbar.create_text((xcoord, 5), text=text_to_write)

    def __call__(self):
        return self.app.mainloop()

if __name__ == '__main__':
    a = applet()
    a()