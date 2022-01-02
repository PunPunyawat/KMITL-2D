class QUEUE:

    def __init__(self):
        self.item=[]

    def enQueue(self,i):
        self.item.append(i)

    def deQueu(self):
        return self.item.pop(0)

    def isEmpty(self):
        return  self.item==[]

    def size(self):
        return len(self.item)   

    def peek(self):
        return self.item[0]

#---- obj 
q= QUEUE();
inpt = input("Enter Input : ").split(",");

for rounds in range(len(inpt)):
    if(inpt[rounds][0]=="E"):
        print("Add",inpt[rounds][2:],"index is",q.size())
        q.enQueue(inpt[rounds][2:])
    if(inpt[rounds][0]=="D"):
        if(q.isEmpty()): print("-1");
        else:
            print("Pop",q.peek(),"size in queue is",q.size()-1)
            q.deQueu()       
        
if(q.isEmpty()): print("Empty");           
else:print("Number in Queue is : ",q.item)