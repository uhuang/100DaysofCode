print("Welcome to the rollercoaster! You must be at least 120 cm to ride.")
while True:
    try:
        height = int(input("What is your height in cm? "))
        break
    except ValueError:
        print("Please type in an integer.")

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you are too short to ride the rollercoaster.")