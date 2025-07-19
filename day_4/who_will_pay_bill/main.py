import random

friends = ["Mike", "Sam", "Daniel", "Mark", "Nik", "Huang", "Alice", "Bob", "david", "Emanuel"]

choice = random.choice(friends)

print(f"The one who will pay the bill is: {choice}.")

#Alternate:
#num = random.int(0, len(friends) - 1)
#print --> friends[num]

