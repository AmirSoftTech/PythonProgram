id = [101, 102, 103, 104, 105, 106]
name = ["Amirul Islam","Tania Islam", "Arian Islam", "Waliul Islam", "Tahmina Islam", "Tushar Islam"]
address = ["America", "USA", "Asia", "Japan", "Canada", "Australia"]

# id, name and address
x = list(zip(id, name, address))
for i in x:
    print(i)

print("-----------------------------------------------------------------------")

# id and name
y = list(zip("123456", id, name))
for j in y:
    print(j)

print("-----------------------------------------------------------------------")

# id and name
z = list(zip( "ABCDEF", id, name)) # id and name
for k in z:
    print(k)