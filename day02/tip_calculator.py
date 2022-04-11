#A tip calculator that also splits the bill for a party

print("Welcome to the tip calculator.")
bill = int(input('How much was the total bill?\n'))
people = int(input('How many people are you splitting the bill with?\n'))
tip = int(input('How much of a tip (in percent) would you like to give? (Just the number, no % symbol)\n'))

total = round(bill * (1 + tip/100), 2)
pay = round(total / people, 2)

print(f"The bill total is ${total}. Each person should pay ${pay}.")