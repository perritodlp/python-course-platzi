# -*- coding: utf-8 -*-

def run():
    with open('numeros.txt','w') as f:
        for i in range(10):
            f.write(str(i))

    # Si no usamos el operador de contexto with, tenemos que usar el try
    # try:
    #     f = open()
    # finally:
    #     f.close()    


if __name__ == '__main__':
    run()