print ('Olá, usuário! Qual documento você quer inserir?')
doc = input ()

class color:
    BOLD = '\033[1m' 
    END = '\033[0m'


while doc != '':
    if doc == 'livro':
        autor = input ('Nome do autor: ')
        sobrenome = input('Sobrenome: ')
        titulo = input('Título: ')
        sub_tit = input ('Subtítulo: ')               
        ed = input ('Edição: ')
        local = input ('Local: ')
        editora = input ('Editora: ')
        ano = input ('Ano: ')
        print (sobrenome.upper() + ', ' + autor.capitalize() + '. ' + color.BOLD + titulo.capitalize() + color.END 
        + ': ' + sub_tit + '. ' + ed + '. ed. ' + local.title() + ': ' + editora.capitalize() + ', ' + ano + '.')
    elif doc == 'artigo':
        autor = input ('Nome do autor: ')
        sobrenome = input('Sobrenome: ')
        titulo = input('Título: ')
        sub_tit = input ('Subtítulo: ')               
        revista = input ('Revista: ')
        local = input ('Local: ')
        vol = input ('Volume: ')
        num = input ('Número: ')
        pag_in = input ('Página inicial: ')
        pag_fin = input ('Página final: ')
        mes = input ('Mês: ')
        ano = input ('Ano: ')
        print (sobrenome.upper() + ', ' + autor.capitalize() + '. ' + titulo.capitalize() + ': ' + sub_tit + '. ' 
        + color.BOLD + revista.capitalize() + color.END + ', ' + local.capitalize() + ', v. ' + vol + ', n. ' 
        + num + ', p. '+ pag_in + '-' + pag_fin + ', ' + mes + ', ' + ano + '.')
    print ('Olá, usuário! Qual documento você quer inserir?')
    doc = input ()