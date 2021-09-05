from random import randint

resultados = {
    "1": "Você não chegou na sala 9\nGAME OVER!!",
    "2": "Você não chegou na sala 9\nGAME OVER!!",
    "3": "Você não chegou na sala 9\nGAME OVER!!",
    "4": "Você não chegou na sala 9\nGAME OVER!!",
    "5": "Você não chegou na sala 9\nGAME OVER!!",
    "6": "Você não chegou na sala 9\nGAME OVER!!",
    "7": "Você não chegou na sala 9\nGAME OVER!!",
    "8": "Você não chegou na sala 9\nGAME OVER!!",
    "9": "Você chegou na sala 9\nYOU WIN!!"
}

CAMINHO_VERMELHO = 1
CAMINHO_PRETO = 2
sala = 1
jogadas = 0

while sala < 9 and jogadas < 7:
    portal = randint(1, 5)
    caminho = int(input(f"""Você está na sala {sala}.
Escolha seu caminho:
[ 1 ] caminho vermelho
[ 2 ] caminho preto\n"""))
    if sala == 8 and caminho == 2: 
        sala = portal
        print(f"O portal te jogará para a sala: {sala}")
        jogadas += 1
    elif sala + caminho == 6:
        sala += caminho
        print("""Você chegou na sala 6, aqui você só tem um único caminho a seguir que te levará para a sala 8""")
        sala += CAMINHO_PRETO
        jogadas += 1
    else:
        sala += caminho
        jogadas += 1

resultadoFinal = resultados[str(sala)]
print(resultadoFinal)