import random
from time import sleep


def jogar_jokenpô():
    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        #Jogada do usuário
        print("Bem vindo ao Jokenpô!")
        sleep(1)
        jogada_user = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar o jogo): ")

        if jogada_user == "sair":
            print("Obrigada por jogar!!")
            break
        elif jogada_user not in opcoes:
            print("Jogada Inválida. Por favor, escolha uma das opções (pedra, papel ou papel)")
            continue

            

        #Jogada do computador
        jogada_computer = random.choice(opcoes)

        print(f"Você escolheu {jogada_user}")
        print(f"E o computador escolheu {jogada_computer}")

        #Define o ganhador
        if jogada_user == jogada_computer:
            print("Empate!!")
        elif((jogada_user == "pedra" and jogada_computer == "tesoura")
             or (jogada_user == "papel" and jogada_computer == "pedra")
             or (jogada_user == "tesoura" and jogada_computer == "papel")):
            print(f"Você venceu!!")
        else:
            print("Você perdeu!")

jogar_jokenpô()