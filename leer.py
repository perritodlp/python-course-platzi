# -*- coding: utf-8 -*-

def run():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} veces en el texto'.format(counter))        


        #print(f.readlines()) readlines() crea una lista con cada línea del archivo

if __name__ == '__main__':
    run()