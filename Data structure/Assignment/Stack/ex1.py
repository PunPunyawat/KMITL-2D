class STACK:

    def __init__(self) :
        self.newlist=[];
        self.rod=0;

    def pop_stack(self): 
        if(len(self.newlist)==0):
            print("-1")
        else : 
            self.rod-=1;
            print("Pop = "+str(self.newlist[self.rod][-2:])+" and Index = "+str(len(self.newlist)-1))
            self.newlist.pop()
            
    def push(self,inp):
        return self.newlist.append(inp)
        

    def outp(self):
            print("Add = "+str(self.newlist[self.rod][-2:])+" and Size = "+str(len(self.newlist)))
            self.rod+=1; 

    def showall(self):
        if(len(self.newlist)==0):
            print("Value in Stack = Empty");
        else:
            print("Value in Stack =" , " ".join(self.newlist));     
 
# input
ipt1 = input("Enter Input : ").split(",");

#----- obj
stac = STACK()

#----- do
for i in range(len(ipt1)):
    if(ipt1[i][0]=="A"):
        temp = ipt1[i][-2:]
        stac.push(temp);
        stac.outp();
        
        
    elif(ipt1[i][0] == "P"):
        stac.pop_stack();
        
stac.showall()
       