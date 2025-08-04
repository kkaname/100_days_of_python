#first we import important modules
import random
import hangman_art
from hangman_words import word_list     

print("*************************************************************************************************")
#importing the logo from hangman_art module and printing it to make the code cleaner
print(hangman_art.logo)

num_life = 6

choosen_word = random.choice(word_list)
#making a array of blank character, with as same length as the choosen word
placeholder = []
for position in range(len(choosen_word)):
    placeholder.append('_')

print("Word to guess:", end='')
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
        print(hangman_art.life[6 - num_life])
        print(f"Wrong guess, the letter '{guess_letter}', is not in the word!")
        print(f"***********************************LIVES-->({num_life}/6)****************************************")
    
    #used to print the updated placeholder array
    for blank in placeholder:
        print(blank, end='')
    print("\n")

    #if all the words are guessed, i.e., all the blanks are filled and there is no blank left, makes the game over and the player has won the game
    if "_" not in placeholder:
        game_over = True
        print("******************************YOU GUESED THE WORD RIGHT, YOU WIN!!!******************************")
    if(num_life == 0):
        print(f"******************************THE WORD WAS '{choosen_word}', YOU LOOSE*****************************")          


