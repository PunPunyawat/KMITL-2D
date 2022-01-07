k, inpday = input('Enter Input : ').split('/')  # num and day
inpday = [int(i) for i in inpday.split()]
num = []
vanCar = {}    # dict

for i in range(int(k)):
    num.append(i + 1)           # number of vanCar
    vanCar[i + 1] = vanCar.get(i + 1, 0)  # set day to 0 of vanCar  // .get(data, defaultNum)
    # print(vanCar[i + 1],"------",num)

for i in range(len(inpday)):
    minNum = num.pop(0)
    # print(minNum,"++")
    vanCar[minNum] = vanCar.get(minNum, 0) + int(inpday[i])    # add day reserve by dayList[i]
    # print(vanCar[minNum],"@@@@@",int(inpday[i]),"--",vanCar.get(minNum, 0))
    print(f"Customer {i+1} Booking Van {minNum} | {inpday[i]} day(s)")

    for index in range(len(num)):   # run every index
        # print("in index")
        # day[0] < day[1,2,3,4,5,6,7,8...] // day[0] == day[1,2,3,4,5,6,7,8...] and minNum < number (same day..different number)
        if vanCar[minNum] < vanCar[num[index]] or (vanCar[minNum] == vanCar[num[index]] and minNum < num[index]):
            num.insert(index, minNum)  # sorted and insert min between list
            minNum = None
            # print("in if var")
            # print(num,"num 888888888")
            break

    if minNum is not None:  # if can't insert and have minNum
        num.append(minNum)  # append last one to num


