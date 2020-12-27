# .set() => c#'dan görmediğiniz hatta merak edip bakmayacağınız HasSet, ödev bile versem bahane bulacağınız nesnemiz :) içerisinde uniq değer tutar, yani türkçe meali (aynı elemandan 2. bir eleman barınmaz, 3. barınmaz)

mySet = set()
 
print(mySet)
 
mySet.add(1)
mySet.add(2)
mySet.add(3)

print(len(mySet))
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(len(mySet))
print(mySet)


sayilar = []

sayi = 5

if not sayi in sayilar:
    sayilar.append(sayi)

print(sayilar)