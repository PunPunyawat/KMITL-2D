class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, indata):
        p=Node(indata);
        if(self.root == None):        
            self.root = p
   
        else:   
            temproot = self.root;        
            while indata != None:   
                if(temproot.data > indata):
                    if(temproot.left == None):
                        temproot.left = p ;
                        
                        break;
                    else:
                        temproot = temproot.left

                elif(temproot.data < indata):
                    if(temproot.right == None):    
                        temproot.right = p;
                        break;
                    else:
                        temproot = temproot.right
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return self.root            

    def checkpos(self,data):
        global counttree
        subtree = self.root
        while True:
            if(subtree.data == data and counttree == 0):
                print("Root");
                break;

            elif(subtree.data != data):
                if(subtree.data > data and subtree.left != None):
                    if(subtree.left.data == data and counttree == 0):
                        print("Inner")
                        break;
                    elif(subtree.left.data == data and counttree == 1):
                        print("Leaf")
                        break;
                    else:
                        subtree = subtree.left
                        counttree+=1;    

                elif(subtree.data < data and subtree.right != None):
                    if(subtree.right.data == data and counttree == 0):
                        print("Inner") 
                        break;
                    elif(subtree.right.data == data and counttree == 1):
                        print("Leaf")
                        break;
                    else:
                        subtree = subtree.right
                        counttree+=1;               
                else:
                    print("Not exist")    
                    break; 

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            # print(node.right,"noede")
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

counttree = 0
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in range(1, len(inp)):
    root = T.insert(inp[i])

T.printTree(root)
T.checkpos(inp[0])