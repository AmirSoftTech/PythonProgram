from random import randint

n = int(input("How many times you want to play the game?:"))

for i in range(n+1):
    print("----------------------------------------------------")
    print(i+1,". Number of try.")
    guessNumber = int(input("Enter your gessing number:"))
    randomNUmber = randint(1,5)

    if guessNumber==randomNUmber:
        print("You have won and your gessing number was:", guessNumber)
        break

    else:
        print("You have lost and your gessing number was:", randomNUmber)
