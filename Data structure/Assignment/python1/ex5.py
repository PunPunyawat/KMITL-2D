inputf=int(input("Enter Input : "))+2;

for i in range(0,inputf):
    
    for f in range(inputf,i+1,-1):
        print(".",end="")

    for k in range(0,i+1):
        print("#",end="")

    for l in range(0,inputf):
        if i==0 or i==(inputf-1) or l==0 or l==(inputf-1):
            print("+",end="");
        else:
            print("#",end="")    
    print();

for i in range(0,inputf):
    for l in range(0,inputf):
        if i==0 or i==(inputf-1) or l==0 or l==(inputf-1):
            print("#",end="");
        else:
            print("+",end="")  

    for k in range(inputf,i,-1):
        print("+",end="");

    for j in range(0,i):
        print(".",end="")
        
    print()        