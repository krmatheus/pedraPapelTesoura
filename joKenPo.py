from random import randint
from time import sleep
list = ('pedra', 'papel', 'tesoura')
com = randint(0,2)
print('''suas opçoes:
[0] pedra
[1] papel
[2] tesoura''')
you = int(input('qual sua jogada? '))
print('='*22)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!!!')
sleep(2)
print(f'o computador escolheu {list[com]}')
print(f'voce escolheu {you}')
print('='*22)
if com == 0:
    if you == 0:
        print('empatou kkk, tenta de novo')      
    elif you == 1:
        print('voce venceu!! as maquinas foram dilaceradas')
    elif you == 2: 
        print('voce perdeu!! as maquinas vao dominar o mundo')
    else:
        print('JOGADA INVÁLIDA')
elif com == 1:
    if you == 0:
        print('voce perdeu!! as maquinas vao dominar o mundo')      
    elif you == 1:
        print('empatou kkk, tenta de novo')
    elif you == 2: 
        print('voce venceu!! as maquinas foram dilaceradas')
    else:
        print('JOGADA INVÁLIDA')
elif com== 2:   
    if you == 0:
        print('voce venceu!! as maquinas foram dilaceradas')      
    elif you == 1:
        print('voce perdeu!! as maquinas vao dominar o mundo')
    elif you == 2: 
        print('empatou kkk, tenta de novo')
    else:
        print('JOGADA INVÁLIDA')        