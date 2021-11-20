from tkinter import *
from os import access, close, path, read
import tkinter.messagebox  # กล่อง แจ้่งเตือน 
from tkinter.colorchooser import *
from tkinter.filedialog import *
from typing import Counter, Sized #เปิดไฟล์ 
import winsound #เสียง
import time
from PIL import ImageTk,Image

text = ['first','second','third','forth','fifth','sixth']
word = text[0]
ip = ''
index = 0
num = 0
star_pic = True
root = Tk()


class inpgame:
    
    def __init__(self,key) :
        self.active_anime=True
        self.c = Label(root,bg="#E9E8C8")
        for i in range(0,3):
            Label(root,text='').grid(row= i, column = 0)

        self.showWord()
        ani.playstage_default() 

    def showWord(self):  #แสดง ข้อมความ
        global word
        for n in range(0,20):
            Label(root, text=' ', font='30').grid(row = 3, column = n)
        for n in range(0,len(word)):
            Label(root,text=word[n],font = '30',fg = 'grey').grid(row = 3,column = n)
            
        Label(root, text='                                      ', font='30').place(x=0, y=90)
        Label(root, text=f'next word : {text[num + 1]}', font='30').place(x=0, y=90)
    

    def onKeyPress(self,event): #กด keyboard
        global index
        global ip
        if index != len(word):
            ip += event.char
            # print(index,"+++")
            # print(ip,"----------")
            if event.char == word[index]:
                Label(root, text=word[index], font='30',fg = 'black').grid(row = 3, column= index)
            else:
                Label(root, text=word[index], font='30', fg='red').grid(row = 3, column= index)
            index += 1
        # else:
        #     print("more")    
        print(event.char)

    def pressBackSpace(self,event): #กด backspace
        global index
        global ip
        print('backspace')
        if index != 0:
            index -= 1
            ip = ip[:-1]
            Label(root, text=word[index], font='30', fg='grey').grid(row = 3, column= index)

    def pressEnter(self,event): #กด Enter
        global index
        global num
        global word
        global ip
        global star_pic 
        Label(root, text='                   ',font = '30').place(x=0, y=35)
        star_pic = False
        if ip == word:
            Label(root,text='correct',fg = 'green',font = '30').place(x=0,y=35)
            ani.playstage_good()

            # if self.active_anime==True :
            #     ani.checkstage_true()
            #     self.active_anime=False
            # else:
            #     print("false green")    

        else: 
            Label(root,text='not correct',fg = 'red',font = '30').place(x=0,y=35)
            ani.playstage_bad()
            

            # if self.active_anime==False :
            #     ani.checkstage_false()
            #     self.active_anime=True
            # else:
            #     print("false red") 

        ip = ''
        index = 0
        num += 1
        word = text[num]
        self.showWord()


class Animation(inpgame):

    def __init__(self, key):
        self.counter_good=0
        self.counter_bad=179
        self.counter_default=255

        self.break_good=0
        self.pinphoto  = Label(root,background="#E9E8C8")

    def playsong(self):  #เปิดเพลง
        winsound.PlaySound("\\Users\\Pun Punyawat\\OneDrive\\Desktop\\2D\\datastr\\game\\song_noodle.wav",winsound.SND_ASYNC)    

    def playstage_good(self): #อร่อย
        self.pinphoto.place(x=10,y=200) #position
        time.sleep(0.02)
        self.counter_good += 1
        # print(self.counter_good,end="  ")
        image=Image.open("pic_png//animation_png//eat-"+str(self.counter_good)+".png")
        image = image.resize((500,500),Image.ANTIALIAS)
        picture = ImageTk.PhotoImage(image) 
        self.pinphoto["image"] = picture  #กล่องรูป
        self.pinphoto.image = picture  # ใส่รูป
        if(self.counter_good == 40):
            self.counter_good=0
            return
        root.after(10,self.playstage_good)

    def playstage_bad(self): #ไม่อร่อย
        self.pinphoto.place(x=10,y=200) #position
        time.sleep(0.02)
        self.counter_bad += 1
        # print(self.counter_bad,end="  ")
        image=Image.open("pic_png//animation_png//eat-"+str(self.counter_bad)+".png")
        image = image.resize((500,500),Image.ANTIALIAS)
        picture = ImageTk.PhotoImage(image) 
        self.pinphoto["image"] = picture  #กล่องรูป
        self.pinphoto.image = picture  # ใส่รูป
        if(self.counter_bad == 220):
            self.counter_bad=179
            return
        root.after(10,self.playstage_bad)

    def playstage_default(self): #รอกิน
        self.pinphoto.place(x=10,y=200) #position
        time.sleep(0.002)
        self.counter_default += 1
        # print(self.counter_bad,end="  ")
        image=Image.open("pic_png//animation_png//eat-"+str(self.counter_default)+".png")
        image = image.resize((500,500),Image.ANTIALIAS)
        picture = ImageTk.PhotoImage(image) 
        self.pinphoto["image"] = picture  #กล่องรูป
        self.pinphoto.image = picture  # ใส่รูป
        if(self.counter_default == 271 and star_pic==True):
            self.counter_default=255

        root.after(10,self.playstage_default) 



