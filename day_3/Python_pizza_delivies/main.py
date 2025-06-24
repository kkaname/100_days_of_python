print("Welcome to Python Pizza Delivery!")
choice = input("Would you like to order a pizza? Y for Yes and N for No: ").lower()
bill = 0
if choice == 'y':
    size = input("What is the size of the pizza you would like to have? s-small, m-medium and l-large: ").lower()
    if size == 's':
        charges = 3
    else:
        charges = 4
        if size == 's':
            bill += 199
        elif size == 'm':
            bill += 299
        else:
            bill += 399
    peperoni = input("Do you want peperonni? Y for yes and N for No: ")
    if peperoni == 'y':
        bill += charges*10 + 30
    cheese = input("Do You want extra cheese? Y for yes and N for no:")
    if cheese == 'y':
        bill += charges*10

    print(f"your choice is:\npizza = {size}\npeperonni = {peperoni}\nextra cheese = {cheese}\nThe total bill is Rs.{bill}/-")


else:
    print("OK! No problem. but make sure whenever you crave for pizza, we are just one call away, so please do call out store.")
