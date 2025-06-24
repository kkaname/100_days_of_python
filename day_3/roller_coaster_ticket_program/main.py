print("Heyy!! Welcome to the Roller Coaster ride.")
height = int(input("What is you height in cm: "))
amount = 0

if height >= 120:
    print("You are eligible to ride the Roller Coaster.")
    age = int(input("What is your age: "))
    choice = input("Do you want the regular ticket for a ride or ticket or unlimited ride, R for regular, U for unlimited: ").lower()
    if choice == 'r':
        if age < 18:
            amount += 149
        elif 18 <= age < 60:
            amount += 299
        else:
            amount += 199

    else:
        if age < 18:
            amount += 899
        elif 18<= age < 60:
            amount += 1299
        else:
            amount += 999

    photo_choice = input("Do you need photos? Y for Yes and N for No: ").lower()
    if photo_choice == 'y':
        amount += 100

    print(f"The total cost of you ticket is Rs.{amount}/-")

else:
    print("Sorry, but you have to grow taller in order to ride the Roller Coaster.")

