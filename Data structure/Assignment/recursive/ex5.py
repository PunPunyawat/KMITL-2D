def staircase(n,k):
    
    if(n>=1):
        print("_"*(n-1)+"#"*k);
        staircase(n-1,k+1)

    elif(n<0):
        print("_"*(k-1)+"#"*(abs(n)))
        staircase(n+1,k+1)

    elif(n==0 and k==1):
        return print("Not Draw!")
      
staircase(int(input("Enter Input : ")),1)





