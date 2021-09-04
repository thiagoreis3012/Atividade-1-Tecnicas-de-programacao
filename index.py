import random

portal = random.randint(1,5)
caminho_vermelho = 1
caminho_preto = 2
sala = 1


print("Você esta no Inicio")
print("Escolha seu caminho:")
print("[1] caminho vermelho")
print("[2] caminho preto")
caminho = int(input())

while (sala <= 7):


  if (caminho == 1):
   print("Você esta na sala: {}".format(sala + caminho_vermelho))
   print("Escolha seu caminho :")
   print("[1] caminho vermelho")
   print("[2] caminho preto")
   sala = sala + caminho_vermelho
   caminho = int(input())

 
  elif(caminho == 2):
   print("Você esta na sala: {}".format(sala + caminho_preto))
   print("Escolha seu caminho :")
   print("[1] caminho vermelho")
   print("[2] caminho preto")
caminho = int(input())
sala = sala + caminho_preto

def count (caminho):


 print("caminhoresultado : {}".format(caminho))

if (sala + caminho_vermelho == 8 or sala + caminho_preto == 8 ):
    print("Você esta na sala : 8 / Portal te mandará para a sala :{}".format(portal))

elif (sala + caminho_vermelho == 9 or sala + caminho_preto == 9):
    print("Você esta na sala : 9")
    print("VENCEU !!!!!!")