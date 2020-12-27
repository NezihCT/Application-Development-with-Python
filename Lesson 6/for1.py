sehirler = ["adana", "urfa", "bursa", "antep", "hatay"]

i = 0
while i < len(sehirler):
    sehir = sehirler[i]
    print(sehir)

    i += 1

print("-"*50)
# new String('-',50)


for sehir in sehirler:
    print(sehir)
    print('-')
print("-"*50)

print("-".join(sehirler)) # adana-urfa-bursa-antep-hatay