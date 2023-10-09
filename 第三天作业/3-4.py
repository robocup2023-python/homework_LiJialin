s = str(input())
t = []
for c in s:
  t.append(c)
t1 = []
for c in t:
  t1.append(c)
t.reverse()
print(t1==t)