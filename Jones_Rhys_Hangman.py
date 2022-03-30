
import random
from collections import Counter

with open("word_list.txt") as f:
        word_list = f.read().splitlines()

word = random.choice(word_list)		

if __name__ == '__main__':
        print('Please enter your next guess: ')
	
        for i in word:
                print('*', end = ' ')		
        print()

        playing = True
        guesses = ''
        totalguesses = ''
        lives = 7
        correct = 0
        flag = 0
        try:
                while (lives > 0) and flag == 0:
                        print()

                        try:
                                guess = str(input('Please enter your next guess: '))
                        except:
                                print('Only enter letters')
                                continue

                        if not guess.isalpha():
                                print('Only enter letter characters')
                                continue
                        elif len(guess) > 1:
                                print('Enter only one letter a ta time')
                                continue
                        elif guess in totalguesses:
                                print('You have guessed that already')
                                continue

                        if guess in word:
                                k = word.count(guess) 
                                for _ in range(k):	
                                        totalguesses += guess
                                        guesses += guess
                        else:
                                lives -=1
                                totalguesses +=guess

                        for char in word:
                                if char in guesses and (Counter(guesses) != Counter(word)):
                                        print(char, end = ' ')
                                        correct += 1
                                elif (Counter(guesses) == Counter(word)): 																# the game ends, even if chances remain
                                        print("The word is: ", end=' ')
                                        print(word)
                                        flag = 1
                                        print('Congratulations you win')
                                        break 
                                        break 
                                else:
                                        print('*', end = ' ')
			

                if lives <= 0 and (Counter(guesses) != Counter(word)):
                        print()
                        print('You lose')

        except KeyboardInterrupt:
                print()
                exit()
