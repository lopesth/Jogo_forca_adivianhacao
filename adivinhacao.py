# coding=UTF-8

import random

def boas_vindas():
    print("****************************************")
    print("*** Bem vindo ao jogo de adivinhação ***")
    print("****************************************")
    print("\nVamos jogar!\n")

def entrada_do_usuario():
    return input("Digite o número: ")

def testar_se_numero(valor):
    try:
        int(valor)
        return True
    except:
        return False

def testar_segredo(chute_dado, segredo):
    if (chute_dado == segredo):
        return {True : " "}
    else:
        if (chute_dado > segredo):
            return {False : "maior"}
        else:
            return {False : "menor"}

def criar_numero_secredo(valor_inicial, valor_final):
    return random.randrange(valor_inicial, valor_final)

def jogando(numero_secredo):
    teste_numero = False
    while(teste_numero == False):
        chute_raw = entrada_do_usuario()
        teste_numero = testar_se_numero(chute_raw)
    chute = int(chute_raw)
    print("Você chutou o número {:d}".format(chute))
    return testar_segredo(chute, numero_secredo)

def dificuldade_safadao():
    while (True):
        resposta = input("Qual a dificuldade desejada? Digite 1 para fácil, 2 para médio, 3 para difícil: ")
        try:
            x = int(resposta)
            if (x in [1, 2, 3]):
                print("Você digitou o número {}" .format(resposta))
                break
            else:
                print("Você digitou fora do intervalo!")
        except:
            print("Você digitou uma letra, seu Safadinho!")
    if (resposta == "1"):
        print("Você escolheu o nível Fácil! Intervalo 0 a 10 em 8 tentativas")
        return {8: [0, 10]}
    if (resposta == "2"):
        print("Você escolheu o nível Médio! Intervalo 0 a 100 em 5 tentativas")
        return {5: [0, 100]}
    if (resposta == "3"):
        print("Você escolheu o nível Difícil! Intervalo 0 a 1000 em 1 tentativas")
        return {1: [0, 1000]}

def jogar_adivinhacao():
    boas_vindas()
    nivel = dificuldade_safadao()
    total_de_chances = list(nivel.keys())[0]
    x_i = list(nivel.values())[0][0]
    x_ii = list(nivel.values())[0][1]
    numero_secredo = criar_numero_secredo(x_i, x_ii)
    pontos = 1000
    continuidade = False
    contador_de_jogadas = 0
    while(continuidade == False):
        contador_de_jogadas += 1
        total_de_chances -= 1
        continuidade_dic = jogando(numero_secredo)
        continuidade = list(continuidade_dic.keys())[0]
        diferenca = list(continuidade_dic.values())[0]
        if (continuidade == False):
            print("Seu chute foi {} do que o número secreto!" .format(diferenca))
            pontos -= 100
        if (total_de_chances == 0):
            print("Você perdeu!")
            break
        if (continuidade == True):
            print("Você Ganhou!!!! Você teve {} pontos" .format(pontos))
    print("Jogo acabou em {:d} rodadas!".format(contador_de_jogadas))
