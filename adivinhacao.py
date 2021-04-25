import random


def jogar():
    print('************* *** **************')
    print('Bem vindo ao jogo de Adivinhação')
    print('************* *** **************')

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print('Escolha o nível de dificuldade:')
    print('(1) Fácil  (2) Médio  (3) Difícil')

    nivel = int(input())

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada:02d} de {total_de_tentativas:02d}')
        chute = int(input('Digite o seu numero entre 1 a 50: '))

        if chute < 1 or chute > 100:
            print('você deve digitar um valor entre 1 e 50')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f'você acertou e fez {pontos} pontos!')
            break
        else:
            if maior:
                print('seu chute foi maior que o número secreto!', end="\n \n")
            elif menor:
                print('seu chute foi menor que o número secreto!', end="\n \n")
            pontos = pontos - abs(numero_secreto - chute)

    print('Fim do jogo')


if __name__ == '__main__':
    jogar()
