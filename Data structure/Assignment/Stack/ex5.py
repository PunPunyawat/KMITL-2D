class STACK:
    
    def __init__(self):
        self.item=[];
       
    def size(self):
        return len(self.item)

    def isempty(self):
        return self.item==[]

    def push(self,i):
        self.item.append(int(i))   

    def poison(self):
        for i in range (len(self.item)):
            if self.item[i] % 2 == 0 : 
                self.item[i]-=1;
            else :  self.item[i]+=2;  


    def seeTree(self):
        temp=[]

        if (self.size() == 1):
            print("1")   
        else : 
            for i in range(len(self.item)):
                if(temp != []):

                    if(temp!=[] and (temp[-1] > self.item[i])) :
                        temp.append(self.item[i])

                    else:    
                        while(temp!=[] and (self.item[i] >= temp[-1])):
                            temp.pop()

                        temp.append(self.item[i])    
                
                else:
                    temp.append(self.item[i])
                
            print(len(temp))


stack=STACK();
inpt = input("Enter Input : ").split(",")    

for i in range(len(inpt)):
    if inpt[i][0] == "B" :
        stack.seeTree()
    elif inpt[i][0] == "S":
        stack.poison();
    else:
        if(inpt[i][0]=="A"):
            stack.push(inpt[i][2:]);    



