print("*** TorKham HanSaa ***")

inputall = input("Enter Input : ").split(",");
# print(inputall[0][0]) # [0] อันแรกบอกตัว index [0]ตัวหลังบอกตัวเลขในข้อมูลนั้น
temp=[]; num=1

for i in range(len(inputall)):
    # print(inputall[i-1][-2:].lower(),"--------",inputall[i][2:4].lower())
    
    if(inputall[i][0]=="P" ):
        if(num==1):
            temp.append(inputall[i][2:]) 
            print("'"+inputall[i][2:]+"' ->",temp);
            num=num+1;
            continue;
        else:
            if(inputall[i-1][-2:].lower()==inputall[i][2:4].lower()):
                temp.append(inputall[i][2:])
                print("'"+inputall[i][2:]+"' ->",temp); 
            else:
                print("'"+inputall[i][2:]+"' ->","game over")         


    elif(inputall[i][0]=="p"):
        print("'"+inputall[i]+"' is Invalid Input !!!");
        exit();

    elif(inputall[i][0]=="R"):
        print("game restarted")
        num=1;
        temp.clear();

    elif(inputall[i][0]=="X"):
        exit();   

