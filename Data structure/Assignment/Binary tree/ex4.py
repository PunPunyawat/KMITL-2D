class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
      
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        p = Node(val)
        if self.root == None:
            self.root = p

        else:
            temproot = self.root   
            while True:
                if(temproot.data > val):
                    if(temproot.left == None):
                        temproot.left = p ;       
                        break;
                    else:     
                        temproot = temproot.left
                        
                elif(temproot.data < val):
                    if(temproot.right == None):    
                        temproot.right = p;    
                        break;
                    else:
                        temproot = temproot.right
        return self.root    

    def delete(self, node, data):
        if(node is None):    # base case
            print("Error! Not Found DATA")
            return
        if(node.data != data):   # not found
            if(node.data > data):
                node.left = self.delete(node.left, data)  # not found left
            elif(node.data < data):
                node.right = self.delete(node.right, data)  # not found right

        else:   # found !!!!
            if(node.left is None):   # left None
                node = node.right
                return node
            elif(node.right is None):  # right None
                node = node.left
                return node
            else:
                current = node.right
                while current.left is not None:
                    current = current.left

                node.data = current.data    # replace delete
                node.right = self.delete(node.right, current.data)  # permanent delete recursive.....
        return node

    def printTree90(self, node, level = 0):
        if(node != None):
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)

Tree = BinarySearchTree()
inp = input('Enter Input : ').split(',')
for i in range (len(inp)):
    if(inp[i][0] == 'i'):
        print("insert " + (inp[i][2:]))
        Tree.root=Tree.insert(int(inp[i][2:]))
        Tree.printTree90(Tree.root)
    if(inp[i][0] == 'd'):
        print("delete " + (inp[i][2:]))
        Tree.root=Tree.delete(Tree.root,int(inp[i][2:]))
        Tree.printTree90(Tree.root)
