arr = [1,2,3,4,5,6,7,8,9,0]
i = 0
m = 4
while(i<m):
  arr.insert(0,arr.pop(-1))
  i += 1
print(arr)