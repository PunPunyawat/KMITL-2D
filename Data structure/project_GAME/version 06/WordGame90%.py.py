from tkinter import *
from os import access, close, path, read
from tkinter.colorchooser import *
import tkinter.messagebox
from typing import Counter, Sized
from tkinter.filedialog import *
import winsound
import time
from PIL import ImageTk, Image
from functools import partial
#from operator import itemgetter
import pickle
from time import time
import csv
from secrets import randbelow
import asyncio
from random import shuffle
import glob
#from playsound import playsound
import winsound
showStr = lambda L: ' '.join(map(str, L))

word = ''
n = 0
ip = ''
index = 0
num = 0
start_pic = True
state = "idle"

# Python program to sort a  
# stack using auxiliary stack. 
  
# This function return the sorted stack 
def sortStack ( stack ): 
    tmpStack = createStack() 
    while(isEmpty(stack) == False): 
          
        # pop out the first element 
        tmp = top(stack) 
        pop(stack) 
  
        # while temporary stack is not 
        # empty and top of stack is 
        # greater than temp 
        while(isEmpty(tmpStack) == False and int(top(tmpStack)[1]) > int(tmp[1])): 
              
            # pop from temporary stack and 
            # push it to the input stack 
            push(stack,top(tmpStack)) 
            pop(tmpStack) 
  
        # push temp in tempory of stack 
        push(tmpStack,tmp) 
      
    return tmpStack 
  
# Below is a complete running  
# program for testing above 
# function. 
  
# Function to create a stack.  
# It initializes size of stack 
# as 0 
def createStack(): 
    stack = [] 
    return stack 
  
# Function to check if  
# the stack is empty 
def isEmpty( stack ): 
    return len(stack) == 0
  
# Function to push an  
# item to stack 
def push( stack, item ): 
    stack.append( item ) 
  
# Function to get top  
# item of stack 
def top( stack ): 
    p = len(stack) 
    return stack[p-1] 
  
# Function to pop an  
# item from stack 
def pop( stack ): 
  
    # If stack is empty 
    # then error 
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
  
    return stack.pop() 
  
# Function to print the stack 
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
    

class MyQueue(asyncio.Queue):

    def __init__(self):
        super().__init__()

    def shuffle(self):
        if self._queue is not self.empty():
         shuffle(self._queue)
        else: return None
        
deeee = MyQueue()

def ConvertString(string):
    tolist=[]
    tolist[:0]=string
    return tolist

def sc():
    global score
    print(score)
    score +=1

def validateLogin(username):
   print("username entered :", username.get())
   return
        
def showMainMenu():
    global mainmenu
    global pinPhoto1
    mainmenu = Tk()

    mainmenu.title("Game")
    mainmenu.geometry("1000x400")
    mainmenu.resizable(width=False, height=False)
    pinPhoto1 = Label(mainmenu,bg = "#E9E8C8")
    pinPhoto1.place(x = 0, y = 0)
    image=Image.open("pic/st2.png")
    picture = ImageTk.PhotoImage(image)
    pinPhoto1["image"] = picture
    pinPhoto1.image = picture
    usernameLabel = Label(mainmenu, text="User Name",fg="#FAAF30",font=('Tahoma', 15, 'bold'),bg="#FFF6F0").place(x=427, y=100)
    
    #อ่านคะแนน
    with open("score.txt") as file_in:
        for line in file_in:
            scoreRead = line.split()
            push( scoreData, scoreRead )
    prints(scoreData)
    scoreData_sorted = sortStack(scoreData)
    prints(scoreData_sorted)
    
    #เขียนลง Tk
    order_score = 10
    order = 1
    y_start = 110
    while (isEmpty(scoreData_sorted) == False) and (order_score > 0):
        score_1 = pop(scoreData_sorted)
        textScore = "No."+str(order)+". score : "+score_1[1] + " " + score_1[0][0:6]
        LabelScore_1 = Label(mainmenu, text=textScore, fg="#FFF6F0",font=('Tahoma', 13, 'bold'),bg="#FAAF30").place(x=750, y=y_start) #x = 750 y= 25+
        y_start += 25
        order_score -= 1
        order += 1
    
    sc = Label(mainmenu,text="HIGH SOCRE", fg="#FFF6F0",font=('Tahoma', 25, 'bold'),bg="#FAAF30").place(x=745, y=65)
    global username
    username = StringVar()
    usernameEntry = Entry(mainmenu, textvariable=username).place(x=547, y=110)
    global validateLogin
    validateLogin = partial(validateLogin, username)
    
   
    button_1 = Button(text="PLAY",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showSelectWorld()]).place(x=537, y=175)
    button_2 = Button(text="HOW TO",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showHowto()]).place(x=514, y=245)
    button_3 = Button(text="EXIT",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command = quitMainmenu).place(x=539, y=315)

    mainmenu.mainloop()

