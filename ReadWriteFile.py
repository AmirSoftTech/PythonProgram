file = open("ReadFile.txt", "r")
x = file.read()
print(x)
file.close()

'''
file = open("ReadFile.txt", "r")
x = file.readlines()
for i in x:
    print(i)
file.close()
'''

'''
file = open("ReadFile.txt", "a") # To add new line with existing line
x = file.write("\nThis is a new readable file")
print(x)
file.close()
#Out put :
#This is a first readable file
#This is a second readable file
#This is a third readable file
#This is a new readable file
'''

'''
file = open("ReadFile.txt", "w") # To overwrite with exitig lines 
x = file.write("\nThis is a new readable file")
print(x)
file.close()
'''

'''
file = open("ReadFile1.txt", "w")# To create new file
x = file.read()
print(x)
file.close()
'''