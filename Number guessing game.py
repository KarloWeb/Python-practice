import random


low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True



while is_running:


    guess = input(f"Guess a number from {low} to {high}: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("Guess is out of range, try again. ")
            guess = input(f"Guess a number from {low} to {high}: ")

        elif guess < answer:
            print("You guessed lower, try again. ")

        elif guess > answer:
            print("You guessed higher, try again. ")

        else:
            print("You are correct! ")
            print(f"Number of guesses: {guesses}")

            is_running = False