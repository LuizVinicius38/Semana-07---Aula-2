num = input("")
if int(num) >= 10 and int(num) <= 99:
    primNum = str(num[0])
    segNum = str(num[1])
    moduloPrim = int(primNum) % 2
    moduloSeg = int(segNum) % 2
    if moduloPrim >= 1 and moduloSeg >= 1:
        print("Os dois dígitos são ímpares.")
    elif moduloPrim >= 1 or moduloSeg >= 1:
        print("Apenas um dígito é ímpar.")
    else:
        print("Nenhum dígito é ímpar.")
else:
    pass
