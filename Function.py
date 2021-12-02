#Function
def Addition(x, y):
    add = x+y
    return add # return value

def Subtraction(x,y):
    sub = x-y
    print("Subtraction: ",sub)

def Multiplication(x, y):
    mul = x*y
    print("Multiplication: ", mul)

def Division(x,y):
    div = x/y
    print("Division: ", div)

def Remainder(x,y):
    rem = x % y
    print("Remainder: ", rem)

a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))

print("-----------------------------------------------")

result = Addition(a, b)
print("Addition: ", result)

Subtraction(a, b)
Multiplication(a, b)
Division(a, b)
Remainder(a,b)
