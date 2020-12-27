class Personel:
    def __init__(self, firstname, lastname):
        self.FirstName = firstname
        self.LastName = lastname

    def email(self):
        return f"{self.FirstName}.{self.LastName}@bilgeadam.com".lower()

    @property
    def Mail(self):
        return f"{self.FirstName}.{self.LastName}@bilgeadam.com".lower()

    @property  # getter metodu => geriye datayı teslim eder
    def FullName(self):
        return f"{self.FirstName} {self.LastName}"

    # datayı set eder
    @FullName.setter
    def FullName(self, parametre):
        ad, soyad = parametre.split(
            ' '
        )  # dışarıdan girilen ayrık 2 kelimeyi ad ve soyad değişkenine atama yapacak  "murat vuranok" girerse, ad = "murat" soyad = "vuranok" şeklinde çalışacak
        self.FirstName = ad
        self.LastName = soyad

    # datanın içerisini temizler
    @FullName.deleter
    def FullName(self):
        print("kişiye ait kayıt silindi")
        self.FirstName = None
        self.LastName = None


personel = Personel("Murat", "Vuranok")
print(personel.FirstName)
print(personel.LastName)
print(personel.email)
# mail bir metot olduğundan direkt olarak personel.email şeklinde çağırırsanız size sınıfın özelliklerini teslim eder.
# <bound method Personel.email of <__main__.Personel object at 0x7ff6a55f8e20>>

# eğer metot içerisindeki değeri almak istiyorsanız aşşağıdaki gibi çağırmanız gerekir.

print(personel.email())

# fakat biz mu metodu property gibi kullanmak istiyorsa, personel.email o zaman decore etmemiz gerekir. O yüzden sınıfın içerisinde birtane Mail metodu ekledik ve property olarak decore ettik<

print(personel.Mail)
print(personel.FullName)

personel.FullName = "Ahmet Şahin"
print(personel.FirstName)
print(personel.LastName)
print(personel.Mail)

# Ahmet
# Şahin
# ahmet.şahin@bilgeadam.com
del personel.FullName
print(personel.FullName)  # None None
