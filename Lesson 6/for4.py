# Kullanıcı dışarıdan şifre girecek, girilen şifre 3 ile 8 karakter aralığında ise, şifreniz : şifre olarak onaylandı

# abc123 => şifreniz : abc123 olarak onaylandı

# kullanıcı 3 denemenin sonuda beceremezse, motive edici bir mesaj veriniz :)

for i in range(3):  # başlangıç değeri vermezseniz, default olarak 0'dan başlayacaktır
    password = input("Lütfen 3 ile 8 aralığında bir şifre seçiniz : ")
    if i == 2:
        print("Şifrenizi 3 defa yanlış girdiniz, bu iyi bişey")
    elif not password:
        print("şifre oluşturabilmen için, klavyede tuşa basman gerekli")
    # elif len(password) >= 3 and len(password) <= 8:
    #     pass
    elif len(password) in range(3, 8):  # şifre uzunluğu bu 2 değer aralığında ise
        print(f"Şükürler olsun,\nŞifreniz : { password} olarak belirlenmiştir")
        break # break anahtar kelimesi, bağlı bulunduğu yapıyı sonlandırır, derlendiği anda döngüyü sonlandıracaktır