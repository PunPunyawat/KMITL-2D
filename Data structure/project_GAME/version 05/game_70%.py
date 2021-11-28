from tkinter import *
from os import access, close, path, read
from tkinter.colorchooser import *
import tkinter.messagebox
from typing import Counter, Sized
from tkinter.filedialog import *
import winsound
import time
import csv
from secrets import randbelow
import asyncio
from random import shuffle
import glob
from PIL import ImageTk, Image

word = ''
n = 0
ip = ''
index = 0
num = 0
start_pic = True
root = Tk()
state = "idle"

# --------------------- may
# class GameInput:
# active_animation = True
c = Label(root, bg = "#E9E8C8")
for i in range(0,3):
    Label(root,text='', bg = "#E9E8C8").grid(row= i, column = 0)
# showWord()
# animation.run()
    

def showWord():
    global word
    print(word,"^^^^^^^^ in show world")
    for count in range(0,20):
        Label(root, text=' ', font='30',bg = "#E9E8C8").grid(row = 3, column = count)
    for count in range(0,len(word)):
        Label(root,text=word[count],font = '30',fg = 'grey',bg = "#E9E8C8").grid(row = 3,column = count)
    Label(root, text='                                                                   ', font='30', bg = "#E9E8C8").place(x=0, y=90)
showWord()


def onKeyPress(event):
    global index
    global ip
    global word
    special_characters = "!@#$%^&*()-+?_=,<>/."
    #   checkisalpha            checkisspacebar     checkisnumber                checkisspecial_char
    if event.char.isalpha() or event.char == ' ' or event.char.isnumeric() or event.char in special_characters:
        if index != len(word):
            ip += event.char
            if event.char == word[index]:
                Label(root, text=word[index], font='30', fg='black', bg = "#E9E8C8").grid(row=3, column=index)
            else:
                Label(root, text=word[index], font='30', fg='red', bg = "#E9E8C8").grid(row=3, column=index)
            index += 1
        print(event.char,"input char")

def pressBackSpace(event):
    global index
    global ip
    global word
    print('backspace')
    if index != 0:
        index -= 1
        ip = ip[:-1]
        Label(root, text=word[index], font='30', fg='grey', bg = "#E9E8C8").grid(row=3, column=index)

def pressEnter(event):
    global index
    global num
    global word
    global ip
    Label(root, text='                   ',font = '30', bg = "#E9E8C8").place(x=0, y=35)
    if ip == word:
        Label(root,text='correct',fg = 'green',font = '30', bg = "#E9E8C8").place(x=0,y=35)
    else: Label(root,text='not correct',fg = 'red',font = '30', bg = "#E9E8C8").place(x=0,y=35)
    ip = ''
    index = 0
    showWorld()
    showWord()

def nothing(event):
    print('shift')


# ------------------------- tong

class MyQueue(asyncio.Queue):
    
    def __init__(self):     
        super().__init__()

    def shuffle(self):
        if self._queue is not self.empty():
            shuffle(self._queue)
        else: return None

def ConvertString(string):
    tolist=[]
    tolist[:0]=string
    return tolist

def worldSearch(inpFileName):
    csvFiles = []
    for file in glob.glob('DataWorld/AllWorld/*.csv'):
        directory = file.replace('DataWorld/AllWorld\\', '')
        directory =directory.replace('.csv', '')
        #directory = directory.strip('.csv')
        csvFiles.append(directory)
    print(csvFiles,"--------------")
    for i in range(len(csvFiles)):
        if str(csvFiles[i]) == str(inpFileName):
            return csvFiles[i]
        else :
            if i == (len(csvFiles)-1):
                return None
            else: pass


async def worldSelect(obj,fileName) :
    print(f'Name : {fileName}')
    if fileName is not None :
        with open('DataWorld/AllWorld/'+fileName+'.csv', newline='') as f:
            reader = csv.reader(f)
            temp = list(reader)
            while len(temp) != 0:
                pos = randbelow(len(temp))
                # output type
                await obj.put(temp[pos])
                #await obj.put(ConvertString(showStr(temp[pos])))
                del temp[pos]
    else:
        print("Not found")
        return -1


async def getWorld(obj):
    print("in get word **********")
    global n
    obj.shuffle()
    #print(obj.__str__())
    while not obj.empty():
        tempGet = await  obj.get()
        Label(text=tempGet[0], bg = "#E9E8C8").place(x=710, y=n+250)  # ข้อความแต่ละคำที่เอามาแสดงเฉยๆ 
        n+=20
        return tempGet


