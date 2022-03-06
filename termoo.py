"""
--- REGRAS ---

O UNDERSCORE INDICADO POR _ REPRESENTA UMA LETRA AINDA NÃO EXISTENTE NA PALAVRA

O SUSTENIDO (HASHTAG) INDICADO POR # REPRESENTA UMA LETRA EXISTENTE NA PALAVRA MAS EM OUTRA POSICAO

UMA LETRA PREENCHIDA ONDE HAVIA ANTES UM UNDESCORE INDICA QUE A LETRA EXISTE NA PALAVRA E ESTÁ NA POSIÇÃO CORRETA

"""

palavra_dia = "ATRIO"
numero_tentativas = 6
resultado = list("_ _ _ _ _")
ganhou = False

print("")
while numero_tentativas > 0:
    print("Você tem ", numero_tentativas, " tentativas")
    tentativa = input('Qual a palavra do dia? ')
    tentativa = tentativa.upper()

    posicao_tentativa = 0
    posicao_resultado = 0
    for letra in tentativa:
        if tentativa[posicao_tentativa] == palavra_dia[posicao_tentativa]:
            resultado[posicao_resultado] = tentativa[posicao_tentativa]

        posicao_tentativa = posicao_tentativa + 1
        posicao_resultado = posicao_resultado + 2

    resultado_string = ""
    for letra in resultado:
        resultado_string += letra

    resultado = list("_ _ _ _ _")
    print(resultado_string)
    print("")

    if(tentativa == palavra_dia):
        print("SENSACIONAL!!")
        ganhou = True
        break
    else:
        numero_tentativas = numero_tentativas - 1

if(ganhou == False):
    print("Que pena! A palavra do dia era ", palavra_dia)
