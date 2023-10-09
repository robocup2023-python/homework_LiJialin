def isLeap (year):
  i = 0
  y = []
  for c in str(year):
    y.append(c)
  if(y[-1]=='0'):
    i = year % 400
  else:
    i = year % 4
  return i == 0
def days (month):#求整月提供的天数
  s = 0
  if(month<=7):
    while(month>0):
      s += 30 if month%2==0 else 31
      month -= 1
    s -= 2 #减去2月多算的（按28天计
  else:
    while(month>7):
      s += 31 if month%2==0 else 30
      month -= 1
    while(month>0):
      s += 30 if month%2==0 else 31
      month -= 1
    s -= 2 #减去2月多算的（按28天计
s = 0
year = int(input('年'))
month = int(input('月'))
day = int(input('日'))
if(isLeap(year)&month>2):
  s = days(year)+day+1
elif(month>2):
  s = days(year)+day
elif(month<=2):
  s = (month-1)*31+day
print(s)