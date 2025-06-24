weight = int(input("Enter your weight in Kgs: "))
height = int(input("Enter your height in Cms: "))

bmi = round((weight/(height ** 2))*(10 ** 4), 2)

if bmi < 16:
    print(f"BMI is Severe Thinness, with {bmi}")
elif 16 <= bmi < 17:
    print(f"BMI is Moderate Thinness, with of {bmi}")
elif 17 <= bmi < 18.5:
    print(f"BMI is Mild Thinness, with {bmi}")
elif 25 <= bmi < 30:
    print(f"BMI is Overweight, with {bmi}")
elif 30 <= bmi < 35:
    print(f"BMI is overweight class I, with {bmi}")
elif 35 <= bmi < 40:
    print(f"BMI is Overweight class II, with {bmi}")
elif bmi >= 40:
    print(f"BMI is Overweight class III, with {bmi}")
else:
    print(f"BMI is normal, with {bmi}")

