import random


def prepare_word_list():
    words = []
    with open('words.txt', 'r') as file:
        raw_words = list(file)
        for word in raw_words:
            words.append(word.rstrip())
    return words


def menu():
    while True:
        x = input('Type "play" to play the game, "exit" to quit: ')
        if x == 'exit':
            quit()
        elif x == 'play':
            play()


def play():
    correct_word = random.choice(prepare_word_list())
    correct_set = set(correct_word)
    lives = 10  # change to manipulate difficulty of the game
    current_state = '-' * len(correct_word)
    attempted_letters = set()
    while lives > 0:
        print()
        print(current_state)
        print(f'Lives left: {lives}')
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
                print(f'The correct word: {correct_word}')
                print()
                menu()
            if '-' not in current_state:
                print('You guessed the word!')
                print('You survived!')
                print()
                menu()


def main():
    print('H A N G M A N')
    menu()


if __name__ == '__main__':
    main()
