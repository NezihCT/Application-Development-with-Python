word = "bilgeadam"

for item in word:
    print(item)

print("-"*30)

for item in enumerate(word):
    print(item)
# (0, 'b')
# (1, 'i')
# (2, 'l')
# (3, 'g')
# (4, 'e')
# (5, 'a')
# (6, 'd')
# (7, 'a')
# (8, 'm')

for (key, value) in enumerate(word):
    print(key)
    print(value)
    print("\n")
