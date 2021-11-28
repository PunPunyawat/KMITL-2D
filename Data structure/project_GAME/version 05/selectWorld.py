import csv
from secrets import randbelow
import asyncio
from random import shuffle
import glob
showStr = lambda L: ' '.join(map(str, L))

word = ''
n = 0

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
        Label(text=tempGet[0]).place(x=710, y=n+250)  # ข้อความแต่ละคำที่เอามาแสดงเฉยๆ 
        n+=20
        return tempGet




#----------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
d = MyQueue()
def Input(group):
    fileName = group
    asyncio.run(worldSelect(d, worldSearch(fileName)))
    print("fisnish","!!!!!!!!!!!")
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------

from tkinter import  *
root = Tk() #หน้าจอ
root.title("World")

# myMenu = Menu()
# root.config(menu =myMenu)

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

    Label(root, text='               ', font='30').place(x=0, y=35)
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


Button(text="เลือกไรมา" , command = Check).place(x=500, y=220)
#กำหนดหน้าต่างหน้าจอ "500x500+x+y"
#menusmall = Menu(menusmall,tearoff=0);
#กล่องข้อความ
root.geometry("1000x500+200+0")

#-----------------------------------------------------------------------------------------------#
ip = ''
index = 0
num = 0
for i in range(0,3):
    Label(root,text='').grid(row= i, column = 0)

def showWord():
    global word
    print(word,"^^^^^^^^ in show world")
    for count in range(0,20):
        Label(root, text=' ', font='30').grid(row = 3, column = count)
    for count in range(0,len(word)):
        Label(root,text=word[count],font = '30',fg = 'grey').grid(row = 3,column = count)
    Label(root, text='                                                                   ', font='30').place(x=0, y=90)
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
                Label(root, text=word[index], font='30', fg='black').grid(row=3, column=index)
            else:
                Label(root, text=word[index], font='30', fg='red').grid(row=3, column=index)
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
    showWorld()
    showWord()

def nothing(event):
    print('shift')

root.bind('<Return>',pressEnter)
root.bind('<BackSpace>', pressBackSpace)
root.bind('<KeyPress-Shift_L>', nothing) #กดShiftแล้วมันเข้า sp char ด้วย เลยต้องดัก shift ไว้ตรงนี้
root.bind('<KeyPress-Shift_R>', nothing)
root.bind('<KeyPress>', onKeyPress)
root.mainloop()