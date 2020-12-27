import os


class Clear:
    def ClearScreen(self):
        os.system(self)
        print("Ekran Temizlendi")

    def ClearString(self):
        arg = self.lower().replace("ş", "s").replace(" ", "")
        return arg


class MathLibrary:
    def Topla(self, *arg):
        toplam = 0
        for i in arg:
            toplam += i
        return toplam
