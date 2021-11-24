# n = 5
'''
n = int(input("Enter value:"))
for i in range(n+1):
    print(i * "* ")
# output :
*
* *
* * *
* * * *
* * * * *
'''

# n = 5
n = int(input("Enter value:"))
for i in range(n+1):
    print((2*i-1) * " *")

'''
#Output
 *
 * * *
 * * * * *
 * * * * * * *
 * * * * * * * * *
'''