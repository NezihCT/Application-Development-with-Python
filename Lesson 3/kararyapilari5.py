# mantıksal operatorler

# and sorguya katılan her bir koşulun sağlanması durumu
# or  sorguya katılan herhangi bir koşulun sağlanması durumu
# not sorguya olumsuzluk katar, değil ise

# username = input("Lütfen kullanıcı adınızı giriniz : ")
# if(username == "admin"):
#     password = input("Lütfen şifrenizi giriniz : ")
#     if password == "123456":
#         print("Giriş yaptınız")
#     else:
#         print("Kullanıcı bilgilerinizi kontrol ediniz")
# else:
#     print("Kullanıcı bilgilerinizi kontrol ediniz")


username = input("Lütfen kullanıcı adınızı giriniz : ")
password = input("Lütfen kullanıcı şifrenizi giriniz : ")

if username == "admin" and password == "123":
    print("Tebrikler giriş yaptınız")
else:
    print("Kullanıcı bilgilerinizi kontrol ediniz")