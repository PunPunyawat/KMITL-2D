def insert_recur(data,n):

    if(n <= 1):
        return 

    insert_recur(data,n-1)
    # print(n,"--  round")
    templast = data[n-1]
    # print(templast,"  ====== templast (n-1)")
    beforelast = n-2   
    # print(beforelast,"  ====== beforelast (n-2)")
    # print(data,"---- data")
    # print("---------------------------------------------")
    # 1 3 2 4                               0       3
    beforelast = forLoopRecursion(data,beforelast,templast)  
    # print(beforelast," nearly !!!! ")
    data[beforelast+1] = templast
    # print(data[beforelast+1],"-----",templast," ooooo")

    if(len(data) != n):
        print(f'insert {templast} at index {beforelast+1} :', data[:n], data[n:])
    else:
        print(f'insert {templast} at index {beforelast+1} :', data)


def forLoopRecursion(data, n, last):
    # base case
    if(n < 0 or data[n] < last):   # out of range and left is less than right
        return n

    data[n+1] = data[n]   # shift left position to right
    # print(data[n+1],"------------- shift")
    return forLoopRecursion(data, n-1, last)   # go left

inp=[int(i) for i in input("Enter Input : ").split()]
total=insert_recur(inp,len(inp))
print("sorted\n"+str(inp))
