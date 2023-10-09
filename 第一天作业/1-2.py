x = float(input('Please input x'))
y = float(input('Please input y'))
z = float(input('Please input z'))
if(x>y):
    temp = x
    x = y
    y = temp
if(y>z):
    temp = y
    y = z
    z = temp
if(x>y):
    temp = x
    x = y
    y = temp
print('From small to big :' + str(x) + '  ' + str(y) + '  ' + str(z))