# dışarıdan gelecek olan parametre sayısı belirsiz olan durumlarm için kullanılan metot tekniği
# C# => params anahtar kelimesine karşılık gelir.

def Hesapla(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam


result = Hesapla(1, 2, 3, 4, 5, 6, 78, 8, 9)
print("toplama işlemi sonucu", result)