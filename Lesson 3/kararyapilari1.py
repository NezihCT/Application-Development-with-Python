# Karar yapıları
# Karşılaştırma operatorleri

# == (eşit eşittir) soldaki değerin, sağdaki değere eşit olma durumu
#   1 == 1 => true  - if
#   1 == 2 => false - else

# != (eşit değildir) soldaki değerin, sağdaki değere eşit olmama durumu
#   1 != 1 => false - else
#   2 != 1 => true  - if

# >  (büyüktür) soldaki değerin, sağdaki değerden büyük olma durumu)
#   2 > 1  => true  - if
#   1 > 1  => false - else

# <  (küçüktür) soldaki değerin, sağdaki değerden küçük olma durumu)
#   1 < 2  => true  - if
#   2 < 1  => false - else

# >= (büyük veya eşit olma) soldaki değerin, sağdaki değerden, büyük veya eşit olma durumu
#   1 >= 1 => true - eşit olma - if
#   2 >= 1 => true - büyük olma - if
#   1 >= 2 => false - else

# <= (küçük veya eşit olma) soldaki değerin, sağdaki değerden, küçük veya eşit olma durumu
#   1 <= 1 => true - eşit olma - if
#   1 <= 5 => true - küçük olma - if
#   5 <= 1 => false - else


username = input("Lütfen kullanıcı adınızı giriniz : ")
username = username.lower()\
    .replace("ı", "i")\
    .replace("ç", "c")\
    .replace("ş", "s")\
    .replace("ö", "o")\
    .replace("ğ", "g")\
    .replace("ü", "u")


print(username)


if(username == "admin"):
    print("Tebrikler, giriş yaptınız")
else:
    print("Kullanıcı adınız yanlış")