d = MyQueue()
def Input(group):
    fileName = group
    asyncio.run(worldSelect(d, worldSearch(fileName)))
    print("fisnish","!!!!!!!!!!!")


#ใส่ข้อความ
mylabel = Label(root,text = "เลือกหมวดดิอิสัส",fg = "red"  , font = 20 , bg = 'yellow'  ).place(x=690, y=0)

def showWorld():
    global word
    word = asyncio.run(getWorld(d))[0]
    print(f'Get world = {word}')

mylabel1 = Label(root,text = "เลือกหมวดกดเลือกไรมาเพื่อเริ่มเกม",fg = "blue"  , font = 20  ).place(x=625, y=30)


def Check():
    global n
    for i in range(0,250):
        Label(text="                                                   ").place(x=710, y=i+250)
        i += 19
    n = 0
    #while d.empty() is False:
    #
    ch1 = Adjective.get()
    if ch1 == 1:
        Label(text="select Adjective").place(x=710, y=n+250)
        print('run file Adjective')
        Input('Adjective')
        n+=20
    ch2 = Animal.get()
    if ch2 == 1:
        Label(text="select Animal").place(x=710, y=n+250)
        print('run file Animal')
        Input('Animal')
        n += 20
    ch3 = CarBrandName.get()
    if ch3 == 1:
        Label(text="select CarBrandName").place(x=710, y=n+250)
        print('run file CarBrandName')
        Input('CarBrandName')
        n += 20
    ch4 = CarID_Model.get()
    if ch4 == 1:
        Label(text="select CarID_Model").place(x=710, y=n+250)
        print('run file CarID_Model')
        Input('CarID_Model')
        n += 20
    ch5 = CarModel.get()
    if ch5 == 1:
        Label(text="select CarModel").place(x=710, y=n+250)
        print('run file CarModel')
        Input('CarModel')
        n += 20
    ch6 = Country.get()
    if ch6 == 1:
        Label(text="select Country").place(x=710, y=n+250)
        print('run file Country')
        Input('Country')
        n += 20
    ch7 = Fruits.get()
    if ch7 == 1:
        Label(text="select Fruits").place(x=710, y=n+250)
        print('run file Fruits')
        Input('Fruits')
        n += 20
    ch8 = Laptop.get()
    if ch8 == 1:
        Label(text="select Laptop").place(x=710, y=n+250)
        print('run file Laptop')
        Input('Laptop')
        n += 20

    Label(root, text='               ', font='30', bg = "#E9E8C8").place(x=0, y=35)
    print("in show world , word")
    showWorld()
    showWord()

# 0 ไม่เลือก 1 = เลือก
Adjective = IntVar()
Checkbutton(text = "Adjective",variable = Adjective).place(x=500, y=60)

Animal = IntVar()
Checkbutton(text = "Animal",variable = Animal).place(x=500, y=80)

CarBrandName = IntVar()
Checkbutton(text = "CarBrandName", variable = CarBrandName).place(x=500, y=100)

CarID_Model = IntVar()
Checkbutton(text = "CarID_Model",variable = CarID_Model).place(x=500, y=120)

CarModel = IntVar()
Checkbutton(text = "CarModel",variable = CarModel).place(x=500, y=140)

Country = IntVar()
Checkbutton(text = "Country",variable = Country).place(x=500, y=160)

Fruits = IntVar()
Checkbutton(text = "Fruits",variable = Fruits).place(x=500, y=180)

Laptop = IntVar()
Checkbutton(text = "Laptop",variable = Laptop).place(x=500, y=200)


Button(text="เลือกไรมา" , command = lambda:[Check(),countdowntime(15)]).place(x=500, y=220)



# class GameInput:
    
#     def __init__(self, key):
#         self.active_animation = True
#         self.c = Label(root, bg = "#E9E8C8")
#         for i in range(0, 3):
#             Label(root, text = "",background="#E9E8C8").grid(row = i, column = 0)
#         self.showWord()
#         animation.run()

#     def showWord(self):
#         global word
#         for n in range(0, 20):
#             Label(root, text = " ", font = "30",background="#E9E8C8").grid(row = 3, column = n)
#         for n in range(0, len(word)):
#             Label(root, text = word[n], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = n)
#         Label(root, text = '                                      ', font = "30",background="#E9E8C8").place(x = 0, y = 90)
#         Label(root, text = f'Next word : {text[num + 1]}', font = "30",background="#E9E8C8").place(x = 0, y = 90)

