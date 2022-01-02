
class QUEUE:
    def __init__(self):
        self.normal =[];
        self.itmirror=[];

    def size(self):
        return len(self.normal);
    def isEmpty(self):
        return self.normal==[];
    def peekfornt(self):
        return self.normal[0]        

    def enQueue(self,i):
        self.inbox.append(i);
    def defornt(self):
        return self.inbox.pop(0)  

    def invertWord(self,i):
        return i[::-1]
#---------------------------------------------
# stack
    def pushMir(self,i):
        self.itmirror.append(i);
    def popMir(self):
        return self.itmirror.pop()    
 
qe=QUEUE(); countMir=0; countNor=0; Boom=0; BoomNor=0;
stackM=[]; stackN=[]; toQueue=[];
failbooM=0;  canbooM=0;
Nor,Mirr = input("Enter Input (Normal, Mirror) : ").split()  
print("NORMAL :")      
temp=""
Mirr="".join(reversed(Mirr))
for i in Mirr:
    if(stackM==[]):
        stackM.append(i);
        temp=i
        countMir+=1;
    else:
        stackM.append(i);
        if(temp==i):
            countMir+=1;
        else:
            temp=i
            countMir=1;
        if(countMir==3):
            stackM.pop()
            stackM.pop()
            toQueue.append(stackM.pop())  # stack ค่าที่จะใช้ต่อส่งไป normal
            Boom+=1;
            countMir=0;
            if(stackM!=[] and len(stackM)>1):
                if(stackM[-1]==stackM[-2]):
                    countMir=2;
                    temp=stackM[-1]
                else: countMir=1; temp=stackM[-1];
            if(len(stackM)==1): countMir=1; temp=stackM[-1];        
            
# print(toQueue, " before tranfer")
for i in Nor:
    if(stackN==[]):
        stackN.append(i)
        countNor+=1;
        temp=i;
    else:
        stackN.append(i);
        if(temp==i):
            countNor+=1;
        else:
            temp=i;
            countNor=1;

        if(countNor==3 ):
            countNor=0;
            if(toQueue!=[]):
                tempMiror=toQueue.pop(0);   
                if(i==tempMiror):     
                    stackN.pop()
                    stackN.pop()
                    stackN.pop()
                    stackN.append(tempMiror);
                    failbooM+=1;
                else:
                    stackN.pop()
                    stackN.append(tempMiror)
                    stackN.append(i)
                     
            else:  # เอาออกหมด กรณี ใส่ mirrror ครบ
                stackN.pop()
                stackN.pop()
                stackN.pop()
                canbooM+=1;

            if(stackN!=[] and len(stackN)>1):
                if(stackN[-1]==stackN[-2]):
                    countNor=2;
                    temp=stackN[-1];
                else:
                    temp=stackN[-1];
                    countNor=1;
            if(len(stackN)==1): countNor=1; temp=stackN[-1];                    

# print(toQueue,"pop")
# print(failbooM,"fail")
# print(canbooM,"canbooM")
# print(stackN,"  ----- final")

if(len(stackN)>=1 ):
    print(len(stackN)); print("".join(reversed(stackN)));
else:
    print(len(stackN)); print("Empty"); 
print(canbooM,"Explosive(s) ! ! ! (NORMAL)")
if(failbooM>0):
    print("Failed Interrupted",failbooM,"Bomb(s)");
print("------------MIRROR------------")
print(": RORRIM"); 
if(len(stackM)>=1):
    print(len(stackM)); print("".join(reversed(stackM))); print("(RORRIM) ! ! ! (s)evisolpxE",Boom);
else:
    print(len(stackM)); print("ytpmE"); print("(RORRIM) ! ! ! (s)evisolpxE",Boom); 
