#this program is used to calculate tip for the bill received
print("Welcome to tip calculator!")
bill = float(input("What is the total bill? Rs."))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

tip_amount = bill*tip /100  
total_amount = bill + tip_amount
per_head_cost = total_amount /no_of_people

print(f"Each person has to pay Rs.{round(per_head_cost, 2)}")

