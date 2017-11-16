# coding=UTF-8

from adivinhacao import jogar_adivinhacao
from forca import jogar_forca

if (__name__ == "__main__"):
    while (True):
        resposta = input("Qual o jogo escolhido? Digite 1 para Adivinhação e 2 para a Forca: ")
        try:
            x = int(resposta)
            if (x in [1,2]):
                break
            else:
                print("Digite um número entre 1 e 2.")
        except:
            print("Digite um número entre 1 e 2.")
    if (resposta == "1"):
        print ("Você escolheu o jogo de Adivinhação, tenha um bom jogo!")
        jogar_adivinhacao()
    if (resposta == "2"):
        print ("Você escolheu o jogo de Forca, tenha um bom jogo!")
        jogar_forca()