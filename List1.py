# List example 1:
'''
list = ["Mohammad", "Amirul", "Islam"]
sum = ""
for x in range(len(list)):
    print(list[x], end=" ")

'''
# List example 2:
list = ["Mohammad", "Amirul", "Islam", "Natore","Rajshahi", "Bangladesh"]
for x in list:
    print(x, end=" ")

print("\n------------------------------------------------")
print(list)
print(list[2:]) # Show out put from ----"Islam", "Natore","Rajshahi", "Bangladesh"
print(list[-2:])# Show out put from last two ---- "Rajshahi", "Bangladesh"
print(list[2:5])#Show put put from --------"Islam", "Natore","Rajshahi"
print("Islam" in list) # True
print("Islam" not in list) # False
print("Raza" in list) # False
print("Raza" not in list) # True
print(list + ["Raza", 30]) # Add two values----- Raza, 30
