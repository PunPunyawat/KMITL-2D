def length(n):
    global count
    if(n==""):
        return 0;
           
    else:
        if(count%2==0):
            print(n[0]+"*",end="")
        else:
            print(n[0]+"~",end="")
        count+=1;    
        return length(n[1:])+1

count=0;         
print("\n",length(input("Enter Input : ")),sep="")


"""
count=0;
def length(n):
    global count
    if(n==""):
        return 0;
           
    else:
        x=n.count("")
        print(x)
        if(x%2==1):
            print(n[0]+"*",end="")
        elif(x%2==0):
            print(n[0]+"~",end="")
        return length(n[1:])+1
          
print("\n",length(input("Enter Input : ")),sep="")

"""