import random

#first we create list of characters that we would like to have in our progaram
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

#we take the number of characters the user would need.
num_letters = int(input("How many letters would you like in your password?"))
num_numbers = int(input("How many numbers would you like?"))
num_symbols = int(input("How many symbols would you like?"))

#we create a empty list to which we wil append characters as the the number of characters entered by the user
password = []
#password = "", also works 

for letter in range(num_letters):
    password.append(random.choice(letters))

for number in range(num_numbers):
    password.append(random.choice(numbers))

for symbol in range(num_symbols):
    password.append(random.choice(symbols))

#after the choosing a random number of element from the list of characters and appending it to password list, we shuffle the list password
random.shuffle(password)

#we print the charcter without any coma or colon or newline between them, as print by default adds newline character at the end of the printed text
for char in password:
    print(char, end='')
print('\n')

