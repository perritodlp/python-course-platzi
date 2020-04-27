# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

def populations():
    seguir = True

    while seguir:
        country = str(raw_input('Escribe el nombre de un país: ')).lower()

        if country == 'x':
            seguir = False

        try:
            print('La población de {} es: {} millones'.format(country, countries[country]))
        except KeyError:
            print('No tenemos el dato de la población de {}'.format(country))
        else:
            print('resultado exitoso')
        finally:
            print('Ingrese el nombre del país o la letra x para salir.')            

if __name__ == '__main__':
    print('Poblaciones de algunos países')

    populations()