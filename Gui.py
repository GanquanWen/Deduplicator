from tkinter import *
from tkinter import messagebox
import time
#import tkMessageBox
def start(rangeValue):
    for i in range(rangeValue+1):  
        time.sleep(0.01)  
        app.change_schedule(i,rangeValue)
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='Welcom to our Locker system!')
        self.helloLabel.grid(row = 0,column = 0)
        self.fileLabel = Label(self, text='Please enter the File name')
        self.fileLabel.grid(row = 1,column = 0)
        self.nameInput = Entry(self)
        self.nameInput.grid(row = 2,column = 0)
        self.lockerLabel = Label(self, text='Please enter the Locker name')
        self.lockerLabel.grid(row = 3,column = 0)
        self.lockerInput = Entry(self)
        self.lockerInput.grid(row = 4,column = 0)
        self.insertButton = Button(self, text='Insert', command=self.insert)
        self.insertButton.grid(row = 5,column = 0)
        self.deleteButton = Button(self, text='Delete', command=self.delete)
        self.deleteButton.grid(row = 6,column = 0)
        self.retrieveButton = Button(self, text='Retrieve', command=self.retrieve)
        self.retrieveButton.grid(row = 7,column = 0)
        self.quitbutton = Button(self, text="QUIT", fg="red", command=self.quit)
        self.quitbutton.grid(row = 8,column = 0)
        self.canvas = Canvas(self,width = 120,height = 30,bg = "white")
        self.canvas.grid(row = 10,column = 0)
    def change_schedule(self,now_schedule,all_schedule):
        x=StringVar()
        self.canvasLabel = Label(self,textvariable = x)
        self.canvasLabel.grid(row = 10,column = 1)
        out_rec=self.canvas.create_rectangle(5,5,105,25,outline = "blue",width = 1)
        fill_rec=self.canvas.create_rectangle(5,5,5,25,outline = "",width = 0,fill = "blue")
        self.update()
        self.canvas.coords(fill_rec, (5, 5, 6 + (now_schedule/all_schedule)*100, 25))   
        x.set(str(round(now_schedule/all_schedule*100,2)) + '%')  
        if round(now_schedule/all_schedule*100,2) == 100.00:
            x.set("Finish")
    def delete(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please Enter the File Name")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please Enter the Locker Name")
        if locker !=self.lockerInput.get():
            return 0
        start(99)
        messagebox.showinfo('Message', 'Delete file '+ name +' from locker '+ locker)
    def insert(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please Enter the File Name")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please Enter the Locker Name")
        if locker !=self.lockerInput.get():
            return 0
        start(99)
        messagebox.showinfo('Message', 'Insert file '+ name + ' to locker '+ locker)
    def retrieve(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please Enter the File Name")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please Enter the Locker Name")
        if locker !=self.lockerInput.get():
            return 0
        start(99)
        messagebox.showinfo('Message','Retrieve file ' + name+ ' from locker '+ locker)
app = Application()
app.master.title('Hello World')
app.master.maxsize(1000,1000)
app.master.minsize(500,300)
app.mainloop()

'''
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")
'''