def play():
    winsound.PlaySound('song_noodle.wav',winsound.SND_LOOP+winsound.SND_ASYNC)

def showSelectWorld():
    global selectworld
    selectworld = Tk()
    selectworld.title('PLAY')
    selectworld.geometry('1000x400')
    selectworld.resizable(width=False, height=False)

    pinPhotomode = Label(selectworld,bg = "#E9E8C8")
    pinPhotomode.place(x = 0, y = 0)
    image=Image.open("pic/mode.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotomode["image"] = picture
    pinPhotomode.image = picture

    user = Label(selectworld,text = "   "+username.get()+"  Score :     "+str(score),fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
    global Adjective
    Adjective = IntVar()
    Checkbutton(text = "Adjective",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Adjective).place(x=100,y=120)
    global Animal
    Animal = IntVar()
    Checkbutton(text = "Animal",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Animal).place(x=320,y=120)
    global BodyParts
    BodyParts = IntVar()
    Checkbutton(text = "BodyParts",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = BodyParts).place(x=100,y=190)
    global Colors
    Colors = IntVar()
    Checkbutton(text = "Colors",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Colors).place(x=320,y=190)
    global Sport
    Sport = IntVar()
    Checkbutton(text = "Sport",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Sport).place(x=100,y=260)
    global Country
    Country = IntVar()
    Checkbutton(text = "Country",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Country).place(x=320,y=260)
    global Fruits
    Fruits = IntVar()
    Checkbutton(text = "Fruits",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Fruits).place(x=100,y=330)
    global ThaiFood
    ThaiFood = IntVar()
    Checkbutton(text = "ThaiFood",fg="#FAAF30",font=('Tahoma', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = ThaiFood).place(x=320,y=330)

    myLable5 = Button(text="PLAY",fg="#FFF6F0",font=('Tahoma', 20, 'bold'),bg="#FAAF30",activebackground='#FFF6F0',activeforeground="#FAAF30",command=lambda:[quitSelectWorld(),showGame()]).place(x=880, y=320)
    back = Button(text="BACK",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[backmain(),showMainMenu()]).place(x=750, y=320)
    selectworld.mainloop()
    
    
def showHowto():
    global howto
    howto = Tk()
    
    howto.title("HOW TO")
    howto.geometry("1000x400")
    howto.resizable(width=False, height=False)
    pinPhotohowto = Label(howto,bg = "#E9E8C8")
    pinPhotohowto.place(x = 0, y = 0)
    image=Image.open("pic/howto.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotohowto["image"] = picture
    pinPhotohowto.image = picture
 
    global myLable4
    myLable4 = Button(text="BACK",fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitHowto(),showMainMenu()]).place(x=30, y=320)
    
    howto.mainloop()
    
def showWindowMenu3():
    window3 =Tk()
    window3.title("SCORE")
    window3.geometry("1000x400")
    window3.resizable(width=False, height=False)
    window3.mainloop()
    
# ===============================================================================================


def onKeyPress(event):
    print("Key press : ",event.char)
    global index
    global ip
    global word
    special_characters = "!@#$%^&*()-+?_=,<>/."
    #   checkisalpha            checkisspacebar     checkisnumber                checkisspecial_char
    if event.char.isalpha() or event.char == ' ' or event.char.isnumeric() or event.char in special_characters:
        if index != len(word):
            ip += event.char
            if event.char == word[index]:
                Label(showgame, text=word[index], font='30', fg='Green', bg = "#FFF6F0").grid(row=3, column=index)
            else:
                Label(showgame, text=word[index], font='30', fg='red', bg = "#FFF6F0").grid(row=3, column=index)
            index += 1

def pressBackSpace(event):
    global index
    global ip
    global word
    print("Key press : BackSpace")
    if index != 0:
        index -= 1
        ip = ip[:-1]
        Label(showgame, text=word[index], font='30', fg='grey', bg = "#FFF6F0").grid(row=3, column=index)

def pressEnter(event):
    global index
    global num
    global word
    global ip
    global start_pic
    global score
    start_pic = False
    Label(showgame, text='                   ',font = '30', bg = "#FFF6F0").place(x=0, y=35)
    if ip == word:
        Label(showgame,text='correct',fg = 'green',font = '30', bg = "#FFF6F0").place(x=0,y=35)
        score +=1
        Label(showgame,text = "   "+username.get()+"  Score :     "+str(score),fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
        #animation.playstage_good()
    else: 
        Label(showgame,text='not correct',fg = 'red',font = '30', bg = "#FFF6F0").place(x=0,y=35)
        #animation.playstage_bad()
    ip = ''
    index = 0
    showWorld()


def nothing(event):
    print('shift')
        
# ===============================================================================================
        
    
def showGame():
    global showgame
    showgame = Tk()
    showgame.title("GAME")
    showgame.geometry("1000x400")
    showgame.resizable(width=False, height=False)
    showgame.focus_force()
    countdowntime(60)
    userplay = Label(showgame,text = "   "+username.get()+"  Score :     "+str(score),fg="#FAAF30",font=('Tahoma', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
   
    Check()
    
    #inp = GameInput(showgame)
    
    showgame.bind("<Return>", pressEnter)
    showgame.bind("<BackSpace>", pressBackSpace)
    showgame.bind('<KeyPress-Shift_L>',nothing) #กดShiftแล้วมันเข้า sp char ด้วย เลยต้องดัก shift ไว้ตรงนี้
    showgame.bind('<KeyPress-Shift_R>',nothing)
    showgame.bind("<KeyPress>",onKeyPress)
    showgame.config(bg = "#FFF6F0")


    for i in range(0,3):
        Label(showgame,text='',bg = "#FFF6F0").grid(row= i, column = 0)
    showWorld()    
    showgame.mainloop()
    
def Check():
    ch1 = Adjective.get()
    if ch1 == 1:
        print('World select: Adjective')
        Input('Adjective')
    ch2 = Animal.get()
    if ch2 == 1:
        print('World select: Animal')
        Input('Animal')
    ch3 = BodyParts.get()
    if ch3 == 1:
        print('World select: BodyParts')
        Input('BodyParts')
    ch4 = Colors.get()
    if ch4 == 1:
        print('World select: Colors')
        Input('Colors')
    ch5 = Sport.get()
    if ch5 == 1:
        print('World select: Sport')
        Input('Sport')
    ch6 = Country.get()
    if ch6 == 1:
        print('World select: Country')
        Input('Country')
    ch7 = Fruits.get()
    if ch7 == 1:
        print('World select: Fruits')
        Input('Fruits')
    ch8 = ThaiFood.get()
    if ch8 == 1:
        print('World select: ThaiFood')
        Input('ThaiFood')

        
def Input(group):
    print("Load World : ",group)
    fileName = group
    asyncio.run(worldSelect(deeee, worldSearch(fileName)))
    
# ===============================================================================================

async def worldSelect(obj,fileName) :
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
            
        print(f'World : {fileName} --- Finish!')
    else:
        print("Not found")
        return -1
    
def worldSearch(inpFileName):
    csvFiles = []
    for file in glob.glob('DataWorld/AllWorld/*.csv'):
        directory = file.replace('DataWorld/AllWorld\\', '')
        directory =directory.replace('.csv', '')
        csvFiles.append(directory)
    print(csvFiles)
    for i in range(len(csvFiles)):
        if str(csvFiles[i]) == str(inpFileName):
            return csvFiles[i]
        else :
            if i == (len(csvFiles)-1):
                return None
            else: pass
            
async def getWorld(obj):
    obj.shuffle()
    while not obj.empty():
        tempGet = await obj.get()
        return tempGet
    
def showWorld():
    global word
    word = asyncio.run(getWorld(deeee))[0]
    print(f'Get word = {word}')

    for count in range(0,20):
        Label(showgame, text=' ', font='30',bg = "#FFF6F0").grid(row = 3, column = count)
    for count in range(0,len(word)):
        Label(showgame,text=word[count],font = '30',fg = 'grey',bg = "#FFF6F0").grid(row = 3,column = count)
    Label(showgame, text='                                                                           ',bg = "#FFF6F0").place(x=0, y=90)
    
def countdowntime(count_time):
    t= Label(showgame,text="Time : ",fg="#FAAF30",font=('Tahoma', 20, 'bold'),background="#FFF6F0").place(x=830,y=0)
    labeltime = Label(showgame,text=count_time,fg="#FAAF30",font=('Tahoma', 20, 'bold'),background="#FFF6F0").place(x=930,y=0)
    if(count_time==9):  #แก้บัค:ตัวเลขซ้อน 
        Label(text="9   ",fg="#FAAF30",font=('Tahoma', 20, 'bold'),background="#FFF6F0").place(x=930,y=0)
    
    if(count_time > 0):
        showgame.after(1000,countdowntime,count_time-1)

    else:
        confirm = tkinter.messagebox.showerror("Game Over !","press ok to exit")
        
        #เก็บคะแนน ===================================================
        check_username  = False
        scoredatatmp = [] #เอาไว้ดึงข้อมูลใน score.txt มาเก็บไว้ใน list
        with open("score.txt") as file_in: #เช็คว่าใน score.txt มีชื่อซ้ำไหมถ้ามีให้แก้เป็นของใหม่
                for line in file_in:
                    scoreRead = line.split()
                    if scoreRead[0].lower() == username.get().lower():
                        check_username = True
                        if int(scoreRead[1]) < score:
                            scoreRead[1] = str(score)
                            scoredatatmp.append(scoreRead)
                        else:
                            scoredatatmp.append(scoreRead)
                    else:
                        scoredatatmp.append(scoreRead)
                
        if(check_username == False): #ถ้าไม่มีอยู่แล้วให้ใส่ชื่อเข้าไปใหม่
            scoredatatmp.append([username.get(), str(score)])

        with open('score.txt', 'w') as f: #เขียนข้อมูลใน list ที่เก็บ scoredatatmp ไว้ลง txt
            for item in scoredatatmp:
                f.write(item[0] + "  " + item[1]+"\n")
        # ============================================================
        
        if(confirm=="ok"):
            showgame.destroy()
            
# ===============================================================================================
    
# ออกจากหน้าแต่ละหน้า
def quitMainmenu():
        mainmenu.destroy()
def quitHowto():
        howto.destroy()
def backmain():
    selectworld.destroy()

def quitSelectWorld():
        selectworld.destroy()
def quitShowgame():
        showgame.destroy()
        
def highscore_read():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

def highscore_write():
    with open('highscores.txt', 'r') as f:
        for line in f:
            print(line.split())

# จุดเริ่มต้นโปรแกรม
if __name__ == '__main__':
    score = 0
    scoreData = createStack()
    play()
    showMainMenu()