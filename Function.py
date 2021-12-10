#Function
def Addition(x, y):
    add = x+y
    return add # return value

def Subtraction(x,y):
    sub = x-y
    return sub # return value

def Multiplication(x, y):
    mul = x*y # not return value
    print("Multiplication: ", mul)

def Division(x,y):
    div = x/y # not return value
    print("Division: ", div)

def Remainder(x,y):
    rem = x % y # not return value
    print("Remainder: ", rem)

#Enter input value
x = int(input("Enter value for a:"))
y = int(input("Enter value for b:"))

print("-----------------------------------------------")

result = Addition(x, y)
print("Addition: ", result)

result = Subtraction(x, y)
print("Subtraction: ",result)

Multiplication(x, y)
Division(x, y)
Remainder(x, y)
