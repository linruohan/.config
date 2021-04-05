from tkinter import *
from tkinter import messagebox
class Application(Frame):
    """docstring for Application."""
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self,text='Hello,World')
        self.helloLabel.pack()


        self.nameInput=Entry(self)
        self.nameInput.pack()

        self.alertButton=Button(self,text='hello',command=self.hello)
        self.alertButton.pack()

        self.quitButton=Button(self,text='quit',command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'World'
        messagebox.showinfo('Message','Hello , %s !'% name)

app=Application()
app.master.title('hello')
app.mainloop()
