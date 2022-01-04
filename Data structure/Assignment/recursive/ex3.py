def play(num,rounds):    
    if(rounds>0):
        play(num,rounds-1);
    print(bin(rounds)[2:].zfill(num))    

num=(int(input("Enter Number : "))); 
if(num <=-1 ):
    print("Only Positive & Zero Number ! ! !")
    exit()
elif(num==0):
    print("0")
    exit()    
rounds=(2**num)-1;
play(num,rounds)
