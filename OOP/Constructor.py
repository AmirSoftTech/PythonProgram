#Constructor
class Student:
    roll = ""
    gpa = ""
    address=""

    def __init__(self, roll, gpa, address):
        self.roll= roll
        self.gpa= gpa
        self.address = address

    def display(self):
        print("Roll:", self.roll)
        print("Gpa:", self.gpa)
        print("Address:", self.address)

print("Rahim's Result")
rahim = Student(100, 3.89, "Dhaka")
rahim.display()

print("------------------------")

print("Karim's Result")
Karim = Student(200, 3.59, "Rajshahi")
Karim.display()

print("------------------------")

print("Abdul's Result")
Abdul = Student(300, 3.79, "Khulna")
Abdul.display()