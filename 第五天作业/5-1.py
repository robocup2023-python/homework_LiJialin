def cacluate(*num):
  avg = sum(num)/len(num)
  ind = []
  for n in num :
    if(n>avg):
      ind.append(n)
  a = (avg,ind)
  return a
print(cacluate(1,2,3))