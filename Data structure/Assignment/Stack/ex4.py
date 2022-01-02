class STACK:
    
    def __init__(self):
        self.item=[];

    def size(self):
        return len(self.item);

    def seeTree(self,inpt):

        for i in inpt:
            num = i.replace("A ","")
            if(num != "B"):
                if(self.item != []):
                    if((int(num)) < self.item[-1]):
                        self.item.append(int(num))
                    else:
                        while self.item != [] and int(num) >= self.item[-1]:
                            self.item.pop()
                        self.item.append(int(num))
                else:
                    self.item.append(int(num))
            else:
                print(self.size())        


stackz = STACK();
inputfr = input("Enter Input : ").split(",") 
stackz.seeTree(inputfr);

