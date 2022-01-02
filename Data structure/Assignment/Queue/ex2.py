class QUEUE:
    def __init__(self):
        self.item1=[];
        self.item2=[];
        self.mainq=[];
        
    def demain(self):
        return self.mainq.pop(0);
    def deQueueitem1(self):
        return self.item1.pop(0) 
    def deQueueitem2(self):
        return self.item2.pop(0)    

    def enQueueitem1(self,i):
        self.item1.append(i);
    def enQueueitem2(self,i):
        self.item2.append(i);

    def isEmpty(self):
        return self.item1==[];
    def peek(self):
        return self.item1[0];
    def size(self):
        return len(self.item1);

inpt = input("Enter people : ")   
q=QUEUE();
num=1
# [main][item1][item2]

for i in inpt:
    q.mainq.append(i)
   

for p in inpt:
    if(q.mainq!=[]):
        # print(num,"++++++++++++")
        q.demain()
        if(q.item1!=[] and num%3==1):
            # print(" pop i tem1")
            q.deQueueitem1()
            q.enQueueitem1(p)

            if(len(q.item1)==5):
                # print("in")
                if(q.item2 !=[] and num% 3==1 and num%2==0):
                    # print(num,"---------")
                    # print("in2")
                    q.deQueueitem2()
                    # print("pop here")
                    
        else:
            if(len(q.item1)==5):
                # print("out")
                
                if(q.item2 !=[] and num% 2==0):
                    # print("out 2")
                    q.deQueueitem2()

                q.enQueueitem2(p)
                       
            else:
                q.enQueueitem1(p)

    else:
        # กันไว้
        q.mainq.append()  
    
    print(num,q.mainq,q.item1,q.item2)         
    num+=1


           
           
            





"""


class QUEUE:
    def __init__(self):
        self.item1=[];
        self.item2=[];
        self.mainq=[];
        
    def deQueueitem(self):
        return self.item1.pop(0)
    def demain(self):
        return self.mainq.pop(0); 
    def deQueueitem2(self):
        return self.item2.pop(0)    

    def enQueueitem(self,i):
        self.item1.append(i);
    def enQueueitem2(self,i):
        self.item2.append(i);

    def isEmpty(self):
        return self.item1==[];
    def peek(self):
        return self.item1[0];
    def size(self):
        return len(self.item1);

inpt = input("Enter people : ")   
q=QUEUE();
count =0
rounds=0
# [main][item1][item2]

for i in inpt:
    q.mainq.append(i)
   
for j in range(len(inpt)):
    for k in inpt:
        if(q.mainq != []):
            q.demain()
            
            if(q.item1 != [] and count%3 == 0):
                q.deQueueitem()
                q.enQueueitem(k)
                
            else:
                if(len(q.item1)>=5 ):
                    
                    q.enQueueitem2(k);    
                    if(rounds%2==0 and q.item2 !=[] ):
                        q.deQueueitem2()
    
                else:    
                    q.enQueueitem(k) 

            count+=1
            rounds+=1                 
            print(count,q.mainq,q.item1,q.item2,"----------",k)
            
"""

