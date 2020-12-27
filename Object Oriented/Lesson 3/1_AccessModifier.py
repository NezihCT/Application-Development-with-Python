class Cup1:
    def __init__(self):
        self.color = None  # public variable
        self.content = None  # public variable

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def __str__(self):
        # return self.color + " " + self.content
        return f"{self.color} {self.content}"


cup1 = Cup1()
cup1.color = "Red"
cup1.content = "Tea"

# print(cup1)
cup1.empty()
cup1.content = "coffee"
# print(cup1)


class Cup2():
    def __init__(self):
        self.color = None  # public variable
        self._content = None  # protected variable

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def __str__(self):
        return f"{self.color} {self._content}"


cup2 = Cup2()
cup2.color = "Yellow"

# yanlış kullanım şeklidir.
cup2._content = "tea"  #_ ile işaretlenmişse korumalı(protected) olarak işaretlenmiş anlamına gelir. kullanım gereği instance(örnek) aldıktan sonra değer ataması yapmamanız gerekmektedir. Eğer dışarıdan değer ataması yapacaksanız constructor içerisinden gönderebilirsiniz.

# _ bir alt tire ile işaretli ise, protected anlamına gelir ve bu değer sınıf üzerinden değil miras verilen sınıf üzerinden erişim sağlanır.
# print(cup2)


class Cup3():
    def __init__(self):
        self._color = None  # Korulalı (protected) variable
        self.__content = None  # Gizli (private) variable


cup3 = Cup3()
cup3._color = "red"

print(cup3.__content
      )  # AttributeError: 'Cup3' object has no attribute '__content'