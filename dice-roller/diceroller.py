import random
print("Welcome to the Dice Roller and Streak tracker!\n")
print("Press Enter to roll the die or type 'q' to quit.\n")

previous_roll = None
streak = 0

while True: 
    roll_input = input("Roll the dice: ")

    if roll_input.lower() == 'q':
        print("Cya thanks for playing!")
        break

    # Generate random number between 1 and 6
    current_roll = random.randint(1, 6)
    print(f"You rolled a {current_roll}")

    # Track streak
    if current_roll == previous_roll:
        streak += 1
        print(f"Streak! Rolled {current_roll} {streak +1} times in a row!")
    else:
        streak = 0

    previous_roll = current_roll
