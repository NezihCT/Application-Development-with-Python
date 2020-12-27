# .index(), .rindex()

metin = "bilge adam beşiktaş şubesi"

# parametre verdiğiniz değerin, metin içerisinde yer alan index değerini teslim eder, metin içerisinde aynı karakter birden fazla içeriyorsa, ilk bulduğu değerin index numarasınız, eğer parametrede gönderdiğiniz değer metin içerisinde geçmiyorsa size, (ValueError: substring not found) değer teslim eder.
result = metin.index("a")
print(result)

sonuc = metin.rindex("a")
print(sonuc)


# metin içerisinde parameterede gönderilen değerin, birden fazla olup olmadığını kullanıcıya mesaj olarak dönen bir metot yazınız.
# metot içeriye metin ve parametre alacak, geriye str mesaj dönecek.


def Kontrol(metin, parametre):
    try:
        if(metin.index(parametre) == metin.rindex(parametre)):
            return f"parametrede gönderdiniz \"{parametre}\" değerin, parametrede gönderdiğiniz \"{metin}\" içerisinde 1 defa geçmektedir"
        else:
            return f"parametrede gönderdiniz \"{parametre}\" değerin, parametrede gönderdiğiniz \"{metin}\" içerisinde birden fazla geçmektedir"
    except ValueError:
        return f"parametrede gönderdiniz \"{parametre}\" değerin, parametrede gönderdiğiniz \"{metin}\" içerisinde geçmeketedir"


result = Kontrol("bilge adam beşiktaş şubesi", "a")
print(result)