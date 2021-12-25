def calcu(input,num_in):
    newlist=[]
    for i in range(0,num_in-2):
        for j in range(i+1,num_in-1):
            for k in range(j+1,num_in):

                if((input[i]+input[j]+input[k])==5):
                    if((input[i]==input[j] or input[i]== input[k] or input[j]== input[k])):
                        # temp=[input[i],input[j],input[k]]
                        # temp.sort()
                        # newlist.append(temp)
                        newlist.extend([input[i],input[j],input[k]])  # extend เป็น list ที่ไม่มี []              
                        newlist.sort()
                        print([newlist])          
                        exit();

                    else:
                        newlist.append([input[i],input[j],input[k]])
                else : pass;

    print(newlist);

inpunumlist = input("Enter Your List : ").split();
result = list(map(int,inpunumlist)); 
k=0; 
for i in result:
   k=k+1 if(type(i)==int) else ""      
print("Array Input Length Must More Than 2")+exit() if(k<=2) else ""
manynum = len(result) # get many member

calcu(result,manynum)