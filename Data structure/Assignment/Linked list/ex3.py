class Node:
    def __init__(self, data,next_tp = None):
        self.value = data   
        self.next = next_tp

def createList(datain):
    head = Node(datain[0])
    for i in datain[1:]:
        temp = head
        while temp.next != None :
            temp = temp.next
        temp.next = Node(i)   # ทำการเชื่อมต่อ node 
    return head

def printList(H): # ใช้สอนท้ายแสดงผลออกมาทีหลัง
    temp = H
    while temp != None :
        print(temp.value,end=" ")
        temp = temp.next

def mergeOrderesList(p,q):
    if(not p):
        return q
    if(not q):
        return p
    if(p.value <= q.value):
        p.next = mergeOrderesList(p.next,q)
        return p
    else:
        q.next = mergeOrderesList(p,q.next)
        return q

L1,L2 = input("Enter 2 Lists : ").split()
li1=[]; li2=[]
L1=L1.replace(","," ")
L2=L2.replace(","," ")

for i in range(1):   # เอาตัวเลขมาต่อกัน เป็น 1 ลิสเพื่อทำการ merge
    li1.extend(L1.split())
    li2.extend(L2.split())

li1new = list(map(int,li1))  # แปลงค่าภายในเป็น int 
li2new = list(map(int,li2))
print("LL1 :"," ".join(li1))
print("LL2 :"," ".join(li2))  # join ต้องเป็น str
headlist1 = createList(li1new)
headlist2 = createList(li2new)
total = mergeOrderesList(headlist1,headlist2)
print("Merge Result : ",end="")
printList(total)
