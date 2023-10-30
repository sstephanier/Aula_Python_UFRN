# Questão 1
# Faça um programa em Python que dado um número inteiro positivo ele informa quantos
# números são múltiplos 7 entre 1 e o número informado.


numero_informado = int(input("Digite um número maior que 1: "))
contador = 0
numero = 1

while numero <= numero_informado:
    if numero % 7 == 0:
        contador += 1
    numero += 1

print(f"Entre 1 e {numero_informado}, existem {contador} múltiplo(s) de 7.")


# # 2) Faça um programa em Python que imprime a seguinte figura:
# # *****
# # ****
# # ***
# # **
# # *

linhas = 5

while linhas > 0:
    ast = "*" * linhas
    print(ast)
    linhas -= 1

# 3) Faça um programa em Python que diz se um número é ou não primo (2,5).
# Pra ser primo basta ser divisivel por 1 e por ele mesmo
# Em um loop avaliando os números so pode ter dois disivores

numeroInformado = int(input("Digite um número: "))
contador = 0
numero = 1

while numero <= numeroInformado:
    if numeroInformado % numero == 0:
        contador += 1
    numero += 1
if contador == 2:
    print(f"O número {numeroInformado} é primo.")
else:
    print(f"O número {numeroInformado} não é primo.")

# 4) Faça um programa em Python que imprime a seguinte figura:
# 1#
# 2##
# 3###
# 4####
# 5#####

numero_linhas = 5
linha = 1

while linha <= numero_linhas:
    print(str(linha) + "#" * linha)
    linha += 1

# 5) Faça um programa em Python que imprime a seguinte figura (Desafio):

# 1#
# 2##
# 3###
# 4####
# 5#####
# 4####
# 3###
# 2##
# 1#


numero_linhas = 5
linha = 1

while linha <= numero_linhas:
    print(str(linha) + "#" * linha)
    linha += 1

linha = 4

while linha >= 1:
    print(str(linha) + "#" * linha)
    linha -= 1
