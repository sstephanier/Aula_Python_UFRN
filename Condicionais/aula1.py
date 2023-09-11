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