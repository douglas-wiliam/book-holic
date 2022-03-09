"""
--- REGRAS ---

O UNDERSCORE REPRESENTADO POR _ INDICA UMA LETRA AINDA NÃO EXISTENTE NA PALAVRA

UMA LETRA EXISTENTE NA PALAVRA MAS EM OUTRA POSICAO É MARCADA NA COR AMARELA

UMA LETRA EXISTE NA PALAVRA E ESTÁ NA POSIÇÃO CORRETA É MARCADA NA COR VERDE

"""
from sty import fg, bg, ef, rs

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

    for letra_tentativa in tentativa:
        posicao_palavra_dia = 0
    
    for letra_dia in palavra_dia:
    		if (letra_tentativa == letra_dia) and (posicao_tentativa != posicao_palavra_dia):
            resultado[posicao_resultado] = bg.yellow + ef.bold + fg.white + letra + fg.rs + ef.rs bg.rs
  			
        posicao_palavra_dia +=1
        
        posicao_tentativa += 1  
        posicao_resultado += 2
  
    
    posicao_palavra_dia = 0
    posicao_resultado = 0
    for letra_tentativa in tentativa:
        if letra_tentativa == palavra_dia[posicao_palavra_dia]:
            resultado[posicao_resultado] = bg.green + ef.bold + fg.white + letra_tentativa + fg.rs + ef.rs bg.rs
        
        posicao_palavra_dia += 1
        posicao_resultado += 2

    
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
