num = input("")
if int(num) >= 100 and int(num) <= 999:
    primNum = str(num[0])
    segNum = str(num[1])
    terNum = str(num[2])
    moduloPrim = int(primNum) % 2
    moduloSeg = int(segNum) % 2
    moduloTer = int(terNum) % 2
    if moduloPrim == 0 and moduloSeg == 0 and moduloTer == 0:
        print("3")
    elif moduloPrim == 0 or moduloSeg == 0 and moduloTer ==0:
        print("2")
    elif moduloPrim == 0 or moduloSeg == 0 or moduloTer == 0:
        print("1")
    else:
        print("0")
else:
    pass
