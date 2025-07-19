import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" 

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

comp_choice = random.randint(0, 2)
user_choice = int(input("Enter a number: 0 - 'rock', 1 - 'paper' or 2 - scissors. "))

#print user's choice
if(user_choice == 0):
    print(f"You chose: rock{rock}")
elif(user_choice == 1):
    print(f"You chose: paper{paper}")
elif(user_choice == 2):
    print(f"You chose: scissor{scissors}")

#print computer's choice
if(comp_choice == 0):
    print(f"computer chose:rock{rock}")
elif(comp_choice == 1):
    print(f"computer chose: paper{paper}")
elif(comp_choice == 2):
    print(f"computer chose: scissor{scissors}")

if(comp_choice == user_choice):
    print("Its a Draw.")
elif(comp_choice == 0 and user_choice == 1):
    print("You win.")
elif(comp_choice == 1 and user_choice == 2):
    print("You win.")
elif(comp_choice == 2 and user_choice == 0):
    print("You win")
else:
    print("You loose.")

