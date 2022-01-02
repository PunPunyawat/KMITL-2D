class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = node()

    def __str__(self):
        return " -> ".join(str(i) for i in self.show())

    def addList(self,data):
        self.head = node()
        for i in data:
            self.append(i)

    def append(self,data):
        next_node,cur = node(data),self.head
        while cur.next != None:
            cur = cur.next
        next_node.prev = cur
        cur.next = next_node

    def show(self):
        temp,cur = [],self.head
        while cur.next != None:
            cur = cur.next
            temp.append(cur.data)
        return temp

    def lenght(self):
        cur,count = self.head,0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count
    
    def sort(self):
        cur = self.show()
        ls,strList = [],[]
        for i in cur:
            ls.append(int(i))
        ls = sorted(ls)
        for i in ls:
            strList.append(str(i))
        self.addList(strList)

def posi(pos,data): 
    pos = pos*-1
    try:
        digit = data[pos]
        return int(digit) if digit != '-' else 0
    except IndexError:
        return 0

def RaSort(useList):
    roundz,nInput = 0,len(useList)
    subList = list(LinkedList() for i in range(10))
    while True:
        roundz += 1
        for i,data in enumerate(useList):
            num = posi(roundz,data)
            for j in range(10):
                if num == j:
                    subList[j].append(data)
                    break

        for i in range(10):
            subList[i].sort()
        print("------------------------------------------------------------")
        print("Round :",roundz)
        for i,data in enumerate(subList):
            print(i,":"," ".join(data.show()))

        useList = []
        for i in subList:                               
            for j in i.show():
                useList.append(j)
        if subList[0].lenght() == nInput: 
            break   
        subList = list(LinkedList() for i in range(10)) #Clear sub list
    return roundz-1,useList


inp = input("Enter Input : ").split()
roundz,result = RaSort(inp)
print("------------------------------------------------------------")
print(roundz,"Time(s)")
print("Before Radix Sort :"," -> ".join(inp))
print("After  Radix Sort :"," -> ".join(result))
