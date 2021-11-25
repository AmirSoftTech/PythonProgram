for x in range(3):

    ch = str(input("Enter value to check vowel or consonant:"))
    ch = ch.lower()#To vonvert upper case value into lower case

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("The letter is vowel.")

    elif ch.isdigit():
        print("This is number of digit.")

    else:
        print("The letter is consonant.")
