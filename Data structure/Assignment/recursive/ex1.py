def facto(n):
    if(n==0 or n==1):
        return 1;
    else:
        return facto(n-1)*n

inp = input("Enter Number : ")
print(inp+"!","=",facto(int(inp)))