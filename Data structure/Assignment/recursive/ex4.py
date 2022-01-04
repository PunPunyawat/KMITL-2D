temp = []
addbfina = []
fina = []
def perket(data,index,l,cl):
    if index == len(data):
        # print(l,"BE1")
        # print(cl,"BE2")
        cl.append(l)
        # print(l,"BE3")
        # print(cl,"BE4")
        return
    # print(l,"BE5")
    # print(cl,"BE6")  
    # print(l + [(data[index])],"tere")  
    perket(data,index+1, l + [(data[index])],cl)
    # print("in")
    perket(data,index+1,l,cl)
inp = input("Enter Input : ").split(",")

perket(inp,0,temp,addbfina)
# print(temp,"af1")
# print(cl,"af2")
for i in addbfina:
    a = 1; b = 0
    for j in i :
        j = j.split()
        # print(j)
        a*=int(j[0])
        b+=int(j[1])
        # print(a,"--",b)
    if len(i) != 0:
        # print(abs(a-b),"pun")
        fina.append(abs(a-b))
print(min(fina))