opcao = int(input('Digite um número: '))

igual_zero = opcao == 0
menor_zero = opcao < 0
maior_zero = opcao > 0

while maior_zero:
    if menor_zero:
        print("A OPÇÃO SELECIONADA É MENOR QUE ZERO")
    elif maior_zero:
        print("A OPÇÃO SELECIONADA É MAIOR QUE ZERO")
    else:
        print("A OPÇÃO SELECIONADA É IGUAL A ZERO")

    opcao = int(input('Digite um número: '))
    igual_zero = opcao == 0
    menor_zero = opcao < 0
    maior_zero = opcao > 0
