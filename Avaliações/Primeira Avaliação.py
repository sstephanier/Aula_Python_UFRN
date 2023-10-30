# Faça um algoritmo em Python que leia três valores, depois informa na tela qual deles é o maior, qual deles é o menor ou se são iguais. [2,5]

a = 30
b = 24
c = 45

maior = a
menor = a

if b > maior :
  maior = b
if c > maior:
  maior = c
if b < menor:
  menor = b
if c < menor:
  menor = c

print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")

#Faça um algoritmo em Python que implementa uma calculadora básica com as quatro operações, mais três operações especiais da sua escolha.
#O usuário do programa sempre que usar deve informar qual operação deseja realizar. [2,5]

import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def potenciacao(a, b):
    return a ** b

def raiz_quadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Erro: Raiz quadrada de número negativo"

def porcentagem(a, b):
    return (a * b) / 100

while True:
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potenciação (^)")
    print("6. Raiz Quadrada (√)")
    print("7. Porcentagem (%)")
    print("8. Sair")

    escolha = input("Escolha a operação (1/2/3/4/5/6/7/8): ")

    if escolha == "8":
        print("Saindo da calculadora.")
        break

    if escolha in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            resultado = soma(num1, num2)
        elif escolha == "2":
            resultado = subtracao(num1, num2)
        elif escolha == "3":
            resultado = multiplicacao(num1, num2)
        elif escolha == "4":
            resultado = divisao(num1, num2)
        elif escolha == "5":
            resultado = potenciacao(num1, num2)

        print(f"Resultado: {resultado}")

    elif escolha == "6":
        num1 = float(input("Digite o número para calcular a raiz quadrada: "))
        resultado = raiz_quadrada(num1)
        print(f"Resultado: {resultado}")

    elif escolha == "7":
        num1 = float(input("Digite o número: "))
        num2 = float(input("Digite a porcentagem: "))
        resultado = porcentagem(num1, num2)
        print(f"{num2}% de {num1} é igual a {resultado}")

    else:
        print("Escolha inválida. Tente novamente.")

#Faça um programa em Python que calcula a comissão de um vendedor de imóveis.
#Cada imóvel tem um percentual diferente que pode ser aplicado ao cálculo da comissão. [2,5]

def calcular_comissao(valor_venda, percentual_comissao):
    comissao = valor_venda * (percentual_comissao / 100)
    return comissao


tipo_imovel = str(input("Digite o tipo do imóvel (casa, apartamento, terreno): "))
valor_venda = float(input("Digite o valor da venda: "))


if tipo_imovel == "casa":
    percentual_comissao = 5
elif tipo_imovel == "apartamento":
    percentual_comissao = 3
elif tipo_imovel == "terreno":
    percentual_comissao = 2
else:
    print("Tipo de imóvel inválido. Por favor, escolha entre casa, apartamento ou terreno.")
    percentual_comissao = 0


if percentual_comissao > 0:
    comissao = calcular_comissao(valor_venda, percentual_comissao)
    print(f"A comissão do vendedor para a venda de um {tipo_imovel} no valor de R${valor_venda:.2f} é de R${comissao:.2f}")

#Faça um algoritmo em Python que oferece um desconto de 13% para idosos que compram carros.
#O valor do carro com o desconto deve ser exibido na tela sempre que o idoso consultar. [2,5]

idade = int(input("Digite sua idade: "))
valor_carro = float(input("Digite o valor do carro: "))

if idade >= 65:
    desconto = valor_carro * 0.13
    valor_com_desconto = valor_carro - desconto
    print(f"Desconto de 13% aplicado para idoso. O carro sairá por R${valor_com_desconto:.2f}")
else:
    print(f"Desconto não aplicado, o valor final do carro será R${valor_carro:.2f}")

#Faça um algoritmo em Python que leia cinco valores, depois informa na tela qual deles é o maior, qual deles é o menor ou se são iguais.


maior = menor = float(input("Digite o 1º valor: "))


for i in range(2, 6):
    valor = float(input(f"Digite o {i}º valor: "))

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor


print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")
