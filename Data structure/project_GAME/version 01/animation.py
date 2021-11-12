from os import read
from tkinter import *
import tkinter.messagebox  # กล่อง แจ้่งเตือน 
from tkinter.colorchooser import *
from tkinter.filedialog import *
from typing import Sized #เปิดไฟล์ 
import winsound #เสียง
import time
from PIL import ImageTk,Image

#--------------- display
root = Tk()
root.title("GAME Noodle practice")
root.geometry("1000x800")
# root.eval('tk::PlaceWindow . center')
root.config(bg="#E9E8C8")

#--------------- default animetion good
counter = 0
yPosition = 100
xPosition = 10
b = Label(root,bg="#E9E8C8") 
#--------------- default animetion bad
counter_bad=177


def showAnima_good():
    global counter,x

    if(counter>=120):
        counter=0

    counter +=1
    b.place(x=xPosition,y=yPosition)  # position 
    time.sleep(0.02) #delay 

    counter = str(counter) #แปลงเป็น str

    image = Image.open("pic_png//animation_png//eat-"+counter+".png");
    image = image.resize((500,500),Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)

    b["image"] = pic # กล่องรูป
    b.image = pic  # ใส่รูป

    counter = int(counter) #แปลงกลับเป็น int
    root.after(10,showAnima_good) # หลัง 0.001 seconds ให้ทำการเล่น showAnima 1 ครั้ง


def showAnima_bad():
    global counter_bad,x_bad
    
    if(int(counter_bad) >= 256):
        counter_bad=177

    
    counter_bad +=1
    b.place(x=500,y=200)  # position 
    time.sleep(0.02) #delay 

    counter_bad = str(counter_bad) #แปลงเป็น str

    image = Image.open("pic_png//animation_png//eat-"+counter_bad+".png");
    image = image.resize((500,500),Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(image)

    b["image"] = pic # กล่องรูป
    b.image = pic  # ใส่รูป

    counter_bad = int(counter_bad) #แปลงกลับเป็น int
    root.after(10,showAnima_bad) # หลัง 0.001 seconds ให้ทำการเล่น showAnima 1 ครั้ง


def playsong():
    winsound.PlaySound(None,winsound.SND_ASYNC)
def stopsong():
    winsound.PlaySound(None,winsound.SND_PURGE)

eatPic = Button(text="กิน",bg="black",fg="white",width=20,height=10,activebackground="red",command=showAnima_good).pack()
changePic = Button(text="ไม่อร่อย",bg="red",fg="white",activebackground="blue",command=showAnima_bad).pack()

# showAnima()
root.mainloop()
