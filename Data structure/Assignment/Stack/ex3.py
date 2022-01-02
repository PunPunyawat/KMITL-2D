class Stack:
        
    def __init__(self):
        self.item=[]
        self.outsring=[]

    def push(self,i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def sizef(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []
    
    def peek(self):
        return self.item[-1]  

    def pushout(self,i):
        self.outsring.append(i)


symbol = set(["(",")","+","-","*","/","^"])
priori = {'+':1, '-':1, '*':2, '/':2, '^':3} 
S = Stack(); 

inp = input('Enter Infix : ')

for cha in inp:
    if(cha not in symbol):
        S.outsring +=cha
        # print(S.outsring," in ")
        # S.pushout(cha)
    
    elif cha=="(":
        S.push(cha)
        # print(S.item,"  (  ")  

    elif cha==")":
        # print(S.item,"  (  before") 
        while  S.peek() != "(" :
            # print(S.item,"--------- before")
            S.pushout(S.pop());
            # print(S.item,"--------- After")              
        S.pop()
         
    else:    
        # print(S.isEmpty())
        # print(not S.isEmpty(),"----")
        while not S.isEmpty() and S.peek()!= "(" and priori[cha] <= priori[S.peek()]:
            S.pushout(S.pop())
        S.push(cha)    
        
while not S.isEmpty():
    S.outsring.append(S.pop())
    # print(S.outsring," final ")  
       
print("Postfix :", "".join(S.outsring));