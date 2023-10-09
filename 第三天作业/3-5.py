year = int(input())
i = 0
y = []
for c in str(year):
  y.append(c)
if(y[-1]=='0'):
  i = year % 400
else:
  i = year % 4
print(i==0)