from enum import Enum, unique, auto


@unique  # sınıf içerisinde aynı index değerine sahip olan 2. bir eleman yer alamaz
class Icecek(Enum):
    Vanilya = auto()
    Cikolata = 2
    Visne = auto()
    Muzlu = 4
    Kirazli = 75
    Cilekli = auto()


liste = list(Icecek)
print(liste)

# [<Icecek.Vanilya: 1>, <Icecek.Cikolata: 2>, <Icecek.Visne: 3>, <Icecek.Muzlu: 4>, <Icecek.Kirazli: 75>, <Icecek.Cilekli: 76>]
