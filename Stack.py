#Stack list in firt out
books = []
books.append("1. Learn C")
books.append("2. Learn C++")
books.append("3. Learn Java")
books.append("4. Learn Python")
books.reverse()
for i in books:
    print(i)

print("--------------------------")

for x in range(2): # how many times you will pop
    books.reverse()
    books.pop()
    books.reverse()

for i in books:
    print("Now the top book is : ",i)

if not books:
    print("No book left")


