#
h = 100
s = 0
i = 1
hm = 0
while(i<10):
    s += h*(0.5**i)*2
    hm = h*(0.5**i)
    i += 1
print('journey='+str(s)+'  max height='+str(0.5*hm))