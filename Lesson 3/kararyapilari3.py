# kullanıcın dışarıdan girdiğin  sayının tek veya çift olma durumunu kontrol etme, 
# sayi tek ise, sayı tektir uyarısı 
# çift ise, sayı çifttir uyarısı veriniz.

try:
    sayi = int(input("Lütfen bir sayı giriniz : "))
    if(sayi % 2 == 0):
        print("Girilen sayı çifttir")
    else:
        print("Girilen sayı tektir")
except Exception as mahmud:
    print(mahmud)