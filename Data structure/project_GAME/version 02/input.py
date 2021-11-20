from tkinter import *

root = Tk()
root.title("Test tkinter")

#----------Add text - label------------#
#myLabel1 = Label(root,text='Normal').pack() # pack -> add label in root (Middle)
#myLabel2 = Label(root,text='change fg',fg='red').pack() # change color of text
#myLabel3 = Label(root,text='change size',font = 20).pack() # change size
#myLabel4 = Label(root,text='change bg',bg = 'green').pack() # change bg
#----------position of widget------------#
#myLabel5 = Label(root,text='place').place(x=20,y=50) # use place
#myLabel6 = Label(root,text='grid').grid(row=0, column=0) # use grid
#myLabel7 = Label(root,text='grid2').grid(row=0,column=1)

def showMessage():
    print('You click the BUTTON')
def showLabel():
    Label(root, text='Why you click me?').pack()

#----------Add button------------#
#btn1 = Button(root,text='Button',bg = 'blue',fg = 'white').pack()
#----------Button command------------#
#btn2 = Button(root,text='Click Me !',bg = 'black',fg = 'white',command=showMessage).pack()
#btn3 = Button(root,text='Do not Click Me !',bg = 'yellow',command=showLabel).pack()

def getText():
    massage = ip.get()
    print(massage)
#----------TextBox------------#
ip = StringVar() #input from textbox
#myText = Entry(root,textvariable = ip).pack() #textbox
#btn4 = Button(root,text='Submit',command=getText).pack()

#----------TextBox------------#
#size - position of window
root.geometry("500x400+300+150") #sizexsize+posX+posY /top-left is 0,0

root.mainloop()