class Linkedlist:

    class Node :
        def __init__(self,i,nexstate = None):
            self.value = i
            if(nexstate is None):
                self.next = None;
            else : self.next = nexstate


    def __init__(self):
        self.head = None;
        self.size = 0;

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s           

    def nodeAt(self,i) : # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def isEmpty(self):
        return self.head == None;

    def append(self,i):   # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if(self.head==None):    # กรณีตัวแรกไม้มี
            p = self.Node(i)
            self.head = p
            self.size+=1
        else:       # เพิ่ม ในกรณีที่ไม่ใช่ Node แรก
            self.insertAfter(self.size-1,i)

    def insertAfter(self,i,data): # เพิ่มข้อผลต่อจากที่มีหัวแล้ว
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.size +=1; 

    def addHead(self,i):
        if(self.isEmpty()):
            p = self.Node(i);
            self.head = p
            self.size+=1;
        else :
            p = self.Node(i,self.head);
            self.head = p
            self.size +=1

    def search(self,i):
        return self.indexOf(i) >= 0 ;

    def indexOf(self,i):   # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head;

        for j in range(self.size):
            if(p.value == i):
                return j  
            p = p.next
        return -1  

    def pop(self,i):
        if(i==0 and self.size>0):
            if(self.head.next != None):
                self.head = self.head.next
                self.size -=1;
            else:
                self.head=None
                self.size=0    
        else:
            self.deleteAfter(i-1)

    def deleteAfter(self,i) :     #ลบ โหนดข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        if self.size > 0 :  
          q = self.nodeAt(i)
          q.next = q.next.next
          self.size -= 1


L = Linkedlist()
inp = input("Enter Input : ").split(",")

for i in range(len(inp)):
    if(inp[i][:2]=="AP"):
        L.append(inp[i][3:]);
    elif(inp[i][:2]=="AH"):
        L.addHead(inp[i][3:]);
    elif(inp[i][:2]=="SE"):
        if(L.search(inp[i][3:])  == True):
            print("Found",inp[i][3:],"in",L)  
        else:
            print("Not Found",inp[i][3:],"in",L)     
    elif(inp[i][:2]=="ID"):
        if(L.indexOf(inp[i][3:])== -1):
            print("Index ("+str(inp[i][3:])+") = -1 :",L)  
        else:
            print("Index ("+str(inp[i][3:])+") =",L.indexOf(inp[i][3:]),":",L)
    elif(inp[i][:2]=="SI"):
        if(L.size<=0):
            print("Linked List size =",L.size,": Empty");
        else:
            print("Linked List size =",L.size,":",L)    

    elif(inp[i][:2]=="PO"):   
        if(L.size>0 and (int(inp[i][3:]) < L.size)): 
            print("Success | "+str(L)+"-> ",end="") 
            L.pop(int(inp[i][3:]))
            print(L)
        else:
            print("Out of Range |",L);

print("Linked List :",L)


 

