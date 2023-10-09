def f(*arg):
  i = 0
  j = []
  while(i<len(arg)):
    if(i%2 != 0):
      j.append(arg[i])
    i += 1
  return j