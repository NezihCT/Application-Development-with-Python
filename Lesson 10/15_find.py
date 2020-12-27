# .find(), .rfind() => aradığınız elemanın index değerini teslim eder, eğer dizi veya metin içerisinde aradığınız değer birden fazla ise, .find() ilk bulduğu elemanı, rfind() son bulduğu elemanı teslim eder. dizi içerisinde eğer aradığız eleman yok ise, size -1 değerin teslim eder


# index meto ile çalışma prensibi aynıdır fark => index ValueError verirken, find metodu -1 değeri teslim eder, parameterdeki eleman içermiyorsa


metin = "bilge adam beşiktaş şubesi"

result = metin.find("a")  # 6
print(result)

result = metin.rfind("a")  # 17
print(result)

result = metin.find("x")  # -1
print(result)

result = metin.rfind("x")  # -1
print(result)