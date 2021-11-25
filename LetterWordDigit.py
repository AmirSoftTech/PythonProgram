numberofletters = 0
numberofwords = 0
numberofdigits =0
value = input("Enter value for letter count:")

for i in value:
    ch = i.lower()
    if ch>='a' and ch<='z':
        numberofletters= numberofletters+1
    elif ch>='0' and ch<='9':
        numberofdigits = numberofdigits + 1

    elif ch ==' ':
        numberofwords = numberofwords + 1

print("------------------------------------------")
print("Number of letters: ",numberofletters)
print("Number of words:",numberofwords)
print("number of digits",numberofdigits)
