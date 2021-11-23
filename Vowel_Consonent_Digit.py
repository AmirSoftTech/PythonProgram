for x in range(3):

    ch = str(input("Enter value to check vowel or consonant:"))

    if ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U':
        print("The letter is vowel.")

    elif ch.isdigit():
        print("This is number of digit.")

    else:
        print("The letter is consonant.")
