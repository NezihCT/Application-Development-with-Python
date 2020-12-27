a = 40  # değeri 40 olan sayısal bir değişken tanımladık
print(type(a))  # <class 'int'>

b = a  # b adında bir değişken tanımladık referansını a değişkeninden almasını sağladık

c = [b]  # c değişkeni tanımlayıp b değerini elemanı olarak atadık

print(type(c))  # <class 'list'>

del a  # a değişkenini ram üzerinden sildik
# print(a)  # NameError: name 'a' is not defined
print(
    b
)  # 40 => a içerisinde yer alan veriyi b adındaki değişkene kopyaladığımızdan, ram üzerinde b değişkeni için yeni bir alan oluşmuş olur o yüzden a değerini silsenizde, b üzerindeki veriyi tutmaya devam eder.
b = 100  # b değişkenin değerini 100 olarak değiştirdik.


class Point:
    def __init__(
        self,
        x=0,
        y=0
    ):  # eğer sınıf tanımlaması yapılırken değer verilmezse constructor'a default değeri 0'dır
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, " heap alan üzerinden silindi")


point1 = Point(10, 20)
point2 = point1
point3 = point1

print(id(point1), id(point2),
      id(point3))  # nesnelerin ram üzerindeki adresini ekrana yazdırma
# 140477489946576
# 140477489946576
# 140477489946576

c = 10  #  c değişkeninin ram üzerindeki adresi => 4516338656
y = c  # c değişkenini y değişkenine referans olarak verdiğimden üzerindeki sayısal tuttuğu değer ve referans adresini bize teslim eder.

# c => 4398533600
# y => 4398533600
print(id(c), id(y))

y = 100  #y değişkenine yeni bir değer atadığımdan dolayı ram üzerinde yeni bir referans adresi oluşur.
print(id(y))

# y => 4300855072

del point1
del point2
del point3