import threading
import time
import random
import os
class Universe():
  map = [[' ' for i in range(20)] for i in range(10)]
  def show(this):
    # print('显示地图')
    for i in this.map:
      print(i)
def mapReload():
  for i in cells:
    if(i.isAlive==True):
      u_main.map[i.position[1]-1][i.position[0]-1] = '*'
    else:
      u_main.map[i.position[1]-1][i.position[0]-1] = ' '
def initCell(cell):
  cell.isAlive = True
def alive(cell):
  num = 0
  x = cell.position[0]-1
  y = cell.position[1]-1
  m = u_main.map
  if(y-1>=0 and m[y-1][x]=='*'):#U
    num += 1
  if((y+1)<10 and m[y+1][x]=='*'):#D
    num += 1
  if((x-1)>=0 and m[y][x-1]=='*'):#L
    num += 1
  if((x+1)<20 and m[y][x+1]=='*'):#R
    num += 1
  if((x-1)>=0 and (y-1)>=0 and m[y-1][x-1]=='*'):#LU
    num += 1
  if((x+1)<20 and (y-1)>=0 and m[y-1][x+1]=='*'):#RU
    num += 1
  if((x-1)>=0 and (y+1)<10 and m[y+1][x-1]=='*'):#LD
    num += 1
  if((x+1)<20 and (y+1)<10 and m[y+1][x+1]=='*'):#RD
    num +=1
  return num
def clock():
  while(isContinue):
    time.sleep(0.5)
    for i in cells:
      neighbor = 0
      neighbor = alive(i)
      if(neighbor < 2 or neighbor > 3):
        i.isAlive = False
      elif((neighbor == 2 or neighbor == 3 ) and i.isAlive == True):
        i.isAlive = True
      elif(neighbor == 3 and i.isAlive == False):
        i.isAlive = True
    mapReload()
    os.system('cls || clear')
    # print()
    # print('下一代',end='')
    u_main.show()
    print('按回车键关闭...')
    # 可选，每次打印世界状态
class Cell():
  isAlive = bool
  isAlive_next = bool
  position = (None,None)
  def __init__(self,x:int,y:int) -> None:
    self.position = (x,y)
    pass
#  迭代用线程
timer = threading.Thread(target=clock)
# 宇宙和细胞创建
u_main = Universe()
cells = []
for i in range(1,11):
  for j in range(1,21):
    cells.append(Cell(j,i))
# 激活25%新细胞,25%感觉有点少，自己改多了点
for i in range(0,100):
  initCell(cells[random.randint(0,199)])
mapReload()
isContinue = True
os.system('cls || clear')
print('started')
u_main.show()
time.sleep(0.5)
timer.start()
# while(True):
#   check = input('输入info查看宇宙信息')
#   if(check=='info'):
#     u_main.show()
exit = input()
isContinue = False
print('正在关闭...')
timer.join()
# 两种卡主线程的方式，个人喜欢后一种