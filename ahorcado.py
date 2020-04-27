# -*- coding: utf-8 -*-

import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        ========='''
]

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)

    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * ---')  
    print('')  

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    letter_used = []

    while True:
        display_board(hidden_word, tries)

        if( len(letter_used) ):
            print('Haz usado las letras: ')
            print(" ".join(letter_used))    

        print('')
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []

        if current_letter == ' ':
            print('')
            print('No ingresaste ninguna letra')

        elif len(current_letter) > 1:
            print('')
            print('Ingresaste más de una letra')

        else:
            try:
                letter_used.index(current_letter)
                display_board(hidden_word, tries)
                print('')
                print('La letra {} ya fue usada!'.format(current_letter))
                print('')

            except ValueError:
                letter_used.append(current_letter)

                for idx in range(len(word)):
                    if word[idx]== current_letter:
                        letter_indexes.append(idx)

                if len(letter_indexes) == 0:
                    tries += 1

                    if tries == 7:
                        display_board(hidden_word, tries)
                        print('')
                        print('¡Perdiste! La palabra correcta era {}'.format(word))
                        break;
                else:
                    for idx in letter_indexes:
                        hidden_word[idx] = current_letter

                    letter_indexes = []

                try:
                    hidden_word.index('-')
                except ValueError:
                    print('')
                    print('¡Felicidades ganaste! La palabra es: {}'.format(word))
                    break;

if __name__ == "__main__":
    print('BIENVENIDOS A AHORCADOS')
    run()