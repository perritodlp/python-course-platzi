# -*- coding: utf-8 -*-

import turtle
import random

def hombre(seg,t):
    t.pendown()
    if seg == 1:
        t.circle(25)
        
    elif seg == 2:
        t.right(90)
        t.forward(100)
     
    elif seg == 3:
        t.right(45)
        t.forward(75)
        t.goto(0,100)
    elif seg == 4:
        t.left(90)
        t.forward(75)
        t.penup()
        t.goto(0,150)
    elif seg == 5:
        t.left(45)
        t.forward(50)
        t.goto(0,150)
    elif seg == 6:
        t.left(180)
        t.forward(50)





def run(t):
    words = ['arroz', 'amarillo','amor','altar','as','ave','avestrus','antro','azul','atomico','beso','baston','brea','britanico','becerro','bote','blanco','brasalete','brazo','bar','casa','centavo','cianuro','coco','cuerpo','calabaza','cerro','cinturon','col','cruz','dado','dragon','dos','diente','doctor','doce','duende','dardo','desde','donde','efe','eres','elefante','entero','feo','frente','fase','futbol','frase','frio','gato','gas','gel','gol','hola','hielo','haz','iglesia','juez','londres']
    num = len(words) - 1
    x =  random.randint(0,num)
    w_found = False
    w = words[x]
    word = w
    lon = len(w)
  
    y = '_'
    string = ''
    print('Adivina la palabra de {} letras'.format(lon))
    for i in range(1,lon+1):
        string = string + y

    print(string) 
    seg = 0 
    while not w_found:

       y = str(input('¿Cual letra o palabra das?  '))
       if len(y) == 1: ### una letra
           if w.find(y) == -1:
               print('LETRA EQUIVOCADA')
               print('')
               print('')
               print('Adivina la palabra de {} letras'.format(lon))
               print(string)
               seg = seg + 1
               if seg >6:
                   print('GAME OVER')
                   w_found = True
               else:    
                    hombre(seg,t)


               ####aqui va el codigo de dibujo ####
           else:
                
                cont = w.find(y)
                print('')
                print('Adivina la palabra de {} letras'.format(lon))
                string = list(string)
                w = list(w)
                for i in range(0,lon):
                    if i == cont:
                        string [i] = y

                string = ''.join(string)        
                print(string)
                w[cont] = '_'
                w = ''.join(w)   
       else:
           if y == word:
               w_found = True
               print('E N H O R A B U E N A  H A S  E N C O N T R A D O  L A  P A L A B R A')
           else:
               print('PALABRA EQUIVOCADA')
               print('')
               print('')
               print('Adivina la palabra de {} letras'.format(lon))
               print(string)
               seg = seg + 1
               if seg > 6:
                   print('GAME OVER')
                   w_found = True
               else:
                   hombre(seg,t)


       if string.find('_') == -1:
           w_found = True
           print('E N H O R A B U E N A  H A S  E N C O N T R A D O  L A  P A L A B R A')
         










if __name__ == "__main__":
    print('A H O R C A D O')
    print('')
    window = turtle.Screen()
    t =  turtle.Turtle()
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.pensize(5)
    t.forward(100)
    t.penup()
    t.goto(-150,0)
    t.pendown()
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.penup()
    t.left(90)
    t.goto(0,200)
    
    t.pensize(1)
    run(t)