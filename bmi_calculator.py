# BMI Calculator in Python

# 1. Get user input
print("Welcome to the BMI Calculator!")
weight_kg = float(input("Please enter your weight in kilograms: "))
height_m = float(input("Please enter your height in meters: "))

# 2. Calculate BMI
bmi = weight_kg / (height_m ** 2)
# Alternatively: bmi = weight_kg / (height_m * height_m)

# 3. Determine the category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

# 4. Display the result
# The :.2f formats the BMI to 2 decimal places
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
