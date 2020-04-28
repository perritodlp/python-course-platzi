# -*- coding: utf-8 -*-

class Lamp:
    # variable de clase
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    # self es la propia instancia, esto es un método de instancia
    # init es el constructor de la clase
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on # variable de instancia

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    # es un método privado, no queremos exponerlo
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])        

def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(input('''
           ¿Qué desea hacer?

           [p]render
           [a]pagar
           [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break        

if __name__ == '__main__':
    run()
