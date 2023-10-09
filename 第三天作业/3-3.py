s = str(input())
print('是'+str(len(s))+'位数')
t = []
for c in s:
  t.append(c)
t.reverse()
for c in t:
  print(c,end='')