import random
def writeInFile():
  path = 'data.txt'
  file = open(path,'w')
  file.close()
  i = 1
  while(i<=10000):
    rand = int(random.random()*100+1)
    f = open(path,'a')
    f.write('\n'+str(rand))
    f.close()
    i += 1
  