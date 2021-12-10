def student(*details): #xxargs and xxxargs
    print(details)
student(100, "Amir")
student(100, "Amir", 30)
student(100, "Amir", 40, "Mohammad")

'''
def student(**details):
    print(details)
    print(details["name"])

student(id=10, name="Amir")
'''

'''
def student(*details):
    sum = 0
    for i in details:
        sum = sum +i
    print(sum)

student(10, 20)
student(10,20,30)
student(10,20,30,40)
'''



