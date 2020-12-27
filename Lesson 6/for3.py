# Kullanıcının dışarıdan girdiği metni alt alta yazdırınız

metin = input("lütfen gereksiz bir metin giriniz : ")


result = ""

for elma in metin:
    # print(elma)
    result += " "+elma
print(result)