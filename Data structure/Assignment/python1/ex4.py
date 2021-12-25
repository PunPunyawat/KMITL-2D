print("*** Fun with Drawing ***")

inputall = int(input("Enter input : "))

if(inputall < 2):
    exit();

else:
    for i in range(1, inputall):
        for j in range(i, inputall):
            print(".", end="");
        for j in range(2 * i - 1):
            if j == 0 or j == (2 * i - 2):
                print("*", end="");
            else:
                print("+", end="");
            j + 1
        for j in range(i, inputall):
            print(".", end="");

        for k in range(i + 1, inputall):
            print(".", end="");
        for k in range(2 * i - 1):
            if k == 0 or k == (2 * i - 2):
                print("*", end="");
            else:
                print("+", end="");
            k + 1
        for k in range(i, inputall):
            print(".", end="");

        print();


    print("*", end="");
    for l in range(2 * inputall - 3):
        print("+", end="");
    print("*", end="");
    for m in range(2 * inputall - 3):
        print("+", end="");
    print("*", end="");



    print()
    for n in range(1, 2 * inputall - 1):
        for p in range(n):
            print(".", end="");
        for Q in range(4 * inputall - (2 * n) - 3):
            if Q == 0 or Q == (4 * inputall - (2 * n) - 4):
                print("*", end="");
            else:
                print("+", end="") ;             
        for r in range(n):
            print(".", end="");

        print();

