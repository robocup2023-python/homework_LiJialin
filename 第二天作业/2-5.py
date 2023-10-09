i = 101
while(i<=200):
    j = 2
    y = 1
    while(j<i):
        y *= i % j
        j += 1
    if(y!=0):
        print(i)
    i += 1