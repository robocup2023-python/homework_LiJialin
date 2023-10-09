num = [1,2,3,4,6,7,9,10,11,12]
x = int(input())
i = 0
while((i<len(num))and(x >= num[i])):
  i += 1
num.insert(i,x)
print(num)