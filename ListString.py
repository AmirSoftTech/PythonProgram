n = input("Enter value:")# 10 20 30 40 50
list = n.split()# 10, 20, 30, 40, 50
print(list)

sum = 0
for i in list:
    sum = sum + int(i)
print("Total number of sum value:", sum)