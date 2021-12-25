def Rshift(num,shift):
    num = num >> shift
    return num
    
n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))