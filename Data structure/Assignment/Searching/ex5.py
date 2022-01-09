def Box(lst, numBox):
    left = max(lst)  ; right = sum(lst)
    while left <= right:
        box_size = (left+right)//2 
        sumBox = 0 ; i = 0
        while i < len(lst):
            weight = 0
            while i < len(lst) and weight + lst[i] <= box_size:  # put item in box
                weight += lst[i]
                i += 1
            sumBox += 1
        if sumBox <= numBox:  # too large
            right = box_size - 1
        else:  # too light
            left = box_size + 1
    return left


inp, box = input("Enter Input : ").split('/')
box = int(box)
inp = list(map(int, inp.split()))
print(f"Minimum weigth for {box} box(es) = {Box(inp, box)}")