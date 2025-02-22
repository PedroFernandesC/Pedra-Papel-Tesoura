import random

print("Olá, vamos jogar Pedra, Papel e Tesoura?")

opcoes = ["Pedra", "Papel", "Tesoura"]
computador = random.choice(opcoes)

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

SuaEscolha = input("Qual sua jogada? -> ").lower()

if SuaEscolha == "pedra":
    print(pedra)
elif SuaEscolha == "papel":
    print(papel)
elif SuaEscolha == "tesoura":
    print(tesoura)
else:
    print("A opção que você escolheu não existe. Tente novamente!")

print("Escolha da máquina:")

if computador == "Tesoura":
    print(tesoura)
elif computador == "Pedra":
    print(pedra)
elif computador == "Papel":
    print(papel)
else:
    print("Não foi possível determinar a jogada. Tente novamente.")

# Resultado
print("Resultado da partida:")
# Condições da Pedra
if SuaEscolha == "pedra" and computador == "Papel":
    print("Você perdeu!")
elif SuaEscolha == "pedra" and computador == "Tesoura":
    print("Você ganhou!")
elif SuaEscolha == "pedra" and computador == "Pedra":
    print("Empate!")
# Condições da Tesoura
elif SuaEscolha == "tesoura" and computador == "Tesoura":
    print("Empate!")
elif SuaEscolha == "tesoura" and computador == "Papel":
    print("Você ganhou!")
elif SuaEscolha == "tesoura" and computador == "Pedra":
    print("Você perdeu!")
# Condições do Papel
elif SuaEscolha == "papel" and computador == "Tesoura":
    print("Você perdeu!")
elif SuaEscolha == "papel" and computador == "Pedra":
    print("Você ganhou!")
elif SuaEscolha == "papel" and computador == "Papel":
    print("Empate!")
else:
    print("Jogada inválida. Por favor, tente novamente.")