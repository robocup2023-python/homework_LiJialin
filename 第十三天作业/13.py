import threading
import time
import random
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
  x = cell.position[0]
  y = cell.position[1]
  if(y-1<10 and x-2 < 20 and u_main.map[y-1][x-2]=='*'):
    num += 1
  if(y-1<10 and x < 20 and u_main.map[y-1][x]=='*'):
    num += 1
  if(y<10 and x-1 < 20 and u_main.map[y][x-1]=='*'):
    num += 1
  if(y-2<10 and x-1 < 20 and u_main.map[y-2][x-1]=='*'):
    num += 1
  return num
def clock():
  while(isContinue):
    time.sleep(5)
    for i in cells:
      neighbor = alive(i)
      if(neighbor<2 or neighbor>3):
        i.isAlive = False
      elif(neighbor==2 and i.isAlive == True):
        i.isAlive = True
      elif(neighbor==3 and i.isAlive == False):
        i.isAlive = True
    mapReload()
    print()
    print('下一代',end='')
    u_main.show()
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
# 激活25%新细胞
for i in range(0,50):
  initCell(cells[random.randint(0,199)])
mapReload()
u_main.show()
time.sleep(1)
isContinue = True
timer.start()
print('started')
# while(True):
#   check = input('输入info查看宇宙信息')
#   if(check=='info'):
#     u_main.show()
exit = input('按回车键退出')
isContinue = False
print('正在退出...')
timer.join()
# 两种卡主线程的方式，个人喜欢后一种