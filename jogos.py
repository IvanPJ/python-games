import forca
import adivinhacao


def escolhe_jogo():
    print('************* *** **************')
    print('** *** Escolha o seu Jogo *** **')
    print('************* *** **************')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input())

    if jogo == 1:
        print("\n" * 130)
        print('Jogando Forca')
        forca.jogar()
    elif jogo == 2:
        print("\n" * 130)
        print('Jogando Adivinhação')
        adivinhacao.jogar()


if __name__ == '__main__':
    escolhe_jogo()
