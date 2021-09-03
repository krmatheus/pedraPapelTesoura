from random import randint
com = randint(0,50)
print('Falo em nome das máquinas e te desafio a adivinhar o numero que acabei de pensar')
print('Tem culhões pra me vencer?')
acertou = False
palpites = 0
while not acertou:
    you = int(input('Qual seu palpite? '))
    palpites += 1
    if you == com:
        acertou = True
    else:
        if you < com:
            print('Mais que isso, tente novamente')
        elif you > com:
            print('Menos que isso, tente novamente')
print(f'Acertou com {palpites} tentativas')                    