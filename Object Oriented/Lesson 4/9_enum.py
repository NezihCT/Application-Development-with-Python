from enum import Enum


class Durum(Enum):
    Mutlu = 1
    Uzgun = 2

    def describe(self):
        return self.name, self.value

    def __str__(self):
        return f"şuanki ruh halim, dıgıdık dıgıdık gidiyor ama {self.name}"

    def __repr__(self):
        return "Ruh haliniz = " + self.name

    @classmethod
    def favori_durum(cls):
        return cls.Uzgun


print(Durum.favori_durum())
print(Durum.Uzgun.describe())
print(Durum.Mutlu)
print(repr(Durum.Mutlu))
