a = int(input('num A'))
n = int(input('How many times'))
i = 1
s = 0
t = 0
while(i<=n):
    j = 0
    while(j<i):
        t += a*(10**j)
        j += 1
    s += t
    t = 0
    i += 1
print(str(s))