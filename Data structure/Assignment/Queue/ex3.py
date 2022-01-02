class Queue:
    def __init__(self) :
        self.inbox=[];
    def size(self):
        return len(self.inbox);
    def isEmpty(self):
        return self.inbox==[];
    def peekfornt(self):
        return self.inbox[0]        

    def enQueue(self,i):
        self.inbox.append(i);
    def defornt(self):
        return self.inbox.pop(0)
        
que = Queue();
inpt = input("Enter Input : ").split("/");
tempSbook = inpt[0]; tempNtock = inpt[1]
stockbook=[];  newstock=[]

# copy list and change
for i in tempNtock : newstock = tempNtock.split(",")
for i in tempSbook: stockbook = tempSbook.split()
    
# print(stockbook," ----OLD st")
# print(newstock," ---NEW st")

for i in stockbook : que.enQueue(i);
# print(que.inbox,"stock now")
for i in range(len(newstock)):
    if(newstock[i][0]=="E"):
        que.enQueue(newstock[i][2:]);
    if(newstock[i][0]=="D" and (not que.isEmpty())):
        que.defornt()    


if len(que.inbox) == len(set(que.inbox)):
    print("NO Duplicate") 
else:
    print("Duplicate")

