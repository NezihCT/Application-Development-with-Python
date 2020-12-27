from enum import Enum


class Icecek(Enum):
    Vanilya = 7
    Cikolata = 4
    Visne = 3
    Muzlu = 1


for x in Icecek:
    print(x)

for ad, uye in Icecek.__members__.items():
    print(str(ad) + " " + str(uye))
    print(ad, uye)