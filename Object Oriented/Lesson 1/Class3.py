class Student:
    """
    self : sınıf içerisinde yer alan metotlarıni diğerlerinden farkı hangi sınıd içerisinde çalıştığını belirtmesidir.Self anahtar kelimesini vererek metodun bu sınıf içerisinde çalıştığını belirtmiş oluruz. Tanımlama yapılırken eklenir fakat kullanım sırasında python bunu bizim için kendisi yapacaktır
    """

    FirstName = ""

    def GiveNot(self, student):
        print(student,  "Adlı öğrenciye not girişi yapıldı")

    def GivePunish(self, student):
        print(student, "Adlı öğrenciye ceza verildi")

    def Check(self, student):
        print(student, "Adlı öğrencinin yoklaması girildi")


student = Student()
student.FirstName = "Murat"

student.Check(student.FirstName)


Student.Check("", "murat vuranok")