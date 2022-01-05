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
            # print("-----",indata,"before in ")
            while indata != None:  
                # print(indata," round re @@@@@@@@")
                # print(temproot.data," befor call")
                if(temproot.data > indata):
                    if(temproot.left == None):
                        temproot.left = p ;
                        # print(temproot.left,"left")
                        break;
                    else:
                        # print(temproot.left,"temp left !!!!!")
                        temproot = temproot.left
                        # print(temproot,"+++++++++++++")

                elif(temproot.data < indata):
                    # print("in again")
                    if(temproot.right == None):    
                        temproot.right = p;
                        # print(temproot.right,"right")
                        break;
                    else:
                        # print(temproot.right," temp right !!")
                        temproot = temproot.right
                        # print(temproot,"&&&&&&&&&")

            # print(self.root,"all ##########")            
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return self.root            

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            # print(node.right,"noede")
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    # print(i,"out loop ---------")
    root = T.insert(i)
# print(root,"head")    
T.printTree(root)



