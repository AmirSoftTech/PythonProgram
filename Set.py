num1 ={1, 2, 3, 4, 5}
num2 = set([4, 5, 6, 7, 8, 9, 10])

num1.add(6)#Add new data 6
print(num1)
num1.remove(6)#Remove new data 6
print(num1)
print(num1 | num2)#union set
print(num1 & num2)#Intersection set
print(num1-num2)