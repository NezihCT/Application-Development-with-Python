# Örnek : Dışarıdan girilen kelimenin uzunluğu, 8 karaktere eşit veya uzunsa, parola onaylandı, 
# kısa ise, daha uzun bir şifre seçiniz uyarısı verdiriniz

password = input("Lütfen yeni şifre giriniz : ")

if len(password) < 8:
    print("Lütfen daha uzun bir şifre seçiniz")
else:
    print("Tebrikler, yeni şifre oluşturdunuz")