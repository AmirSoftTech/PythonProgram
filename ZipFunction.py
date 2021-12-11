id = [101, 102, 103, 104, 105, 106]
name = ["Amirul Islam","Tania Islam", "Arian Islam", "Waliul Islam", "Tahmina Islam", "Tushar Islam"]

x = list(zip(id, name))
for i in x:
    print(i)

print("-----------------------------------------------------------------------")

y = list(zip("123456", id, name))
for j in y:
    print(j)

print("-----------------------------------------------------------------------")

z = list(zip( "ABCDEF", id, name))
for k in z:
    print(k)