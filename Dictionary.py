studentId = {
    100: "Amir",
    101: "Islam",
    102: "Zohra",
    102: "Nazrul",
    103: "Bangladesh"
}

for i,j in studentId.items():
    print(i, ":", j)

print("----------------------------------------")
studentId[102]="Islam" # Change name "Islam" inplace of "Nazrul"
for i,j in studentId.items():
    print(i, ":", j)

print("----------------------------------------")
#Add new item 104 in to the list
studentId.update({
    104: "red"
})
for i,j in studentId.items():
    print(i, ":", j)
print("----------------------------------------")

studentId.pop(104) # Remove item 104 from the list
for i,j in studentId.items():
    print(i, ":", j)

#studentId.clear()# Empty the list

