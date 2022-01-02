class DoublyLinkList:
    class Node:
        def __init__(self,data,prev_to=None,next_to = None):
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
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur ,  s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        if self.size == 1 :
            x = self.head.value;
            return  str(x)
        cur ,  s = self.tail, str(self.tail.value) + " "
        while cur.prev != None :
            s += str(cur.prev.value) + " "
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.size==0

    def append(self,i):
        if(self.head==None):
            self.head = self.Node(i)  
            self.size+=1;

        else :
            q = self.nodeAt(self.size-1)
            x = self.Node(i,q,None)
            q.next = x;
            self.size+=1;
            if(x.next==None):
                self.tail = x


    def addHead(self,data):          
        if(self.isEmpty()):
            p = self.Node(data,None,None)
            self.head = p
            self.size+=1;
        else :
            k = self.head
            p  = self.Node(data,None,k)
            if(self.tail==None):
                self.tail = k;
                self.tail.prev=p
            if(self.size>=2):
                k.prev = p
                k = k.next;
            self.head = p 
            self.size+=1;

    def indexOf(self,data):
        q = self.head
        for i in range(self.size):
            if(q.value == data):
                return i
            q = q.next;
        return -1;   # กรณีไม่เจอตัวอะไรเลย          
     
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

    def seaech(self,data):
        return self.indexOf(data) >= 0  

    def insert(self,q,data):
        revertnum = -(self.size)
        if(q<=revertnum):
            if(self.size>=1):
                p = self.head
                x = self.Node(data,None,p)
                if(self.tail==None):
                    self.tail = p;
                    self.tail.prev=x
                if(self.size>=2):
                    p.prev = x
                    p = p.next;
                self.head = x
                self.size+=1;
                     
            else:
                p = self.Node(data,None,None)
                self.head = p
                self.size+=1;
                    
        elif(q>=self.size):
            if(self.size>=1):
                m = self.nodeAt(self.size-1)
                x = self.Node(data,m,None)   
                self.tail = x  
                m.next = x
                self.size +=1;

            elif(self.size==0):
                p = self.Node(data,None,None)
                self.head = p
                self.size+=1;    
        else:
            if(q>=revertnum and q<0):   # กรณีลบ        
                if(q==revertnum):
                    x = self.head
                    m = self.Node(data,None,x)
                    self.head = x.prev= m
                    self.size+=1;
                else: 
                    numnext = self.nodeAt(q)
                    numbef = self.nodeAt(q-1)
                    m = self.Node(data,numbef,numnext)
                    numnext.prev = numbef.next = m  
                    self.size+=1;           

            else:  # กรณที่เป็น + 
                numbef = self.nodeAt(q-1)
                numnext = self.nodeAt(q)
                if(q==0):
                    x = self.head
                    m = self.Node(data,None,x)
                    self.head = x.prev= m
                    self.size+=1;
                else:
                    m = self.Node(data,numbef,numnext)
                    numnext.prev = numbef.next = m
            
    def pop(self,i):
        if(i==0 and self.size >=0 ):
            self.head.prev = None
            self.head = self.head.next
            self.size-=1
        elif ( i == (self.size-1)) :
            x = self.nodeAt(i)
            p = x.prev
            p.next = None
            self.size -=1;
        else:
            self.popselect(self.nodeAt(i))    

    def popselect(self,i):
        p = i.prev
        x = i.next
        p.next = x 
        x.prev = p
        self.size-=1;

L = DoublyLinkList();
inp = input("Enter Input : ").split(",")

for i in range(len(inp)):
    if(inp[i][:2] == "AP"):
        L.append(inp[i][3:]);
    elif(inp[i][:2] == "AH"):
        L.addHead(inp[i][3:]);
    elif(inp[i][:2] == "SE"):
        if(L.seaech(inp[i][3:]) == True):
            print("Found",inp[i][3:],"in",L)
        else:
            print("Not Found",inp[i][3:],"in",L)
    elif(inp[i][:2] == "ID"):
        if(L.indexOf(inp[i][3:])==-1):
            print("Index ("+str(inp[i][3:]+") = -1 :"),L)
        else:
            print("Index ("+str(inp[i][3:])+") =",L.indexOf(inp[i][3:]),":",L);
    elif(inp[i][:2] == "SI"):
        if(L.size<=0):
            print("Linked List size = 0 : Empty")     
        else: print("Linked List size =",L.size,":",L)  
    elif(inp[i][:2]=="PO"):
        if(L.size>0 and (int(inp[i][3:])<L.size)):
            print("Success | "+str(L)+"-> ",end="") 
            L.pop(int(inp[i][3:]))
            print(L)
        else:
            print("Out of Range |",L);
    elif(inp[i][:2]=="IS"):
        x=inp[i].replace("IS ","")
        pos,item = x.split()
        L.insert((int(pos)),item)

print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
