# coding=UTF-8

import random

def pegar_palavra():
	lista_de_palavras = []
	with open("palavras.txt", "r", encoding="UTF-8") as myFile:
		for line in myFile:
			linha = line.split()
			if len(linha) != 0:
				lista_de_palavras.append(linha[0])
	numero = random.randrange(0, len(lista_de_palavras))
	return lista_de_palavras[numero]

def pegar_chute():
    while (True):
        chute = input("Digite seu chute: ")
        if len(chute) < 1 or len(chute) > 1:
            print("Chute apenas um caractere! Seu tapado!")
            continue
        else:
            break
    return chute.upper().split()[0]

def comparar_chute(chute, palavra_secreta):
    lista_palvra_secreta = list(palavra_secreta)
    pos = 0
    posicoes = []
    for caractere in lista_palvra_secreta:
        if chute == caractere.upper():
            posicoes.append(pos)
        pos += 1
    return {chute : posicoes}

def desenhar_palavra(palavra_secreta, lista_de_acerto):
    lista_a_imprimir = []
    numero_de_caracteres = len(palavra_secreta)
    for elemento in range(0, numero_de_caracteres):
        ancora = False
        for letra in list(lista_de_acerto.keys()):
            posicoes_de_acertos = lista_de_acerto[letra]
            if elemento in posicoes_de_acertos:
                lista_a_imprimir.append(letra)
                ancora = True
        if ancora == False:
            lista_a_imprimir.append("_")
    for caractere_a_imprimir in lista_a_imprimir:
        print(caractere_a_imprimir, end=' ')
    print('', end='\n')
    if "_" in lista_a_imprimir:
        return True
    else:
        return False

def desenhar_boneco(erro):
    print ("Você já teve {} erros!".format(erro))
    print ("     +--------+")
    print ("     |        |")
    if (erro > 0):
        print("     O        |")
    else:
        print("              |")
    if (erro == 2):
        print("     |        |")
    elif (erro == 3):
        print("    /|        |")
    elif (erro > 3):
        print("    /|\       |")
    else:
        print("              |")
    if (erro > 5):
        print ("     |        |")
    else:
        print("              |")
    if (erro == 6):
        print ("    /         |")
    elif (erro >= 7):
        print("    / \       |")
    else:
        print("              |")
    print ("              |")
    print (" ________________")
    print (" ________________", end="\n\n")


def jogar_forca():
    palavra_secreta = pegar_palavra()
    lista_de_acerto = {}
    condicao = desenhar_palavra(palavra_secreta, lista_de_acerto)
    erros = 0
    while (condicao == True):
        desenhar_boneco(erros)
        x = pegar_chute()
        print(palavra_secreta)
        comparado = comparar_chute(x, palavra_secreta)
        if len(list(comparado.values())[0]) != 0:
            lista_de_acerto.update(comparado)
        else:
            erros += 1
        condicao = desenhar_palavra(palavra_secreta, lista_de_acerto)
        if (erros > 7):
            print("Você perdeu! LOSER!!!!!!!!!!!")
            exit(0)



