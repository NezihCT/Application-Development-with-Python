# lower() => tüm metni küçük harfe çevirir
# upper() => tüm metni büyük harfe çevirir

metin = "bilge ADAM"
print(metin.lower())

print("-"*50)
print(metin.upper())

# islower()  => metin içerisinde yer alan tüm elemanlar küçük harf olup olmadığını kontrol eder,geriye True / False değeri teslim eder.


result = metin.lower().islower()


print(result)


result = metin.upper().isupper()
print(result)