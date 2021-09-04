import random
contador = 1
#inicio caminho vermelho ou preto
print("Você esta na sala: 1")
print("Escolha seu caminho: ")
print("[1] caminho vermelho")
print("[2] caminho preto")
sala1 = int(input()) 

while (contador <= 9):
#sala 2 caminho vermelho
 if(sala1 == 1 ):
  CV = 1 + 1
  print("você esta na sala : {}".format(CV + contador))
  print("Escolha seu caminho: ")
  print("[1] caminho vermelho")
  print("[2] caminho preto")
  sala2 = int(input()) 

#sala 1 caminho preto
 elif(sala1 == 2):
  CP = 1 + 2
  print("você esta na sala : {}".format(CP +))
  print("Escolha seu caminho: ")
  print("[1] caminho vermelho")
  print("[2] caminho preto")
  sala3 = int(input())

#sala 3 caminho preto
if (sala3 == 2):
  CP = 3 + 2
  print("você esta na sala : {}".format(CP))
  print("Escolha seu caminho: ")
  print("[1] caminho vermelho")
  print("[2] caminho preto")
  sala5 = int(input()) 

#sala 5 caminho preto
elif (sala5 == 2):
  CP = 5 + 2
  print("você esta na sala : {}".format(CP))
  print("Escolha seu caminho: ")
  print("[1] caminho vermelho")
  print("[2] caminho preto")
  sala7 = int(input()) 

# Vitoria
if (sala7 == 1):
  CV = 7 + 1
  print("vc esta na sala : 8")


# caminho preto
if(sala2 == 2 ):
  CP = 2 + 2
  print("você esta na sala : {}".format(CP))
  print("Escolha seu caminho: ")
  print("[1] caminho vermelho")
  print("[2] caminho preto")
  sala4 = int(input()) 

# caminho preto
if(sala4 == 2 ):
  CP = 4 + 2
  print("você esta na sala : {}".format(CP))
  print("Escolha seu caminho: ")
  print("[1] caminho vermelho")
  print("[2] caminho preto")
  sala6 = int(input()) 

if(sala6 == 2 ):
  CP = 6 + 2
  print("você esta na sala : {}".format(CP))
  print("Escolha seu caminho: ")
  print("[1] caminho vermelho")
  print("[2] caminho preto")
  sala8 = random.randint(1,5)
  print("você esta na sala :{} entrará no portal e voltará para a sala: {}".format(CP,sala8))