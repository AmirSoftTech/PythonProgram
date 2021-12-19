#Polymorphism, here we can see same method but different behaviour
#https://www.geeksforgeeks.org/polymorphism-in-python/?ref=lbp
def add(a, b, c=0, d=0):
    return a + b + c + d

# Driver code
print("Result from two parameters: ",add(2,2))
print("Result from three parameters: ",add(2, 2, 2))
print("Result from four parameters: ",add(2, 2, 2))

print("-----------------------------------------------------")

class Bird:
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.flight()
obj_spr.flight()
obj_ost.flight()