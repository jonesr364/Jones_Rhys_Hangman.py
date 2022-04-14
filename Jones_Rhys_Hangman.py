# (JCS) Module 3: python
# Completed by Rhys Jones

import random
from collections import Counter

# import word list document
with open("word_list.txt") as f:
        word_list = f.read().splitlines()

word = random.choice(word_list)		

if __name__ == '__main__':
        print('Please enter your next guess: ')

	#Print spaces for letters in word
        for i in word:
                print('*', end = ' ')		
        print()

        playing = True
        #store letter guesses found in word
        guesses = ''
        # store all the guessed letters
        totalguesses = ''
        lives = 7
        correct = 0
        flag = 0
        try:
                while (lives > 0) and flag == 0: #flag updates when word is completed
                        print()

                        try:
                                userguess = str(input('Please enter your next guess: '))
                                guess = userguess.lower()
                        except:
                                print('Only enter letters')
                                continue

                        #validate the character entered
                        if not guess.isalpha():
                                print('Only enter letter characters')
                                continue
                        elif len(guess) > 1:
                                print('Enter only one letter a ta time')
                                continue
                        elif guess in totalguesses:
                                print('You have guessed that already')
                                continue

                        # if the letter guessed is in the word
                        if guess in word:
                                k = word.count(guess) # k stores the number of times the letter appears in the word
                                for _ in range(k):	
                                        totalguesses += guess #Add the letter to the bank of guessed letters
                                        guesses += guess #The guessed letter is added to the word
                        # if the letter is guessed is not in the word
                        else:
                                lives -=1 # Remove a life for incorrectly guessing
                                totalguesses +=guess # Add the letter to the bank of guessed letters
                                print('Incorrect Guess. Lives left: ', end=' ')
                                print(lives)

                        # Print the word
                        for char in word:
                                if char in guesses and (Counter(guesses) != Counter(word)):
                                        print(char, end = ' ')
                                        correct += 1
                                #If all letters have been guessed
                                elif (Counter(guesses) == Counter(word)): 																# the game ends, even if chances remain
                                        print('The word is: ', end=' ')
                                        print(word)
                                        flag = 1
                                        print('Congratulations you win')
                                        break # Break for loop
                                        break # break while loop
                                else:
                                        print('*', end = ' ')
			
                # When the user runs of of lives
                if lives <= 0 and (Counter(guesses) != Counter(word)):
                        print()
                        print('You lose')
                        print("The word was: ", end=' ')
                        print(word)

        except KeyboardInterrupt:
                print()
                exit()
