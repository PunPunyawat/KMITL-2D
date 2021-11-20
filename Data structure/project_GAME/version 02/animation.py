from os import access, close, read
from tkinter import *
import tkinter.messagebox  # กล่อง แจ้่งเตือน 
from tkinter.colorchooser import *
from tkinter.filedialog import *
from typing import Sized #เปิดไฟล์ 
import winsound #เสียง
import time
from PIL import ImageTk,Image

class Animation:
    global counter,x,counter_bad,x_bad

    def __init__(self,key):
        self.counter = 0
        self.yPosition = 200
        self.xPosition = 10
        self.counter_bad=180
        self.stage = True
        self.b = Label(root,bg="#E9E8C8") 
        self.eatPic = Button(key,text="กิน",bg="black",fg="white",width=20,height=10,activebackground="red",command=self.checkstage_true).pack()
        self.changePic = Button(key,text="ไม่อร่อย",bg="red",fg="white",activebackground="blue",command=self.checkstage_false).pack()
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
            

        else:
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
            

#--------------- object
root = Tk()
ani=Animation(root)
# stage = True

root.title("GAME Noodle practice")
root.geometry("1000x800")
# root.eval('tk::PlaceWindow . center')
root.config(bg="#E9E8C8")

#--------------- default animetion good
# counter = 0
# yPosition = 200
# xPosition = 10
# b = Label(root,bg="#E9E8C8") 

#--------------- default animetion bad
# counter_bad=180

# ani.playsong() #เปิดเพลง

root.mainloop()
