import os


def decorator_metot(func):
    def sarmal_metot():
        os.system("Clear")
        # print("sarmal metodu : {}'dan önce tetiklendi".format(func.__name__))
        return func()
    return sarmal_metot


print("sdasdsa")


@decorator_metot
def print_metot():
    print("print_metot tetiklendi")


print_metot()