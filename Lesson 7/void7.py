# dışarıdan girilen metin içerisinde yer alan sesli ve sessiz harflerin toplamını kullanıcıya bildiriniz.

def SesliKontrol(mahmud):
    sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'u', 'ö', 'u']
    liste = list(mahmud.lower())
    sesli = 0
    sessiz = 0
    for i in liste:
        if i in sesli_harfler:
            sesli += 1
        else:
            sessiz += 1

    print(
        f"metin içerisinde yer alan, sesli harflerin toplam sayısı  : {sesli}")

    print(
        f"metin içerisinde yer alan, sessiz harflerin toplam sayısı : {sessiz}")


SesliKontrol("akdşkasdşkwqoASAAAAeğqwei")
