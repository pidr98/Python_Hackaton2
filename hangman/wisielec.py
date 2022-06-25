import random
from ludek import display_hangman

def get_word():
    animals = ['cat', 'dog', 'bird']
    fruit = ['orange', 'banana', 'apple']
    word_animals = random.choice(animals)
    word_fruit = random.choice(fruit)
    question_type = int(input('Choose category: 0 = animals, 1 = fruit: '))

    if question_type == 0:
        word = word_animals
    else:
        word = word_fruit

    return word.lower()


def game(word):

    guessed = False
    guessed_letters = []
    word_progress = '_' * len(word)
    tries = 6

    print('--------------Start--------------')
    print(f'Word to guess: {word_progress}')

    while not guessed and tries > 0:
        guess = input('Input a guess: ').lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'Already guessed this letter {guess}', )
                if guess not in guessed_letters:
                    guessed_letters += guess
                else:
                    print(f'Guessed letters: {guessed_letters}')
            elif guess not in word:
                print(f'-{guess}- not in the word')
                tries -= 1
                print(f'Tries left: {tries}')
                if guess not in guessed_letters:
                    guessed_letters += guess
                    print(f'Guessed letters: {guessed_letters}')
            else:
                print(f'You guessed right!, -{guess}- is in the word!')
                guessed_letters += guess

                word_to_list = list(word_progress)
                if guess not in guessed_letters:
                    guessed_letters += guess
                else:
                    print(f'Guessed letters: {guessed_letters}')
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexes:
                    word_to_list[index] = guess
                word_progress = "".join(word_to_list)
                if "_" not in word_progress:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess not in word:
                print(f'{guess} is not the word.')
                tries -= 1
                print(f'Tries left: {tries}')
                if guess not in guessed_letters:
                    guessed_letters += guess
                    print(f'Guessed letters: {guessed_letters}')
            else:
                guessed = True
                word_progress = word
        else:
            print('Wrong input')
        print(display_hangman(tries))
        print(word_progress)


    if guessed:
        print('You found the word!')
    else:
        print(f'You lost, the word was:{word}')


def main():
    word = get_word()
    game(word)

main()