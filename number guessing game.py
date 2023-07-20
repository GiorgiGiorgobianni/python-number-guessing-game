import random
guesses = 10
num = (random.randint(1, 100))





while guesses <= 10:
    answer = int(input("guess the number: "))

    if answer == num:
        print("YOU WON")
        break


    elif answer > num:
        guesses = guesses -1
        print("guess guess lower. you have " + str(guesses) + " tries left")

    elif answer < num:
        guesses = guesses - 1
        print("guess higher. you have " + str(guesses) + " tries left")




    if guesses == 0:
        print("you lost")
        break


