from tkinter import *
from os import access, close, path, read
from tkinter.colorchooser import *
import tkinter.messagebox
from typing import Counter, Sized
from tkinter.filedialog import *
import winsound
import time
from PIL import ImageTk, Image

text = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh']
word = text[0]
ip = ""
index = 0
num = 0
start_pic = True
root = Tk()
state = "idle"

class GameInput:
    
    def __init__(self, key):
        self.active_animation = True
        self.c = Label(root, bg = "#E9E8C8")
        for i in range(0, 3):
            Label(root, text = "",background="#E9E8C8").grid(row = i, column = 0)
        self.showWord()
        animation.run()

    def showWord(self):
        global word
        for n in range(0, 20):
            Label(root, text = " ", font = "30",background="#E9E8C8").grid(row = 3, column = n)
        for n in range(0, len(word)):
            Label(root, text = word[n], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = n)
        Label(root, text = '                                      ', font = "30",background="#E9E8C8").place(x = 0, y = 90)
        Label(root, text = f'Next word : {text[num + 1]}', font = "30",background="#E9E8C8").place(x = 0, y = 90)

    def onKeyPress(self, event):
        global index, ip
        if index != len(word):
            ip += event.char
            if event.char == word[index]:
                Label(root, text = word[index], font = "30", fg = "black",background="#E9E8C8").grid(row = 3, column = index)
            else:
                Label(root, text = word[index], font = "30", fg = "red",background="#E9E8C8").grid(row = 3, column = index)
            index += 1
        print(event.char)

    def pressBackSpace(self, event):
        global index, ip
        print("backspace")
        if index != 0:
            index -= 1
            ip = ip[:-1]
            Label(root, text = word[index], font = "30", fg = "grey",background="#E9E8C8").grid(row = 3, column = index)
        
    def pressEnter(self, event):
        global index, num, word, ip, start_pic, state
        Label(root, text = '                   ', font = "30",background="#E9E8C8").place(x = 0, y = 35)
        start_pic = False
        if ip == word:
            state = "good"
            print("correct")
            Label(root, text = "correct", fg = "green", font = "30",background="#E9E8C8").place(x = 0, y = 35)
            animation.run()

        else:
            state = "bad"
            print("incorrect")
            Label(root, text = "incorrect", fg = "red", font = "30",background="#E9E8C8").place(x = 0, y = 35)
            animation.run()

        ip = ""
        index = 0
        num += 1
        word = text[num]
        self.showWord()


class App(GameInput):

    def __init__(self, key):
        self.currentFrame_good = 0
        self.currentFrame_bad = 179
        self.currentFrame_default = 255

        self.break_good = 0
        self.pinPhoto = Label(root, bg = "#E9E8C8")


    def playsong(self):
        winsound.PlaySound("//Users//Pun Punyawat//OneDrive//Desktop//2D//datastr//game//song_noodle.wav",winsound.SND_ASYNC)
        

    def run(self):
        global state, start_pic
        if state == "idle":
            #print("idle work")
            self.pinPhoto.place(x = 10, y = 200)
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
            self.pinPhoto.place(x = 10, y = 200)
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
            self.pinPhoto.place(x = 10, y = 200)
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

    def countdowntime(self,count_time):
        labeltime = Label(root,text=count_time,background="#E9E8C8");
        labeltime.place(x=250,y=150);

        if(count_time > 0):
            root.after(1000,self.countdowntime,count_time-1);

        else:
            confirm = tkinter.messagebox.showerror("Game Over !","press ok to exit")
            if(confirm=="ok"):
                root.destroy()   # ani.countdowntime(15) #นับเวลา

animation = App(root)
inp = GameInput(root)

root.bind("<Return>", inp.pressEnter)
root.bind("<BackSpace>", inp.pressBackSpace)
root.bind("<KeyPress>", inp.onKeyPress)

root.title("Noodle game")
root.geometry("1000x800")

root.config(bg = "#E9E8C8")

# animation.playsong()
animation.countdowntime(15)
root.mainloop()