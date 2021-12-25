
from functools import partial
from itertools import permutations
# อันนี้เหมือนอันล่างแต่ เลขมันรวมเป็นก้อนแบล้วค่อยสลับ

print("*** Fun with permute ***")
inputall= input("input : ").split(",")  # list

results = list(map(int, inputall)) # การแปลงค่าใน list เป้น int แล้วใส่ list อีกรอบ
print(type(results))

print("Original Cofllection:",results)
print("Collection of distinct number: ",end="")

total = [''.join(p) for p in permutations(inputall)]
print(total)

'''
การรับค่าหลายตัวแล้วสลับตำแหน่งเหมือนความน่าจะเป้น

from itertools import permutations

def funco(number):
  result_perms = [[]]
  
  for n in number:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms


print("*** Fun with permute ***")
inputall= input("input : ").split(",")  # list
print(inputall,"    -------- list str");

results = list(map(int, inputall)) # การแปลงค่าใน list เป้น int แล้วใส่ list อีกรอบ
print(results,"     -------- list int");
print("Original Cofllection: ",results)
print("Collection of distinct numbers:\n",funco(results))




'''



