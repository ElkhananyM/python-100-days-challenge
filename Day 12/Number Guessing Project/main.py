import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
num = random.choice(range(101))
print(f"Shouldn't see this {num}")
diff = input("Choose a difficulty. Types 'easy' for 5 attempts and 'hard' for 10: ").lower()
if diff == 'hard':
    attempts = 5
else:
    attempts = 10

def guessed_num():
    print(f"You have {attempts} remaining to guess the number.")
    try:
        u_guess = int(input("Make a guess: "))
        return u_guess
    except ValueError:
        print("Invalid input. Please enter a valid number")

while attempts > 0:
    guess = guessed_num()
    if type(guess) == int:
        if guess == num:
            print(f"You got it! The answer was {guess}")
            break
        elif guess > num:
            print("Too high")
        else:
            print("Too low")
        attempts -= 1

if attempts == 0:
    print(f"You ran out of attempts! The correct guess was {num}")

