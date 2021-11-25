# List example to add and remove extra value with the list
list = ["Mohammad", "Amirul", "Islam", "Natore","Rajshahi", "Bangladesh"]
#list = [20, 10, 5, 1,8, 100,500]
print("Actual data:",list)
#list.sort()
list.reverse()
print("sorted data:",list)
print("Total number of list:",len(list))

print("------------------------------------------------------------------------")

#list.append("Computer Science")
#list.insert(2,"Computer Science")
list.remove("Rajshahi")
print(list)
print("After removing the total number of list data:",len(list))


'''
list = [100,10,30,500,80,40,60]
print("Actual data:",list)

list.sort()
print("Sorted data:", list)

list.pop()
list.pop()
print(list)

list.clear()
print(list)
'''
'''
subjects = [10,50,130,60,80, 40,70,500,10,20,10]

#sub = subjects[2] # return index value
sub = subjects.count(10)
print(sub)
'''