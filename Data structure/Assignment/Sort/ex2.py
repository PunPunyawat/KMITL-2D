def sortnum(data):

    for last in range(1,len(data)):
        # swappos = False
        maxnum = 0

        for i in range(len(data)+1-last):
            
            if(data[i] < 0):
                # print(data[i],"--")
                continue

            elif(data[i] > data[maxnum]):
                # print(maxnum,"---")
                maxnum = i
            
        if(data[len(data)-last] < 0 ):
            continue

        else:    
            data[len(data)-last] , data[maxnum] = data[maxnum] , data[len(data)-last]

        
inp = [int(i) for i in input("Enter Input : ").split()]
sortnum(inp)
for i in inp :
    print(i,end=" ")