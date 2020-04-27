# -*- coding: utf-8 -*-

def recursive_sum(sum, start):
    go = True

    while go:
        if start == True:
            message = 'Ingresa el primer entero a sumar o la letra x para salir: '
            start = False
        else:    
            message = 'Ingresa el valor entero para sumar o la letra x para salir: '

        option = input(message)

        if type(option) == str and option == 'x':
            go = False
        else:   
            try:
                sum = int(option) + sum
                print('La suma va en: {}'.format(sum))

                return recursive_sum(sum, start)

            except ValueError:
                print('Se produjo un error. No tenemos el dato de la suma, ya que lo ingresado no es un entero.')

if __name__ == '__main__':
    print('*** SUMANDO RECURSIVAMENTE ***')
    recursive_sum(0, True)