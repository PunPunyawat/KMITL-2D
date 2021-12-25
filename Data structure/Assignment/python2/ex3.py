temp1=[]

def odd_even(arr, s,oe):
    if((arr=="S"or arr=="s")and oe=="Odd"):
        for i in range(len(s)):
            if(i%2==0):
                print(s[i],end="")
        
    elif((arr=="S"or arr=="s")and oe=="Even"):     
        for i in range(len(s)):
            if(i%2==1):
                print(s[i],end="")



    elif((arr=="L"or arr=="l")and oe=="Odd"): 
        if(" " not in s):
            s = [''.join(s)]
            print(s)
        if(" " in s):
            for i in range(len(s)):
                if(i%4==0):
                    temp1.append(s[i])
            print(temp1);            

    elif((arr=="L"or arr=="l")and oe=="Even"):
        if(" " not in s):
            print("[]")
        if(" " in s):
            for i in range(len(s)):
                if(i%4==2):
                    temp1.append(s[i])
            print(temp1);



print("*** Odd Even ***")
st,mess,o_e = input("Enter Input : ").split(",")   

odd_even(st,mess,o_e);
   
