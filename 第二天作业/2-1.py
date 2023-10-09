string = input('Str input')
num = 0
char = 0
other = 0
for c in string:
    if(c.isalpha()):
        char +=1
    elif(c.isdigit()):
        num += 1
    else:
        other +=1
print('Char: '+ str(char)+'  Number: '+str(num)+' Other: '+str(other))