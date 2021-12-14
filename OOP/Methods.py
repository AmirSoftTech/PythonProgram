'''
class Student:
    roll = ""
    gpa = ""

    def display(self):
        print("Roll :", self.roll)
        print("Gpa :", self.gpa)

rahim = Student()
print("Rahim's Result.")
rahim.roll = 1
rahim.gpa = 3.78
rahim.display()

print("------------------------------------------------------")

print("Karim's Result.")
karim = Student()
karim.roll = 2
karim.gpa = 3.59
karim.display()

'''
class Student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll= roll
        self.gpa= gpa

    def display(self):
        print("Roll :", self.roll)
        print("Gpa :", self.gpa)

rahim = Student()
print("Rahim's Result.")
rahim.set_value(1, 3.89)
rahim.display()

print("------------------------------------------------------")

print("Karim's Result.")
karim = Student()
karim.set_value(2, 3.79)
karim.display()

