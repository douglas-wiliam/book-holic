from turtle import clear


título = input('Qual o seu título de livro favorito?: ')
autor = input('Qual o nome do/a autor/a?: ')
sobrenome = input('Qual o sobrenome?: ')
ed = input('Qual a edição desse livro: ')
ano = input('Qual o ano de publicação?: ')
print('A sua referência do livro é: ', sobrenome.upper() + ', ' +
      autor.capitalize() + '. ' + título.capitalize() + '. ' + ed + '. ed. ' + ano + '.')
print('Faz ' + str(2022 - int(ano)) + ' ano(s) que esse livro foi lançado')
