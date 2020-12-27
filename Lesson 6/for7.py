myList1 = [1, 2, 3]
myList2 = ["a", "b", "c"]


print(zip(myList1, myList2))

for item in zip(myList1, myList2):
    print(item)

myList1 = [1, 2, 3, 4, 5]
myList2 = ['a', 'b', 'c', 'd']
myList3 = [100, 200, 300, 400]

for item in zip(myList1, myList2, myList3):
    print(item)
