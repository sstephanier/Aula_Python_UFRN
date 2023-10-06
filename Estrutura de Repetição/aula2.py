# Utilizando o comando While (estrutura de repetição) faça um programa em Python que dado um número inteiro positivo qualquer informado pelo usuário ele informa se o número é ou não primo.

# Caso o usuário informe um número negativo o sistema deve informar que não há números primos negativos.

# Depois o programa deve em Python deve ser enviado pelo SIGAA.

#Declarando as váriaveis
número = int(input ("Digite um número inteiro positivo maior que 1: ")) #recebe o número e converte para inteiro
divisor = 1 # variável utilizada para incrementar a divisão e obter o resto
contador = 0 # variável utilizada para incrementar o resto da divisão para tentar encontrar o primo - se for igual 2 no final é porque o número é primo

print("\n") #Somente para organizar a saída de dados

#Laço utilizado para contar os restos das divisões até o número informado pelo usuário
if (número > 1):
  while (divisor <= número):
    if ((número%divisor)==0): #testa o resto da divisão, se for igual 0 incrementa a variável contador
      contador +=1
      if (contador == 3):
        break # força a saída do laço, pois não faz mais sentido ficar contando
    divisor +=1 # incrementa a variável divisor para que possa encontrar a condição de parada do laço e para que possa ser utilizado para contar os restos das divisões iguais a 0
  if (contador == 2): # Se depois que finalizar o laço contador for igual a 2 é porque o número é primo
    print(str(número) + " é um número primo")
  else:
    print(str(número) + " não é um número primo")
elif (número == 1) or (número == 0): # testes complementare para ajudar o usuário
  print("Você não digitou um número inteiro positivo maior que 1")
else:
   print("Não há números primos negativos, por exemeplo igual a " + str(número))
