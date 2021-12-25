from itertools import permutations

print("*** Fun with permute ***")
inputall= input("input : ").split(",")  # list

results = list(map(int, inputall)) # การแปลงค่าใน list เป้น int แล้วใส่ list อีกรอบ

print("Original Cofllection: ",results)

source = [[]];

for i in results:
  new_source = [];
  for j in source:
    for k in range(len(j)+1):
      new_source.append(j[:k] + [i]+ j[k:])
      source = new_source;

print("Collection of distinct numbers:\n",source)

