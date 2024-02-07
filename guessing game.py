#guessing game
import random
print("Hello ,welcome")

remaining_attempts =4

while remaining_attempts > 0:
    lucky_number =int(input("enter a number between 1 and 20:"))
    random_number =random.randint(1,20)

    print("Random_number: ", random_number)

    if lucky_number == random_number:
        print("Hooray! You won")
        break
    else:
        print("Boo! Try again")
        remaining_attempts -= 1
        print(f"Remaining Attempts: {remaining_attempts}")

    if remaining_attempts == 0:
        print("Out of moves")
