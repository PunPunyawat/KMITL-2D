powerList, groupList = input("Enter Input : ").split("/")
powerList = [int(i) for i in powerList.split()]
groupList = [str(i) for i in groupList.split(",")]
sumList = []

def Mondstadt(data):
    sum = 0                             # initial sum = 0

    if data >= len(powerList):             # if out of array
        return 0

    sum += Mondstadt(2 * data + 1)     # go index left
    sum += Mondstadt(2 * data + 2)     # go index right
    return powerList[data] + sum           # sum of (powerList[index] + sum)

print(Mondstadt(0))                 # node sum (index = 0)

for i in groupList:
    i = list(map(int, i.split()))       # 2 group compare
    sum1 = Mondstadt(i[0])          # group 1st
    sum2 = Mondstadt(i[1])          # group 2nd

    if(sum1 > sum2):
        print(i[0], ">", i[1], sep="")
    elif(sum1 < sum2):
        print(i[0], "<", i[1], sep="")
    else:
        print(i[0], "=", i[1], sep="")