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

# Faça um programa em Python que dado um intervalo entre 1 a N informa quantos números ímpares são múltiplos de 3, onde N é informado pelo usuário.

#Declarando as váriaveis
número = int(input ("Digite um número inteiro positivo maior que 1: ")) #recebe o número e converte para inteiro
cont = 0

print("\n")

for i in range(1, número+1):
  if (i%2!=0) and (i%3==0):
    print ("["+ str (i) + "] é um número impar multiplo de 3")
    cont+=1

print("\n")
print ("Entre [1 e "+str(número)+ "] existem "+str(cont)+ " números impares multiplos de 3")

# Faça um programa em Python, utilizando While que calcula o fatorial de um número. Por exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.

#Declarando as váriaveis
número = int(input ("Digite um número inteiro positivo maior que 1: ")) #recebe o número e converte para inteiro
fatorial = 1

for i in range(1, número+1):
  fatorial *= i # Essa expressão é igual a  fatorial =  fatorial * i

print("O fatorial de "+str(número)+ " é igual a : " + str(fatorial))
