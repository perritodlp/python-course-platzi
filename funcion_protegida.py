# -*- coding: utf-8 -*-

# Qué es un decorador
# A, B y C son funciones
# A recibe como parámetro a B para poder crear C
# protected() es A que recibe a protected_func que es B, para poder crear wrapper() que es C

def protected(func): # A recibe a B como parámetro

    def wrapper(password): # Para crear una nueva función C

        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta.')

    return wrapper


@protected # Definimos el decorador
def protected_func():  # B
    print('Tu contraseña es correcta.')

if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contraseña: '))

    # Forma 1
    #wrapper = protected(protected_func)

    #wrapper(password)

    protected_func(password)