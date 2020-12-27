from Helpers import Clear


class Employee:

    FirstName = ""
    LastName = ""
    Mail = ""

    def CreateMail(self):
        self.Mail = Clear.ClearString(
            f"{self.FirstName}.{self.LastName}@bilgeadam.com")


class EmployeeService:

    def IseAll(self):
        pass
