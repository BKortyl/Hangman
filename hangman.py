import random


def menu():
    while True:
        x = input('Type "play" to play the game, "exit" to quit: ')
        if x == 'exit':
            quit()
        elif x == 'play':
            break


file = open('words.txt', 'r')
raw_words = list(file)
words = []
file.close()
for word in raw_words:
    words.append(word.rstrip())
print('H A N G M A N')
menu()
correct_word = random.choice(words)
correct_set = set(correct_word)
lives = 30
current_state = '-' * len(correct_word)
attempted_letters = set()
while lives > 0:
    print()
    print(current_state)
    letter = input('Input a letter: ')
    if letter in attempted_letters:
        print("You've already guessed this letter")
    elif len(letter) != 1:
        print('You should input a single letter')
    elif not letter.islower():
        print('Please enter a lowercase English letter')
    else:
        if letter in correct_set:
            attempted_letters.add(letter)
            new_state = ''
            for character, hidden in zip(correct_word, current_state):
                if letter == character:
                    new_state += letter
                else:
                    new_state += hidden
            current_state = new_state
        else:
            attempted_letters.add(letter)
            lives -= 1
            print("That letter doesn't appear in the word")
        if lives == 0:
            print('You lost!')
            print()
            menu()
        if '-' not in current_state:
            print('You guessed the word!')
            print('You survived!')
            print()
            menu()
