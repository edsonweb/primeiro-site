import random

numero = random.randint(1, 100)
tentativas = 0

print('bem vindo ao jogo de adivinhação!')
print('eu escolhi um numero entre 1 e 100. Voce tem 10 tentativas para adivinhar.')

while tentativas < 10:
    palpite = int(input('digite seu palpite:'))
    tentativas += 1

    if palpite == numero:
        print(f'parabens! voce acertou o numero em {tentativas} tentativas.')
        break 
    elif palpite < numero :
        print('o numero é maior. tente novamente.')
    else:
        print(' o numero é menor . tente novamente.')
else:
    print(f'voce perdeu! o numero era{numero}.')