"""   ไม่น่าใช้แล้ว
class Animation(inpgame):
    global counter,x,counter_bad,x_bad

    def __init__(self,key):
        self.counter = 0
        self.counter_bad=180

        self.yPosition = 200
        self.xPosition = 10

        self.stage = False
        self.b = Label(root,bg="#E9E8C8") 
        # self.eatPic = Button(key,text="กิน",bg="black",fg="white",width=20,height=10,activebackground="red",command=self.checkstage_true).pack()
        # self.changePic = Button(key,text="ไม่อร่อย",bg="red",fg="white",activebackground="blue",command=self.checkstage_false).pack()
        self.playstage()

    def playsong(self):
        winsound.PlaySound("\\Users\\Pun Punyawat\\OneDrive\\Desktop\\2D\\datastr\\game\\song_noodle.wav",winsound.SND_ASYNC)

    def checkstage_true(self):
        global stage
        self.stage = True
        self.playstage()

    def checkstage_false(self):
        global stage
        self.stage = False
        self.playstage()

    def playstage(self):
        
        if(self.stage):
            # print(self.counter)
            if(self.counter>=120):
                self.counter=0

            self.counter +=1
            self.b.place(x=self.xPosition,y=self.yPosition)  # position 
            time.sleep(0.02) #delay 

            self.counter = str(self.counter) #แปลงเป็น str

            image = Image.open("pic_png//animation_png//eat-"+self.counter+".png");
            image = image.resize((500,500),Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(image)

            self.b["image"] = pic # กล่องรูป
            self.b.image = pic  # ใส่รูป

            self.counter = int(self.counter) #แปลงกลับเป็น int
            root.after(10,self.checkstage_true) # หลัง 0.001 seconds ให้ทำการเล่น showAnima 1 ครั้ง
            
        if(False):
        # else:
            # print(self.counter_bad)
            if(self.counter_bad >= 251):
                self.counter_bad=180
            
            self.counter_bad +=1
            self.b.place(x=500,y=200)  # position 
            time.sleep(0.02) #delay 

            self.counter_bad = str(self.counter_bad) #แปลงเป็น str

            self.image = Image.open("pic_png//animation_png//eat-"+self.counter_bad+".png");
            self.image = self.image.resize((500,500),Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(self.image)

            self.b["image"] = pic # กล่องรูป
            self.b.image = pic  # ใส่รูป

            self.counter_bad = int(self.counter_bad) #แปลงกลับเป็น int
            root.after(10,self.checkstage_false) # หลัง 0.001 seconds ให้ทำการเล่น showAnima 1 ครั้ง
            
"""

#--------------- object
ani=Animation(root)
inp=inpgame(root)
# stage = True

#--------------- in put
root.bind('<Return>',inp.pressEnter)
root.bind('<BackSpace>', inp.pressBackSpace)
root.bind('<KeyPress>', inp.onKeyPress)

root.title("GAME Noodle practice")
root.geometry("1000x800")
# root.eval('tk::PlaceWindow . center')
root.config(bg="#E9E8C8")


ani.playsong() #เปิดเพลง
root.mainloop()