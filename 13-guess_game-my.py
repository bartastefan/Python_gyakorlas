# Number guess game: you have 3 try
secret_number = 4  # set the number -could be random in the future
print("I'm thinking for a number between 0-9, you have 3 try.")
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess_count += 1
    guess_number = input("Enter a number! ")
    if secret_number != int(guess_number):
        print("It isn't the correct number.")
        print(f"You guessed {guess_count} times.")
    elif secret_number == int(guess_number):
        print("Congratulation! You find the correct number!")
        print(f"You guessed {guess_count} times.")
        break
else:
    print("Sorry, you didn't guess the correct number!")
    print(f"The correct number was:{secret_number}.")