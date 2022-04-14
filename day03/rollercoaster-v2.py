print("Welcome to the rollercoaster! You must be at least 120 cm to ride.")
while True:
    try:
        height = int(input("What is your height in cm? "))
        age = int(input("What is your age? "))
        break
    except ValueError:
        print("Please type in an integer.")

if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Your ticket will be $5")
    elif age <= 18:
        print("Your ticket will be $7")
    else:
        print("Your ticket will be $12")
else:
    print("Sorry, you are too short to ride the rollercoaster.")