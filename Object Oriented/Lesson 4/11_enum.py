from enum import Enum


# value olarak farklı veri tipleri tanımlayabilirsiniz
class Renkler(Enum):
    Kirmizi = 1
    Sari = 2
    Mavi = "Blue"
    Mail = "mail adresi @ işareti içermelidir. Lütfen kontrol ediniz"


print(repr(Renkler.Mavi))  # <Renkler.Mavi: 'Blue'>
print(Renkler.Mavi.value)  # Blue


# enum sınıfı tanımlarken bir veri tipi belirleseniz, value olarak o veri tipi harici bir değer veremezsiniz.
class IntEnum(int, Enum):
    Kirmizi = 1
    Mavi = 2
    # Sari = "Yellow"


# print(IntEnum.Sari)  # ValueError: invalid literal for int() with base 10: 'Yellow'


class floatEnum(float, Enum):
    Kirmizi = 1
    Mavi = 2
    Yesil = 1.1


print(floatEnum.Yesil.value)