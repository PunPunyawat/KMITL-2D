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
import threading

showStr = lambda L: ' '.join(map(str, L))
word = ''
n = 0
ip = ''
index = 0
csvFiles = [] 

# ===== count accurate
count_correctword = 1
count_notcorrectword=0
count_char_correct = 0
count_char_notcorrect = 0
tempaccurate_float2f = 0 
allchar = 1
rowtext = 5

def sortStack ( stack ): 
    tmpStack = createStack() 
    while(isEmpty(stack) == False): 
        tmp = top(stack) 
        pop(stack)     
        while(isEmpty(tmpStack) == False and int(top(tmpStack)[1]) > int(tmp[1])):  
            push(stack,top(tmpStack)) 
            pop(tmpStack) 
        push(tmpStack,tmp) 
    return tmpStack 

def createStack(): 
    stack = [] 
    return stack 

def isEmpty( stack ): 
    return len(stack) == 0

def push( stack, item ): 
    stack.append( item ) 
  
def top( stack ): 
    p = len(stack) 
    return stack[p-1] 

def pop( stack ): 
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
    return stack.pop() 
  
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
    

# ======================================================

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

def finishgame():
    global endgame
    global allchar,count_char_correct,tempaccurate_float2f
    endgame = Tk()
    endgame.title("EndGame")
    endgame.iconbitmap("pic/icon_noodlenew.ico")
    endgame.geometry("1000x400")
    endgame.config(bg = "#FFF6F0")
    endgame.resizable(width=False, height=False)
    pinPhotoend = Label(endgame,bg ="#FFF6F0")
    pinPhotoend.place(x = 0, y = 0)
    image=Image.open("pic/endpic.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotoend["image"] = picture
    pinPhotoend.image = picture

    # === CALCU ACCURATE
    tempaccurate = (count_char_correct / allchar)*100
    tempaccurate_float2f = "{:.2f}".format(tempaccurate)
    print(tempaccurate_float2f,"---------")

    Homebutton=Button(text="HOME",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=gobackHome).place(x=30, y=330)
    exitbutton=Button(text="EXIT",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=quitendgame).place(x=870, y=330)
    name_end=Label(endgame,text = username.get() ,fg="#4f3645",font=('Comic Sans MS', 20, 'bold'),background="#fcc4a3").place(x=380,y=185)
    score_end=Label(endgame,text = str(score),fg="#4f3645",font=('Comic Sans MS', 20, 'bold'),background="#fcc4a3").place(x=660,y=185)
    accuratetext = Label(endgame,text = str(tempaccurate_float2f)+" %" ,fg="#4f3645",font=('Comic Sans MS', 20, 'bold'),background="#fcc4a3").place(x=520,y=289)
    endgame.mainloop()

def showMainMenu():
    global mainmenu
    global pinPhoto1
    mainmenu = Tk()
    mainmenu.title("Game")
    mainmenu.geometry("1000x400")
    mainmenu.iconbitmap("pic/icon_noodlenew.ico")
    mainmenu.resizable(width=False, height=False)
    pinPhoto1 = Label(mainmenu,bg ="#FFF6F0")
    pinPhoto1.place(x = 0, y = 0)
    image=Image.open("pic/st2.png")
    picture = ImageTk.PhotoImage(image)
    pinPhoto1["image"] = picture
    pinPhoto1.image = picture
    usernameLabel = Label(mainmenu, text="User Name",fg="#FAAF30",font=('Comic Sans MS', 15, 'bold'),bg="#FFF6F0").place(x=427, y=100)
    
    #อ่านคะแนน
    with open("score.txt") as file_in:
        for line in file_in:
            scoreRead = line.split()
            push( scoreData, scoreRead )
    print("---------- Before Sort ------------")
    prints(scoreData)
    scoreData_sorted = sortStack(scoreData)
    print("------------ Sort ------------")
    prints(scoreData_sorted)
    print("------------ muticheck ------------")
    
    #เขียนลง Tk
    order_score = 10
    order = 1
    y_start = 110
    while (isEmpty(scoreData_sorted) == False) and (order_score > 0):
        score_1 = pop(scoreData_sorted)
        textScore = "No."+str(order)+". score : "+score_1[1] + " " + score_1[0][0:6]
        LabelScore_1 = Label(mainmenu, text=textScore, fg="#FFF6F0",font=('Comic Sans MS', 13, 'bold'),bg="#FAAF30").place(x=750, y=y_start) #x = 750 y= 25+
        y_start += 25
        order_score -= 1
        order += 1
    
    sc = Label(mainmenu,text="HIGH SOCRE", fg="#FFF6F0",font=('Comic Sans MS', 25, 'bold'),bg="#FAAF30").place(x=745, y=65)
    global username
    username = StringVar()
    usernameEntry = Entry(mainmenu, textvariable=username).place(x=547, y=110)
    global validateLogin    
    validateLogin = partial(validateLogin, username)
 
    button_1 = Button(text="PLAY",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),bugname()]).place(x=537, y=175)
    button_2 = Button(text="HOW TO",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitMainmenu(),showHowto()]).place(x=514, y=245)
    button_3 = Button(text="EXIT",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command = quitMainmenu).place(x=539, y=315)

    mainmenu.mainloop()

