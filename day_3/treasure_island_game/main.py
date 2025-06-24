print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."'` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to Treasure Island Game.")
choice_1 = input("You are at a cross road, where you have to either go right of left:\n"
    "type 'left' to move towards left side or 'right' to move towards right side: ").lower()
if choice_1 == 'left':
    choice_2 = input("After walking for some time, you have reached the sea.\nThere is a Island some meters for from the shore\n"
                     "You either to swim towards it or wait for the boat\n"
                     "type 'wait' to wait for a boat or 'swim' to swim towards the Island: ").lower()
    if choice_2 == 'wait':
        print("you reached the Island unharmed.\nThere are three doors."
              "A yellow, a blue and a red door.")
        choice_3 = input("type 'red' to open red door, 'yellow' to open the yellow door or "
                          "'blue' to open the blue door: ").lower()
        if choice_3 == 'yellow':
            print("YOU HAVE FOUND THE TREASURE, CONGRATULATIONS!!")
        elif choice_3 == 'red':
            print("There is a lion behind the door, GAME OVER.")
        elif choice_3 == 'blue':
            print("There are dangerous bees behind the door, GAME OVER.")
    else:
        print("You wear eaten by sharks, GAME OVER!")
        
else:
    print("You fell in a deep hole, GAME OVER!") 
