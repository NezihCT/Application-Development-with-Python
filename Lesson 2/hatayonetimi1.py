# Programcı hataları (Error)
# Program kusurları
# İstisnai hatalar
# Mantıksal hatalar


# telefonNumarasi = int(input("Lütfen telefon numaranızı giriniz : "))
# print("Tebrikler, hayatta birkez bile olsa başarı sağladın!")


try:
    telefonNo = int(input("Lütfen telefon numaranızı giriniz : "))
    print("tebrikler")

except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("İşlem hatası")
