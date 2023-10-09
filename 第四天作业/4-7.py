player = list(range(1,234))
i = 0
while(len(player)>1):
  i = (i+2)%len(player)
  player.pop(i)
print(player[0])