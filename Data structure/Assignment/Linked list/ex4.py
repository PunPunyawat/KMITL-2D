class DoublyLiklist:
    class Node:
        def __init__(self,data,prev_to=None,next_to=None):
            self.value = data
            if(prev_to==None):
                self.prev=None
            else:
                self.prev=prev_to;
            if(next_to==None):
                self.next=None
            else:
                self.next = next_to
               
    def __init__(self):
        self.head = None
        self.tail = self.Node("|")
        self.size = 0
        self.countlift = True
        self.countdelete = True
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur,s = self.head , str(self.head.value) + " "    
        while cur.next!= None:
            s += str(cur.next.value) + " "
            cur = cur.next
        # if(self.size>=0):
        #     s = s+self.ll    
        return s    

    def append(self,i):
        indes = self.indexOf("|")
        if(self.head == None):
            self.head = self.Node(i) 
            self.size+=1;
        else:
            if(self.tail.next == None):
                t = self.tail
                q = self.nodeAt(self.size-1)
                x = self.Node(i,q,t)
                q.next = x;
                t.next = None;
                self.size+=1;
                # if(x.next==None):
                #     self.tail = x
                # print("in if")
            else:
                if(indes<=self.size-1):

                    if(indes!=1):
                        # print("pim")
                        t = self.tail
                        q = self.nodeAt(0)
                        x = self.Node(i,q,t)
                        self.size+=1; q.next = x
                        t.next = None ; self.head = q ;

                    else:
                        # print("in if 2 ")
                        t = self.tail 
                        q = self.nodeAt(indes-1)
                        m = self.nodeAt(indes+1)
                        x = self.Node(i,q,t)
                        self.size+=1;
                        q.next = x ; t.next = m ; t.prev =x
                          
                if(indes==0):
                    # print("inelse 2") 
                    t = self.tail
                    q = self.nodeAt(indes+1)
                    x = self.Node(i,None,t)
                    self.size+=1;
                    t.next = q; self.head = x

    def shlift(self):
        indes = self.indexOf("|")
        if(self.isEmpty()==True):
            # print("in em----------")
            pass
        else:    
            # print("sh lift else")   ใช้ self.tail.next == None  แทนในการเข้า
            # if(self.countlift==True):
                # if():
                #     t = self.tail
                #     p = self.nodeAt(self.size-1)
                #     m = self.nodeAt(self.size-2)
                #     m.next = t ;t.next = p ; p.next = None ;self.countlift=False
                    
                # elif():
                #     t = self.tail
                #     p = self.nodeAt(self.size-1)
                #     t.next = p ; p.next = None;   self.head = t

            if(self.tail.next == None):
                if(self.size>1):
                    # print("coming")   
                    t = self.tail
                    p = self.nodeAt(self.size-1)
                    m = self.nodeAt(self.size-2)
                    m.next = t ;t.next = p ; p.next = None ; 
                else:
                    # print("coming 111111") 
                    t = self.tail
                    p = self.nodeAt(self.size-1)
                    t.next = p ; p.next = None;   self.head = t
                # print("count ture")

            else:
                if(indes>1 and self.tail.next != None ):
                    # print("in indes > 1")
                    t = self.tail
                    # print(self.indexOf("|"),"-----")   
                    p=self.nodeAt(indes-1)
                    m=self.nodeAt(indes-2)
                    ne=self.nodeAt(indes+1)
                    m.next = t; t.next = p ; p.next = ne ; p.prev = t

                elif(indes==1):
                    # print("in indes == 1")
                    t = self.tail
                    p = self.nodeAt(indes-1)
                    ne = self.nodeAt(indes+1)
                    self.head = t; self.head.value = "|"    
                    t.next = p ; p.next = ne
                    
                elif(self.tail.prev != None):
                  
                    if(self.size>1):
                        # print("on")
                        t = self.tail
                        p = self.nodeAt(self.size-1)
                        m = self.nodeAt(self.size-2)
                        m.next = t; t.next = p ; p.next = None; t.prev=None
 
                # elif(self.tail.next == None):   เอาไปใช้แทนข้างบนเลยกรณี อยุ่ขวาสุด
                #     if(self.size>1):
                #         # print("coming")   
                #         t = self.tail
                #         p = self.nodeAt(self.size-1)
                #         m = self.nodeAt(self.size-2)
                #         m.next = t ;t.next = p ; p.next = None ; 
                #     else:
                #         # print("coming 111111") 
                #         t = self.tail
                #         p = self.nodeAt(self.size-1)
                #         t.next = p ; p.next = None;   self.head = t
                    
    def shright(self):
        indes = self.indexOf("|")
        if(indes<self.size-1 and indes >=1 ):
            t = self.tail
            p = self.nodeAt(indes-1)
            m = self.nodeAt(indes+1)
            q = self.nodeAt(indes+2)
            p.next = m; m.next = t ; t.next =q ; m.prev = p
        else:
            if(indes == 0):
                t = self.tail
                m = self.nodeAt(indes+1)
                p = self.nodeAt(indes+2)
                m.next = t ; t.next = p ;self.head = m ; 

            elif(indes == self.size-1 and self.tail.next != None ):
                # print("out")
                t = self.tail
                p = self.nodeAt(indes-1)
                ne = self.nodeAt(indes+1)
                p.next = ne; ne.next = t; t.next = None ; t.prev=ne
                # print(p.value,ne.value,t.next,"-------------- check",t.value)

    def backleft(self):
        indes = self.indexOf("|")
        if(indes!=0):
            if(indes >1):
                t = self.tail
                p = self.nodeAt(indes-2)
                ne = self.nodeAt(indes+1)
                p.next = ne.prev = t; t.next=ne
                self.size-=1;
            else:
                t =self.tail
                p = self.nodeAt(indes+1)
                self.head=t
                t.next = p; p.prev = t;  
                self.size-=1;  

    def backright(self):
        indes = self.indexOf("|")
        if(indes < self.size-1  and self.tail.next != None):
            t = self.tail
            p = self.nodeAt(indes+2);
            m = self.nodeAt(indes-1);
            m.next = p.prev = t ; t.next = p
            self.size-=1;
            # print("in 1")
            
        elif(self.tail.next != None and self.countdelete == True):
            t = self.tail
            p = self.nodeAt(self.size-1)
            t.next = None
            self.countdelete = False
            self.size-=1;
            # print("in2")

    def nodeAt(self,i):
        p = self.head
        t = self.tail
        if(i>=0):
            for j in range(0,i):
                p = p.next
            return p   
        else:
            for j in range(-1,i,-1):
                t = t.prev
            return t  

    def indexOf(self,data):
        q = self.head
        for i in range(self.size):
            if(q.value == data):
                return i
            q = q.next;
        return -1;   # กรณีไม่เจอตัวอะไรเลย 

    def isEmpty(self):
        return self.size==0


inp = input("Enter Input : ").split(",")
L = DoublyLiklist()
for i in range(len(inp)):
    if(inp[i][:1]=="I"):
        L.append(inp[i][2:])
    elif(inp[i][:1]=="L"):
        L.shlift()
    elif(inp[i][:1]=="R"):
        L.shright()
    elif(inp[i][:1]=="B"):
        L.backleft()
    elif(inp[i][:1]=="D"):
        L.backright()

print(L)

