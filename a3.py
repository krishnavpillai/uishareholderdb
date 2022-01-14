from tkinter import *

class Dialog(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.list = Listbox(self, selectmode=EXTENDED)
        self.list.pack(fill=BOTH, expand=1)
        self.current = None
        self.poll() # start polling the list

    def poll(self):
        now = self.list.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.after(250, self.poll)

    def list_has_changed(self, selection):
        print ("selection is", selection)

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()
d.mainloop()