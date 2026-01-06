import random

def jogo_de_advinhacao():
    numero = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de advinhação!")
    print("Tente advinhar um número de 1 a 100.")

    while True:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 3

        if palpite < numero:
            print("Palpite muito baixo. Tente novamente!")
        elif palpite > numero:
            print("Palpite muito alto. Tente novamente!")
        else:
            print(f"Parabéns!! Você acertou o número em {tentativas} tentativas.")
            break
jogo_de_advinhacao() 
