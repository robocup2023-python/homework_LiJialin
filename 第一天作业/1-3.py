fibonacci = [1,1]
i =2
while(i<20):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    i += 1
for f in fibonacci :
    print(f)