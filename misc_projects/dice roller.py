# A basic script to roll dice based on the user's needs

import random

# Using while True: and try/except to force an integer input from the user
while True:
    try:
        sides = int(input("How many sides does the die have?\n"))
        dice_rolled = int(input("How many dice to roll?\n"))
        break

    except ValueError:
        print("Please insert an integer only.")
        continue

num_of_dice = dice_rolled
# If the integers are <= 0
if sides == 0:
    print("I can't roll 0-sided dice!")
elif sides < 0:
    print("Negative-sided dice don't exist!")
elif dice_rolled == 0:
    print("You have no dice to roll!")
elif dice_rolled < 0:
    print("I can't roll a negative number of dice!")
else:
    save = 0
    while num_of_dice > 0:
        roll = random.randint(1, sides)
        print(f"Rolled a {roll}")
        save += roll
        print(f"Current total: {save}")
        num_of_dice -= 1
    print(f"Rolled {dice_rolled}d{sides} with the result {save}")