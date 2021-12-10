#Map function
def square(x):
    return x * x

num = [1,2,3,4,5]
result = list(map(square, num))
print("Map function square number: ",result)

print("-------------------------------------------------")

#Filter function
num = [1, 2 , 3 , 4, 5, 6, 7, 8, 9, 10]
evenNumber = list(filter(lambda x: x%2==0, num))

print("Filter function even number : ", evenNumber)
oddNumber = list(filter(lambda x: x%2==1, num))
print("Filter function odd number : ", oddNumber)