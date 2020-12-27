try:
    sayi = int(input("Lütfen sadece sayısal değer giriniz : "))
    print("gelen sayı :", sayi)
    sayi = sayi / 0
    print("İşlem sonucu")
except ValueError as mahmud:
    print("Lütfen tekrar deneyiniz")
    print("Sistem mesajı :", mahmud)
except Exception as elma:
    print("işlem hatası")
    print("Sistem mesajı :", elma)
