# sistema de adivinhaçao
# -*- coding: utf-8 -*-
from time import sleep
from random import randint

print("-#"*16)
print("Bem vindo ao jogo de adivinhação")
print("-#"*16)

sair = False

while sair == False:
    print("Menu:")
    print("Digite 1 para Jogar.")
    print("Digite 2 para saber seu saldo.")
    print("Digite 3 para sair.")
    opcao =int(input("Digite sua opção: "))

    if opcao == 1:
        print("01001011.if..lorem ipsum...")
        sleep(0.8)
        print("Ops.. digo")
        sleep(0.7)
        print("Lets play :)")
        valor=float(input("Digite o valor que quer apostar: "))
        sleep(0.7)
        print("-#" * 20)
        print("Regras:")
        print("1. para cada acerto se ganha 5 reais.")
        print("2. para cada erro se perde 5 reais.")
        print("3. penso em um número de 0 a 20")
        print("-#" * 20)
        sleep(1)
        parar = False
        while parar == False :
            print("Vamos la humano,")
            print("Pensando...")
            sleep(2)
            computador = randint(0, 20)

            dica = input("Quer receber uma dica?(s/n)")
            if dica == "s":
                if computador >= 0 and computador <= 10:
                    print("O meu número esta entre 1 e 10.")
                if computador >= 11 and computador <= 20:
                    print("O meu número esta entre 11 e 20.")

            numero = float(input("Digite seu número: "))
            sleep(1)
            if numero == computador:
                print(f"Parabéns você acertou, o meu número foi o {computador}")
                ganho = valor + 5
                print(f"você ganhou 5 reais, e seu saldo agora é: {ganho}")
                valor = ganho
                sleep(2)
            else:
                print("Que pena humano, você errou")
                print(f"O meu número escolhido foi {computador}")
                perca = valor - 5
                print(f"Você perdeu 5 reais, e seu saldo agora é: {perca}")
                sleep(2)
                valor = perca


            print("Deseja apostar novamente? (s/n)")
            jogo = input("Digite: ")
            if valor <= 0:
                 parar = True
                 print("Voce ficou sem dinheiro, voltando ao menu...")

            if jogo == "n":
                parar = True
                sleep(1)
                print("Voltado ao menu...")

    if opcao == 2:
        print(f"Seu saldo e: {valor:.2f}")
        sleep(1)


    if opcao == 3:
        sair = True
        print("Tudo bem, volte logo...")

