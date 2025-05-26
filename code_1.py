import random
import os
print("                          |    |  _     _   _        _      ___  _")
print("                          | /\ | |_ |  |   | | |\/| |_       |  | |")
print("                          |/  \| |_ |_ |_  |_| |  | |_       |  |_|")
print("                   | |  _        _          _              __    _          _")
print("                   |_| |_| |\ | |  _  |\/| |_| |\ |       |  _  |_| |\  /| |_")
print("                   | | | | | \| |_| | |  | | | | \|       |_| | | | | \/ | |_")
print()
print()print("\033[1m      THERE ARE 3 LEVELS   \n LEVEL 1)SPORTS \n LEVEL 2)PLACES \n LEVEL 3)CHEMICAL NAMES\033[0m")
level=int(input("\033[1m      CHOOSE A LEVEL TO PLAY\n\033[0m"))

str1 = ""
l1=["javelin", "rugby", "soccer", "hockey", "archery","wrestling","gymnastics","boxing"]
l2=["berlin", "tokyo", "nairobi", "denver", "helsinki","moscow","bogota","stockholm"]
l3=["vitriol", "formaldehyde", "hexasulphur", "benzophenone", "naphthalene","phenolphthalein","acetophenone","icosane"]
l=[l1,l2,l3]
x = random.randint(0,len(l[level-1]))
chosen_word = (l[level-1])[x]


guess_word = ["_"] * len(chosen_word)
attempts = 7

hangman_images = [
    '''
     -----
     |   |
         |
         |
         |
         |
    -----|-----
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    -----|-----
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    -----|-----
    ''',
    '''
     -----
     |   |
     O   |
    \|   |
         |
         |
    -----|-----
    ''',
    '''
     -----
     |   |
     O   |
    \|/  |
         |
         |
    -----|-----
    ''',
    '''
     -----
     |   |
     O   |
    \|/  |
    /    |
         |
    -----|-----
    ''',
    '''
     -----
     |   |
     O   |
    \|/  |
    / \  |
    -----|-----
    ''',
    '''
     -----
     |   |
     O   |
    /|\  |
    / \  |
    -----|-----
    '''
]

print("You have 7 attempts.")
print("LET'S START THE GAME")
print("The word is:", len(chosen_word), "letters.")

while "".join(guess_word) != chosen_word and attempts > 0:
    print(" ".join(guess_word))
    print(hangman_images[7 - attempts])
    letter = input("Enter a letter: ").lower()

    if letter in chosen_word:
        print("Correct! You have", attempts, "attempts remaining.")
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                guess_word[i] = letter
    else:
        attempts -= 1
        print("Incorrect guess!")
        print("You have lost one attempt. Remaining attempts:", attempts)

    if "".join(guess_word) == chosen_word:
        print("Congratulations! You've guessed the word:", chosen_word)
        break

if attempts == 0 and "".join(guess_word) != chosen_word:
    print("You have failed to guess the word.")
    print("The word was:", chosen_word)



    