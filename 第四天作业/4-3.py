x = [[1,2,3],
     [4,5,6],
     [7,8,9]]
y = [[10,11,12],
     [13,14,15],
     [16,17,18]]
i = 0
j = 0
z = [[0 for m in range(3)]for n in range(3)]
while(i<3):
  while(j<3):
    z[i][j] = x[i][j] + y[i][j]
    j += 1
  i += 1
  j = 0
print(z)