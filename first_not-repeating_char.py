# -*- coding: utf-8 -*-

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    # 3233045297 Claro

    # "abacabad"
    # {
    #     'a': (0, 4),
    #     'b': (1, 2),
    #     'c': (3, 1)
    # }        

    final_letters = []

    for key, value in seen_letters.iteritems():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )  # "abacabad" [('a', 0), ('d', 7)]      

    # Otra forma de ver lo que hace la función lambda
    # def sort_order(value):
    #     return value[1]

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))    