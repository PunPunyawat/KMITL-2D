"""
class SinglyLinkedListNoDummy :     # ทำงานเหมือนกับ List (อ้าง อินเด็กซ์แบบเดียวกัน)
    class Node :                    # โหนดเก็บข้อมูล
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
            
    def __str__(self):                # แสดงข้อมูลทุกตัวใน linked list
        s = 'linked data : '
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next     
        return s
          
    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size         
            
    def isEmpty(self) :               # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.size == 0
        
    def indexOf(self,data) :          # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head

        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :             # ตรวจสอบว่าใน linked list นี้ มีข้อมูลตัวนี้ไหม
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):            # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if self.head is None :
          p = self.Node(data)
          self.head = p
          #self.head = self.Node(data,None)
          self.size += 1
        else :                        # เพิ่ม ในกรณีที่ไม่ใช่ Node แรก
          self.insertAfter(len(self)-1,data)   #len(self) = จำนวนสมาชิก - 1 คือ index
    
    def insertAfter(self,i,data) :       #เพิ่ม ข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        #q.next = self.Node(data,q.next)
        self.size += 1
    
    def deleteAfter(self,i) :            #ลบ โหนดข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        if self.size > 0 :  # len(self)
          q = self.nodeAt(i)
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :                 #ลบข้อมูลที่ อินเด็กซ์ที่กำหนด
        if i == 0 and self.size > 0 :    #ลบตัวแรก
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)          #ลบตัวก่อนหน้า
        
    def removeData(self,data) :          #ลบข้อมูลใน linked list
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head = p
          #self.head = self.Node(data,None)
          self.size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.size += 1


l1 = SinglyLinkedListNoDummy()
l1.addHead('a')
print(l1 ," อันแรกก ")
l1.addHead('b')
print(l1)





l1.append('b')
l1.append('c')
l1.append('d')
l1.append('e')
l1.append('z')
l1.append('aa')
print(l1,"---------",len(l1))
l1.delete(0)
print(l1)
l1.delete(2)
print(l1,len(l1))
l1.delete(len(l1)-1)
print(l1)
l1.delete(0)
print(l1)
l1.delete(len(l1)-1)
print(l1)
"""



"""
class DoublyLinkedListNoDummy :
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data

            if prev is None :
                self.prev = None
            else :
                self.prev = prev

            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):
        s = 'linked data : '
        p = self.head
        for i in range(len(self)) :
            s += str(p.data) + ' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
        
    def isEmpty(self) :
        return self.size == 0
    
    def indexOf(self,data) :
        q = self.head
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def insert(self,q,data) :
          p = q.prev
          x = self.Node(data,p,q)
          p.next = q.prev = x
          self.size += 1
        
    def append(self,data) :
        if self.head == None :
          self.head = self.Node(data)
          self.size += 1
        else :
          q = self.nodeAt(len(self)-1)
          x = self.Node(data,q,None)
          q.next = x
          self.size += 1
    
    def removeNode(self,q) :
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1
        
    def delete(self,i) :
        if i == 0 :      # เอาออกที่หัว
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        elif i == len(self) - 1 :    # เอาออกที่ท้าย
            x = self.nodeAt(i)
            p = x.prev
            p.next = None
            self.size -= 1
        else:
            self.removeNode(self.nodeAt(i))    # เอาออกเฉพาะที่


l2 = DoublyLinkedListNoDummy()
l2.append('a')
print(l2)
l2.append('b')
print(l2)
l2.append('c')
l2.append('d')
l2.append('e')
print(l2)
l2.append('z')
print(l2)
l2.delete(0)
print(l2)
l2.delete(2)
print(l2)
l2.delete(3)
print(l2)"""

