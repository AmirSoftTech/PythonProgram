#Recursion function
def fact(n): # Calculate factorial
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
n = int(input("Enter value for n :"))
result = fact(n)
print("Factorial of", n ,"is : ",result)
