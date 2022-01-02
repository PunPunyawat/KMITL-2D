class STACK:
    def __init__(self):
        self.item = []

    def push(self, i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def emptylist(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def show(self):
        print(self.item)


opensymbol = ["(", "[", "{"]
closesymbol = [")", "]", "}"]
er = 0
stack = STACK()
inputfr = input("Enter expresion : ")

for i in inputfr:
    if(i in opensymbol):
        stack.push(i)
    elif(i in closesymbol):
        if(not stack.emptylist()):
            if(opensymbol.index(stack.peek()) != closesymbol.index(i)):
                er = 1
            else:
                stack.pop()
        else:
            er = 2
if(not stack.emptylist() > 0 and er == 0):
    er = 3

if(er == 0):
    print(inputfr, "MATCH")
if(er == 1):
    print(inputfr, "Unmatch open-close")
if(er == 2):
    print(inputfr, "close paren excess")
if(er == 3):
    print(inputfr, "open paren excess  ",
          stack.size(), ":", "".join(stack.item))
