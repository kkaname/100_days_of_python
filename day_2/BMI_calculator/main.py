#This program calculates the BMI of the patient
print("Welcome to BMI calculator!")
weight = int(input("Enter you weight in kg: "))
height = float(input("Enter you height in meter: "))
bmi = weight/(height ** 2)
print(f"Your BMI is {round(bmi, 2)}")

