a = True
b = True
c = False

#Operador OR
print ("\n Operador OR \n")

# Tudo verdade
if a or b:
  print ("Uma verdade - eu entro no IF")

# Somente uma falsidade
if a or c:
  print ("Uma verdade - eu entro no IF")

# Todas falsidade
if not a or c:
  print ("Tudo verdade - eu entro no IF")
else:
  print ("Todas as sentenças falsas")

#  Atividade 01  Faça um programa em Python que solicita a idade de uma pessoa e depois imprime na tela se ela é menor de idade, maior de idade ou idosa.
# >18 maior de idade < 65 idoso

idade = 12

if (idade > 18 and idade < 65):
  print("maior de idade")
elif (idade > 65):
  print("idoso")
else :
  print("menor de idade")


# 2) Usando estruturas condicionais implemente uma calculadora básica. O usuário deve informar os valores de entrada e a operação que deseja.

a = 3
b = 5

operacao = 3 + 5

if (operacao == a + b):
  print("soma")
elif (operacao == a * b):
  print("multiplicação")
elif (operacao == a / b):
  print("divisão")
else :
  print("subtração")



