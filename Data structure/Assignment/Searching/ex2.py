def Fist_greatervalue(lst,key):
    # print(lst)
    for data in range(len(lst)-1):
        if(lst[data] > key):
            return print(lst[data])
    return print("No First Greater Value")

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for key  in k :
    Fist_greatervalue(sorted(arr),key)