def play():
    winsound.PlaySound('song_noodle.wav',winsound.SND_LOOP+winsound.SND_ASYNC)

def bugname():
    global username
    countchar = 0
    tempchar = []
    if username.get() == '':
        showMainMenu()
    else:
        for i in username.get():
            tempchar.append(str(i))
            countchar+=1;
        print(countchar," count ")
        showSelectWorld()

def showSelectWorld():
    global selectworld
    selectworld = Tk()
    selectworld.title('PLAY')
    selectworld.iconbitmap("pic/icon_noodlenew.ico")
    selectworld.geometry('1000x400')
    selectworld.resizable(width=False, height=False)

    pinPhotomode = Label(selectworld,bg = "#E9E8C8")
    pinPhotomode.place(x = 0, y = 0)
    image=Image.open("pic/mode.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotomode["image"] = picture
    pinPhotomode.image = picture

    user = Label(selectworld,text = "   "+username.get()+"  Score :     "+str(score),fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0").place(x=10,y=20)
    global Adjective
    Adjective = IntVar()
    Checkbutton(text = "Adjective",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Adjective).place(x=100,y=120)
    global Animal
    Animal = IntVar()
    Checkbutton(text = "Animal",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Animal).place(x=320,y=120)
    global BodyParts
    BodyParts = IntVar()
    Checkbutton(text = "BodyParts",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = BodyParts).place(x=100,y=190)
    global Colors
    Colors = IntVar()
    Checkbutton(text = "Colors",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Colors).place(x=320,y=190)
    global Sport
    Sport = IntVar()
    Checkbutton(text = "Sport",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Sport).place(x=100,y=260)
    global Country
    Country = IntVar()
    Checkbutton(text = "Country",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Country).place(x=320,y=260)
    global Fruits
    Fruits = IntVar()
    Checkbutton(text = "Fruits",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = Fruits).place(x=100,y=330)
    global ThaiFood
    ThaiFood = IntVar()
    Checkbutton(text = "ThaiFood",fg="#FAAF30",font=('Comic Sans MS', 10, 'bold'),bg="#FFF6F0",activebackground='#FFF6F0',activeforeground="red",variable = ThaiFood).place(x=320,y=330)

    myLable5 = Button(text="PLAY",fg="#FFF6F0",font=('Comic Sans MS', 20, 'bold'),bg="#FAAF30",activebackground='#FFF6F0',activeforeground="#FAAF30",command=lambda:[quitSelectWorld(),bugmode()]).place(x=880, y=320)
    
    back = Button(text="BACK",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[backmain(),showMainMenu()]).place(x=750, y=320)
    selectworld.mainloop()
    
    
def showHowto():
    global howto
    howto = Tk()
    howto.title("HOW TO")
    howto.geometry("1000x400")
    howto.iconbitmap("pic/icon_noodlenew.ico")
    howto.resizable(width=False, height=False)
    pinPhotohowto = Label(howto,bg = "#E9E8C8")
    pinPhotohowto.place(x = 0, y = 0)
    image=Image.open("pic/howto.png")
    picture = ImageTk.PhotoImage(image)
    pinPhotohowto["image"] = picture
    pinPhotohowto.image = picture
 
    global myLable4
    myLable4 = Button(text="BACK",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0",activebackground='#FAAF30',activeforeground="#FFF6F0",command=lambda:[quitHowto(),showMainMenu()]).place(x=30, y=320)
    howto.mainloop()
    
# ===============================================================================================

def onKeyPress(event):
    print("Key press : ",event.char)
    global index
    global ip
    global word
    global allchar
    global count_char_correct 
    global count_char_notcorrect 

    special_characters = "!@#$%^&*()-+?_=,<>/."
    #   checkisalpha            checkisspacebar     checkisnumber                checkisspecial_char
    if event.char.isalpha() or event.char == ' ' or event.char.isnumeric() or event.char in special_characters:
        if index != len(word):
            ip += event.char
            if event.char == word[index]:
                Label(showgame, text=word[index], font=('Comic Sans MS', 20, 'bold'), fg='Green', bg = "#FFF6F0").grid(row=rowtext, column=index+5)
                count_char_correct += 1;
                allchar+=1;
            else:
                Label(showgame, text=word[index], font=('Comic Sans MS', 20, 'bold'), fg='red', bg = "#FFF6F0").grid(row=rowtext, column=index+5)
                count_char_notcorrect +=1;
                allchar+=1;
            index += 1

def pressBackSpace(event):
    global index
    global ip
    global word
    global allchar
    allchar+=1;
    print("Key press : BackSpace")
    if index != 0:
        index -= 1
        ip = ip[:-1]
        Label(showgame, text=word[index], font=('Comic Sans MS', 20, 'bold'), fg='grey', bg = "#FFF6F0").grid(row=rowtext, column=index+5)

def pressEnter(event):
    global index
    global word
    global ip
    #global state
    global score
    global count_correctword
    global count_notcorrectword
    Label(showgame, text='                   ',font = ('Comic Sans MS', 20, 'bold'), bg = "#FFF6F0").place(x=30, y=63)
    Label(showgame, text='                                      ',font = ('Comic Sans MS', 30, 'bold'), bg = "#FFF6F0").place(x=30, y=97)

    if ip == word:
        animation.state = "good"
        Label(showgame,text='correct',fg = 'green',font = ('Comic Sans MS', 20, 'bold'), bg = "#FFF6F0").place(x=30,y=55)
        count_correctword+=1;
        score +=1
        Label(showgame,text = "   "+username.get()+"  Score :     "+str(score),fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
        run_threading = threading.Thread(target = animation.run)
        run_threading.start()
    else: 
        animation.state = "bad"
        Label(showgame,text='not correct',fg = 'red',font = ('Comic Sans MS', 20, 'bold'), bg = "#FFF6F0").place(x=30,y=55)
        count_notcorrectword+=1;
        run_threading = threading.Thread(target = animation.run)
        run_threading.start()
    ip = ''
    index = 0
    showWorld()


def nothing(event):
    print('shift')
        
# ===============================================================================================
class App:
    def __init__(self, key):
        self.currentFrame_good = 0
        self.currentFrame_bad = 179
        self.currentFrame_default = 255
        self.state = "idle"
        self.run_fun = True

        # background main play
        pinPhotomain = Label(showgame,bg ="#FFF6F0")
        self.pinPhoto = Label(showgame, bg = "#FFF6F0")
        pinPhotomain.place(x = 0, y = 0)
        image=Image.open("pic/maingame.png")
        picture = ImageTk.PhotoImage(image)
        pinPhotomain["image"] = picture
        pinPhotomain.image = picture
        self.run()

    def run(self):
        run_threading = threading.Thread(target = self.run)
        if self.state == "idle" and self.run_fun == True:
            self.pinPhoto.place(x = 250, y = 110)
            self.image = Image.open(f"pic_png/animation_png/default/eat-{self.currentFrame_default}.png")
            self.image = self.image.resize((480, 360), Image.ANTIALIAS)
            if self.run_fun == True:
                picture = ImageTk.PhotoImage(self.image)
                self.pinPhoto["image"] = picture
                self.pinPhoto.image = picture
            self.currentFrame_default += 1
            if self.state != "idle" and self.run_fun == True:
                self.currentFrame_default = 255
            if self.currentFrame_default == 271 and self.state == "idle" and self.run_fun == True:
                self.currentFrame_default = 255
            showgame.after(20, self.run)
        elif self.state == "good" and showgame != None and self.run_fun == True:
            self.pinPhoto.place(x = 250, y = 110)
            self.image = Image.open(f"pic_png/animation_png/good/eat-{self.currentFrame_good}.png")
            self.image = self.image.resize((480, 360), Image.ANTIALIAS)
            if self.run_fun == True:
                picture = ImageTk.PhotoImage(self.image)
                self.pinPhoto["image"] = picture
                self.pinPhoto.image = picture
            self.currentFrame_good += 1
            if self.state != "good" and self.run_fun == True:
                self.currentFrame_good = 0
            if self.currentFrame_good == 40 and self.state == "good" and self.run_fun == True:
                self.currentFrame_good = 0
                self.state = "idle"
                return
            showgame.after(20, self.run)
        elif self.state == "bad" and showgame != None and self.run_fun == True:
            self.pinPhoto.place(x = 250, y = 110)
            self.image = Image.open(f"pic_png/animation_png/bad/eat-{self.currentFrame_bad}.png")
            self.image = self.image.resize((480, 360), Image.ANTIALIAS)
            if self.run_fun == True: 
                picture = ImageTk.PhotoImage(self.image)
                self.pinPhoto["image"] = picture
                self.pinPhoto.image = picture
            self.currentFrame_bad += 1
            if self.state != "bad" and self.run_fun == True:
                self.currentFrame_bad = 179
            if self.currentFrame_bad == 220 and self.state == "bad" and self.run_fun == True:
                self.currentFrame_bad = 179
                self.state = "idle"
                return
            showgame.after(20, self.run)        
    
def showGame():
    global showgame
    global animation
    showgame = Tk()
    animation = App(showgame)
    animation.run_fun = True
    showgame.title("GAME")
    showgame.iconbitmap("pic/icon_noodlenew.ico")
    showgame.geometry("1000x400")
    showgame.resizable(width=False, height=False)
    showgame.focus_force()
    countdowntime(60)
    userplay = Label(showgame,text = "   "+username.get()+"  Score :     "+str(score),fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),bg="#FFF6F0").place(x=0,y=0)
    Check()

    showgame.bind("<Return>", pressEnter)
    showgame.bind("<BackSpace>", pressBackSpace)
    showgame.bind('<KeyPress-Shift_L>',nothing) #กดShiftแล้วมันเข้า sp char ด้วย เลยต้องดัก shift ไว้ตรงนี้
    showgame.bind('<KeyPress-Shift_R>',nothing)
    showgame.bind("<KeyPress>",onKeyPress)
    showgame.config(bg = "#FFF6F0")

    for i in range(0,5):
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

def bugmode():
    ch1 = Adjective.get()
    ch2 = Animal.get()
    ch3 = BodyParts.get()
    ch4 = Colors.get()
    ch5 = Sport.get()
    ch6 = Country.get()
    ch7 = Fruits.get()
    ch8 = ThaiFood.get()

    if (ch1==0 and ch2 == 0 and ch3 == 0 and ch4 == 0 and ch5 == 0 and ch6 == 0 and ch7 == 0 and ch8 == 0):
        showSelectWorld()
    else:
        showGame()

        
def Input(group):
    print("Load World : ",group)
    fileName = group
    asyncio.run(worldSelect(deeee, worldSearch(fileName)))
    csvFiles.clear()
    
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

def clearListWord(): 
    while deeee.empty() is False:    
        deeee.get_nowait() 

def worldSearch(inpFileName):
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
    global word , rowtext
    word = asyncio.run(getWorld(deeee))[0]
    print(f'Get word = {word}')

    for i in range(0,5):
        Label(showgame, text='', font=('Helvatical bold', 20),bg = "#FFF6F0").grid(row=rowtext, column=i)

    for count in range(0,20):
        Label(showgame, text=' ', font=('Comic Sans MS', 20),bg = "#FFF6F0").grid(row = rowtext, column = count+5)
    for count in range(0,len(word)):
        Label(showgame,text=word[count],font = ('Comic Sans MS', 20),fg = 'grey',bg = "#FFF6F0").grid(row = rowtext,column = count+5)
        # Label(showgame, text='                                       ',font = ('Comic Sans MS', 20),bg = "#FFF6F0").place(x=0, y=90)
    
def countdowntime(count_time):
    t= Label(showgame,text="Time : ",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),background="#FFF6F0").place(x=830,y=0)
    labeltime = Label(showgame,text=count_time,fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),background="#FFF6F0").place(x=930,y=0)
    if(count_time==9):  #แก้บัค:ตัวเลขซ้อน 
        Label(text="9   ",fg="#FAAF30",font=('Comic Sans MS', 20, 'bold'),background="#FFF6F0").place(x=930,y=0)
    
    if(count_time > 0):
        showgame.after(1000,countdowntime,count_time-1)

    else:
        #เก็บคะแนน ===================================================
        check_username  = False
        scoredatatmp = [] #เอาไว้ดึงข้อมูลใน score.txt มาเก็บไว้ใน list
        # print(type(username.get()),"-------------------------------")
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
        animation.run_fun = False
        quitShowgame()
        finishgame()
# ===============================================================================================
    
# ออกจากหน้าแต่ละหน้า
def quitMainmenu():
    mainmenu.destroy()
def quitHowto():
    howto.destroy()
def backmain():
    selectworld.destroy()
def quitendgame():
    endgame.destroy()
def quitSelectWorld():
    selectworld.destroy()
def quitShowgame():
    showgame.destroy()
def gobackHome():
    global allchar, count_char_correct, tempaccurate_float2f, score, ip, index , word
    allchar,count_char_correct,tempaccurate_float2f,score = 1, 0, 0, 0
    animation.state = "idle"
    animation.currentFrame_good = 0
    animation.currentFrame_bad = 179
    animation.currentFrame_default = 255
    word = ''
    ip = ''
    index = 0
    clearListWord()
    endgame.destroy()
    showMainMenu()
        

# จุดเริ่มต้นโปรแกรม
if __name__ == '__main__':
    score = 0
    scoreData = createStack()
    play()
    showMainMenu()