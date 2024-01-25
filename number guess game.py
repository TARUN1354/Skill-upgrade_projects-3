import random

def number_guessing_game():
    number = random.randint(1, 100)
    guess = -1
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("Congratulations! You guessed the correct number!")

if __name__ == "__main__":
    number_guessing_game()
