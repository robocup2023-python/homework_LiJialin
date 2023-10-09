i = 1
j = 0
k = 0
while(i<=9):
    s = 100*i+10*j+k
    if(i**3+j**3+k**3==s):
        print(s)
    k += 1
    if(k==10):
        j += 1
        k = 0
        if(j==10):
            i += 1
            j = 0