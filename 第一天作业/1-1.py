unit = 1
ten =1
hundred =1
while (hundred <= 4):
    while (ten <=4):
        while (unit <=4):
            if(unit != ten & unit!= hundred & ten != hundred):
                    print(100*hundred + 10*ten + unit)
            unit +=1
        ten +=1
        unit = 1
    hundred +=1
    ten = 1