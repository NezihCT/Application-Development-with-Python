# yaptığımız işlemin sonunda oluşan değeri geriye teslim almak istiyorsak, function kullanmalıyız.

# dışarıdan aldığı 2 sayının toplamını geriye teslim eden metot
def Hesapla(x, y):
    toplam = x + y

    # not => return anahtar kelimesinden sonra, herhagi bir kod bloğu çalışmaz...
    return toplam


sonuc = Hesapla(10, 3)
print(sonuc)

# bu alan içerisinde diğer hesaplamalar yapılacak
