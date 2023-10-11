import threading
import os
def newFile():
  path = './img'
  os.makedirs(path)
  i = 1
  while(i<=100):
    fullPath = path +'/'+ str(i)+'.png'
    file = open(fullPath,'w')
    file.close()
    i += 1
def changeName(i):
  old = './img/'+str(i)+'.png'
  new = './img/'+str(i)+'.jpg'
  os.rename(old,new)
def c1():
  for i in range(1,101):
    if i % 2 == 1:
      changeName(i)
def c2():
  for i in range(1,101):
    if i % 2 == 0:
      changeName(i)
newFile()
t1 = threading.Thread(target=c1)
t2 = threading.Thread(target=c2)
t1.start()
t2.start()
t1.join()
t2.join()