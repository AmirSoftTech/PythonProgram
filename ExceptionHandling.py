# Try .... Except
try :
    num1 = int(input("Enter value : "))
    num2 = int(input("Enter value : "))
    result = num1 / num2
    print(result)

except (ValueError, ZeroDivisionError):
    print("You have entered an incorrect value!")

finally:
    print("Thanks!!")

#Type Error
'''
try:
    number = int(input("Enter value : "))
    result = 20/ number
    print(result)
except TypeError:
    print("TypeError, need to convert input value into integer!")
print("Successflly done!")
'''

#ZeroDivision Error
'''
try:
    number = int(input("Enter value : "))
    result = 20/ number
    print(result)
except ZeroDivisionError:
    print("Dividing by zero is not possible")
print("Successflly done!")
'''

#Index Error
'''
try:
    list = [20, 0, 30]
    result = list[0]/list[4]
    print(result)
    print("Done")
except IndexError:
    print("Index Error")
print("successful")
'''

#finally keyword
'''
try:
    list = [20, 0, 30]
    result = list[0]/list[4]
    print(result)
except ZeroDivisionError:
    print("Index Error")
finally:
    print("successfully done!")
'''


#Raise Keyword

'''
def voter(age):
    if age<18:
        raise ValueError("You are not allowed to vote!")
    return  "You are allowed to vote!"

try:
    n = int(input("Enter value : "))
    x = voter(n)
    print(x)
except  ValueError as e:
    print(e)
'''