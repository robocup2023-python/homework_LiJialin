i=1
j=1
while(i<=9):
    while(j<=i):
        print(str(i)+'*'+str(j)+'='+str(i*j)+'\t',end='')
        j += 1
    j = 1
    i += 1
    print()