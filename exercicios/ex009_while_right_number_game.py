from random import randint

print("GAME: Try to guess the number from 1 to 10.")
computer = randint(1, 10)
attempts = 0

while True:
    player_number = int(input("Enter a number: "))
    attempts += 1
    if player_number == computer:
        print(
            f"You got it right! Your number was {player_number} and the computer number was {computer}."
        )
        break
    else:
        if player_number > computer:
            print("You got it wrong. The number is smaller. Try again.")
        if player_number < computer:
            print("You got it wrong. The number is bigger. Try again.")

print(f"You had {attempts} attempts to get it right.")
print("Program Completed.")