#     def onKeyPress(self, event):
#         global index, ip
#         if index != len(word):
#             ip += event.char
#             if event.char == word[index]:
#                 Label(root, text = word[index], font = "30", fg = "black",background="#E9E8C8").grid(row = 3, column = index)
#             else:
#                 Label(root, text = word[index], font = "30", fg = "red",background="#E9E8C8").grid(row = 3, column = index)
#             index += 1
#         print(event.char)

#     def pressBackSpace(self, event):
#         global index, ip
#         print("backspace")
#         if index != 0:
#             index -= 1
#             ip = ip[:-1]
#             Label(root, text = word[index], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = index)
        
#     def pressEnter(self, event):
#         global index, num, word, ip, start_pic, state
#         Label(root, text = '                   ', font = "30",background="#E9E8C8").place(x = 0, y = 35)
#         start_pic = False
#         if ip == word:
#             state = "good"
#             print("correct")
#             Label(root, text = "correct", fg = "green", font = "30",background="#E9E8C8").place(x = 0, y = 35)
#             animation.run()

#         else:
#             state = "bad"
#             print("incorrect")
#             Label(root, text = "incorrect", fg = "red", font = "30",background="#E9E8C8").place(x = 0, y = 35)
#             animation.run()

#         ip = ""
#         index = 0
#         num += 1
#         word = text[num]
#         self.showWord()

# --------------------- pun keaw
class App():

    def __init__(self, key):
        self.currentFrame_good = 0
        self.currentFrame_bad = 179
        self.currentFrame_default = 255
        self.break_good = 0
        self.pinPhoto = Label(root, bg = "#E9E8C8")
        self.run()  # เริ่มต้น

    # def playsong(self):
    #     winsound.PlaySound("//Users//Pun Punyawat//OneDrive//Desktop//2D//datastr//game//song_noodle.wav",winsound.SND_ASYNC)
        

    def run(self):
        global state, start_pic
        if state == "idle":
            #print("idle work")
            self.pinPhoto.place(x = 10, y = 400)
            time.sleep(0.02)
            self.currentFrame_default += 1
            image=Image.open("pic_png//animation_png//default//eat-"+str(self.currentFrame_default)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_default == 271:
                self.currentFrame_default = 255
                #state = "idle"
                print(state)
            if state == "idle":
                root.after(10, self.run)

        elif state == "good":
            #print("good work")
            self.pinPhoto.place(x = 10, y = 400)
            time.sleep(0.02)
            self.currentFrame_good += 1
            image=Image.open("pic_png//animation_png//good//eat-"+str(self.currentFrame_good)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_good == 40:
                self.currentFrame_good = 0
                state = "idle"
                #start_pic = True
                print(state)
                return 
            if state == "good":
                root.after(10, self.run)

        elif state == "bad":
            #print("bad work")
            self.pinPhoto.place(x = 10, y = 400)
            time.sleep(0.02)
            self.currentFrame_bad += 1
            image=Image.open("pic_png//animation_png//bad//eat-"+str(self.currentFrame_bad)+".png")
            image = image.resize((480, 400), Image.ANTIALIAS)
            picture = ImageTk.PhotoImage(image)
            self.pinPhoto["image"] = picture
            self.pinPhoto.image = picture
            if self.currentFrame_bad == 220:
                self.currentFrame_bad = 179
                state = "idle"
                #start_pic = True
                print(state)
                return
            if state == "bad":
                root.after(10, self.run)


# ---------- นับเวลา
def countdowntime(count_time):
    labeltime = Label(root,text=count_time,background="#E9E8C8").place(x=250,y=150);

    if(count_time==9):  #แก้บัค ตัวเลขซ้อน 
        Label(text="9 ",bg="#E9E8C8").place(x=250,y=150)
    
    if(count_time > 0):
        root.after(1000,countdowntime,count_time-1);

    else:
        confirm = tkinter.messagebox.showerror("Game Over !","press ok to exit")
        if(confirm=="ok"):
            root.destroy()   # ani.countdowntime(15) #นับเวลา


# ----------------------- main
animation = App(root)
# inp = GameInput(root)

root.bind("<Return>", pressEnter)
root.bind("<BackSpace>", pressBackSpace)
root.bind('<KeyPress-Shift_L>',nothing) #กดShiftแล้วมันเข้า sp char ด้วย เลยต้องดัก shift ไว้ตรงนี้
root.bind('<KeyPress-Shift_R>',nothing)
root.bind("<KeyPress>",onKeyPress)

root.title("Noodle game")
root.geometry("1000x800")

root.config(bg = "#E9E8C8")

# animation.playsong()
root.mainloop()