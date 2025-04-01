import random
from time import sleep

#Função para sortear números aleatórios
def sorteia(min, max):
    sort = random.randint(int(min),int(max))
    return sort

#Função que compara o número que o usuário inseriu como entrada e o número que foi sorteado.
def compara(num_jg, num_sort):
    if num_jg > num_sort:
        print("Errou! Tente um número menor!")
        resultado = False
    elif num_jg == num_sort:
        print("Acertou!! Esse é o número")
        resultado = True
    elif num_jg < num_sort:
        print("Errou! Tente um número maior!")
        resultado = False 
    return resultado

#Introdução do jogo
print("Olá, seja bem vindo(a) ao Chute o Número!!")
sleep(1)
player = input("Qual seu nome? ")
print(f"Prazer em conhecer {player}")
sleep(1)

#Laço de repetição para rodar o jogo em loop
play = True
while play == True:
    print("Deseja jogar Chute o Número??")
    sleep(1)
    print("Sim = (1)")
    print("Não = (2)")
    resp = int(input("Qual sua resposta? "))
    #Condição para que o usuário possa jogar
    if resp == 1:
        print("Um número de 1 a 100 será sorteado, vc tem a missão de adivinhá-lo")
        sleep(1)
        print("Vc tem 10 tentativas, de acordo com os acertos vc ganha pontos!")
        sleep(1)
        print("Vamos começar!!")
        sorteado = int(sorteia(1,10))
        print("Agora tente adivinhar")
        comparacao = False
        point_rod = 10 

        #Laço de repetição para comparar e contar a pontuação
        while comparacao == False:
            resp_num = int(input("Qual seu chute? "))
            comparacao = compara(resp_num, sorteado)
            if comparacao == False and point_rod > 0:
                point_rod = point_rod-1
            elif comparacao == False and point_rod == 0:
                print("Infelizmente vc não conseguiu em 10 tentativas, tente novamente!")
                sleep(1)
            elif comparacao == True and point_rod > 0:
                pontuacao =+ point_rod
                print(f"Parabéns!! Vc acertou, vc ganhou {point_rod} pontos nessa rodada. A sua pontuação geral é de {pontuacao}")

    #Condição para sair do jogo
    elif resp == 2:
        play = False
        print(f"OK! Volte logo {player}")
    #Condição caso haja uma opção inválida
    else:
        print("Opção Inválida! Tente novamente")

    




