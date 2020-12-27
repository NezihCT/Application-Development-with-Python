# dışarıdan aldığı değere göre içi dolu kare çiziniz


def KareCizVol1(x):
    index = 0
    while index < x:
        metin = ""
        for i in range(x):
            metin += "X "
        print(metin)
        index += 1


# KareCizVol1(10)

def KareCizVol2(x):
    index = 0
    while index < x:
        print("X "*x)
        index += 1


# KareCizVol2(10)


def KareCizVol3(x):
    for i in range(x):
        print("X "*x)


KareCizVol3(10)
