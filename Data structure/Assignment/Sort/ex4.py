def sort_alphabet(data):

    for i in range(len(data)):
        tempalpha = ""
        tempposi = 0
        # print("in",i)
        for j in range(len(data)-i):
            for k in data[j]:
                if("a" <= k <= "z"):
                    if(j == 0):
                        tempalpha = k
                        # print(tempalpha," alpha ",j)
                        # print(j,"round______________________________",k)
                    else:
                        # print(j,"round------------------------------",k)
                        if(k > tempalpha):
                            # print("inside :)))")
                            tempalpha = k
                            # print(tempalpha," alpha ")
                            tempposi = j
                            # print(tempposi," possi ")

        data[len(data)-i-1] , data[tempposi] = data[tempposi] , data[len(data)-i-1]  # swap
        # print(data[len(data)-i-1] , data[tempposi],"+++")
        # print("##################################")
    return data                   

inp = input("Enter Input : ").split()
print(" ".join(sort_alphabet(inp)))