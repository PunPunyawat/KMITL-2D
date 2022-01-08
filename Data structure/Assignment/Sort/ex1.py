def Bubble(data):
    global tempnum

    for last in range(len(data)-1,-1,-1):
        swaped = False
        tempnode = None

        for i in range(last):
            if(data[i] > data[i+1]):
                tempnode = data[i]     
                data[i] , data[i+1] = data[i+1], data[i]      
                swaped = True
            
        if(swaped == True):
            if(tempnum == len(data)-1):
                print("last step :",data,"move["+str(tempnode)+"]")
                break;

            else:
                print(tempnum,"step :",data,"move["+str(tempnode)+"]")  

            tempnum += 1;      
                   
        elif(swaped == False):
            print("last step :",data,"move["+str(tempnode)+"]")
            break;  

tempnum = 1 
# inp = input("Enter Input : ").split();
# inp = list(map(int,inp))

inp = [int(i) for i in input("Enter Input : ").split()]
Bubble(inp)