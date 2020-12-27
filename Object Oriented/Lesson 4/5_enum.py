from enum import Enum


class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3


print(Color.Blue)
print(repr(Color.Blue))  # <Color.Blue: 2>
print(Color.Red.name)  # sınıfın isim değerini teslim alırsınız
print(isinstance(Color.Blue,
                 Color))  # Color.Red Color sınıfının bir elemanııdır
