# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight)/(int(height)^2)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}. You are a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}. You are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}. You are obese.")
else:
    print(f"Your BMI is {bmi}. You are clinically obese.")