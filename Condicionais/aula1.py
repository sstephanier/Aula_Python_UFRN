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


