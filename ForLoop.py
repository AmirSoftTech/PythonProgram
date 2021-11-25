'''
#Sum value of forloop
# 1 + 2 + 3 + --------- + n
sum = 0
n = int(input("Enter value:"))

for i in range(1,n+1):
    print(i)
    sum = sum + i
print("----------------------")
print("Total sum value:", sum)
'''

'''
#Sum value of forloop
# 2 + 4 + 6 + --------- + n
#Even number value print and sum
sum = 0
n = int(input("Enter value:"))
for i in range(1,n+1):

    if i%2 == 0:
        print(i)
        sum = sum + i

print("----------------------")
print("Total sum value:", sum)
'''

#Sum value of forloop
# 1 + 3 + 5 + --------- + n
#Even number value print and sum
sum = 0
n = int(input("Enter value:"))
for i in range(1,n+1):

    if i%2 == 1:
        print(i)
        sum = sum + i

print("----------------------")
print("Total sum value:", sum)