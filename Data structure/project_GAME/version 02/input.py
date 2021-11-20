from tkinter import *

text = ['first','second','third','forth','fifth','sixth']
word = text[0]
ip = ''
index = 0
num = 0

root = Tk()
root.geometry('300x200+300+150')

for i in range(0,3):
    Label(root,text='').grid(row= i, column = 0)


def showWord():
    global word
    for n in range(0,20):
        Label(root, text=' ', font='30').grid(row = 3, column = n)
    for n in range(0,len(word)):
        Label(root,text=word[n],font = '30',fg = 'grey').grid(row = 3,column = n)
        
    Label(root, text='                                      ', font='30').place(x=0, y=90)
    Label(root, text=f'next word : {text[num + 1]}', font='30').place(x=0, y=90)
showWord()

def onKeyPress(event):
    global index
    global ip
    if index != len(word):
        ip += event.char
        # print(index,"+++")
        # print(ip,"----------")
        if event.char == word[index]:
            Label(root, text=word[index], font='30',fg = 'black').grid(row = 3, column = index)
        else:
            Label(root, text=word[index], font='30', fg='red').grid(row = 3, column= index)
        index += 1
    # else:
    #     print("more")    
    print(event.char)

def pressBackSpace(event):
    global index
    global ip
    print('backspace')
    if index != 0:
        index -= 1
        ip = ip[:-1]
        Label(root, text=word[index], font='30', fg='grey').grid(row=3, column=index)

def pressEnter(event):
    global index
    global num
    global word
    global ip
    Label(root, text='                   ',font = '30').place(x=0, y=35)
    if ip == word:
        Label(root,text='correct',fg = 'green',font = '30').place(x=0,y=35)
    else: Label(root,text='not correct',fg = 'red',font = '30').place(x=0,y=35)
    ip = ''
    index = 0
    num += 1
    word = text[num]
    showWord()

root.bind('<Return>',pressEnter)
root.bind('<BackSpace>', pressBackSpace)
root.bind('<KeyPress>', onKeyPress)
root.mainloop()