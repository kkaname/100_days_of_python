import random
#r""" --> means raw string, i.e., it tells python not to see blackslashs as escape sequence
#this below here, is called 'manual indexing using variables'
life = {
    1: r"""   +---+
   |   |
   O   |
       |
       |
       |
 =========""",

    2: r"""   +---+
   |   |
   O   |
   |   |
       |
       |
 =========""",

    3: r"""   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========""",

    4: r"""   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========""",

    5: r"""   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========""",

    6: r"""   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 ========="""
}

print("***********************************************************************")
print('''Welcome to, 
 _                                                
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ ' / _` | '_ ' / _` | '_ ` _ ' / _` | '_ ' 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|'__,_|_| |_|'__, |_| |_| |_|'__,_|_| |_|  GAME
                    __/ |                      
                   |___/    
      +---+
      |   |
          |
          |
          |
          |
    =========

''')

num_life = 6

#defineing a list of words from which a word will be choosen in random and is asked the user to guess the letter from the same word
word_list = ['apple', 'house', 'chair' 'tiger', 'water',  'bread',  'smile',  'green', 'pizza',  'music', 'jungle',  'planet', 'ladder', 'pillow',  'guitar',  'castle' ,'window',  'doctor', 'rocket' 'tunnel', 'labyrinth', 'zephyr',  'phoenix',  'cryptic',  'knapsack',  'bewilder',  'drought',  'avalanche',  'quadrant',  'mystique']

choosen_word = random.choice(word_list)
print("Word to guess:", end='')
#making a array of blank character, with as same length as the choosen word
placeholder = []
for position in range(len(choosen_word)):
    placeholder.append('_')
for blank in placeholder:
    print(blank, end='')
print("\n")

#this game_over will be used to check whether all the blank of the word is filled correctly or not
game_over = False

while(not game_over and num_life > 0):
    letter_present = 0
    guess_letter = (input("Guess a letter: ")[0]).lower()
    for letter in choosen_word:
        if letter == guess_letter:
            letter_present = 1
            #this enumerate returns all the indices of occurance of mentioned char in the string which is much better than the inder() 
            #enumerate(choosen_word) gives each character with its index.
            #The if filters only the characters that match guess_letter.
            #It collects their indexes into the list indices.
            indices = [i for i, char in enumerate(choosen_word) if char == guess_letter]
            for index in indices:
                placeholder[index] = letter


    if(letter_present == 0):
        #if the guess letter is not in the choosen word, it is a wrong letter
        num_life -= 1
        print(life[6 - num_life])
        print("Wrong guess!")
        print(f"*************************lives-->({num_life}/6)*************************")
    
    #used to print the updated placeholder array
    for blank in placeholder:
        print(blank, end='')
    print("\n")

    #if all the words are guessed, i.e., all the blanks are filled and there is no blank left, makes the game over and the player has won the game
    if "_" not in placeholder:
        game_over = True
        print("YOU HAVE GUESSED ALL THE LETTERS CORRECTLY, YOU WON!!")
    if(num_life == 0):
        print(f"AAHHOHHH! YOU FAILED TO GUESS THE LETTERS.\nTHE WORD WAS ==> {choosen_word}.\nAND RAN OUT OF YOUR CHANCES, LOST!!")


