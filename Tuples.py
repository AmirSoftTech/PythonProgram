# A tuple is a collection which is ordered and unchangeable.
# stusent[0]="Amir" is not possible to change the value.
student=(
    ("Mohammad", 10, 50.6, 100),
    "Amirul",
    "Islam",
    "Arian",
    "Islam",
    "Bangladesh"
)

print(student)
print("---------------------------------------------------------------------------")
for i in student:
    print(i, end=" ,")