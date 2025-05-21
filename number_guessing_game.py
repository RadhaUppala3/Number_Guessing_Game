import random
number_to_guess = random.randint(1, 100)
chance = 6
while chance > 0:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > number_to_guess:
            print("Too high")
        elif guess < number_to_guess:
            print("Too low")
        else:
            print("Congratulations, you guessed the number!")
    except ValueError:
        print("Please enter a valid number")

    chance -= 1
else:
    print(f"You failed!, The correct number is {number_to_guess}")