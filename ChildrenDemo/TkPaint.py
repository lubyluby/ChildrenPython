from tkinter import*
class Paint:
    def __init__(self):
        self.tk=Tk()
    def hello(self,str):
            print("hello world!"+str)
    def input(self,str):
        bth=Button(self.tk,text="click me",command=lambda :self.hello(str)) #没参数情况下command=self.hello
        bth.pack()
        self.tk.mainloop()
   
