#This program tell whether the number entered is even or odd
num = int(input("Enter a number to check wheter its odd or even: "))

remainder = num % 2

if remainder == 0:
    print("The number is even.")
else:
    print("The number is odd")

