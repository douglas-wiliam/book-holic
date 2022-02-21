from utils import color
from utils import month

print('OLÁ, USUÁRIO! QUAL DOCUMENTO VOCÊ QUER INSERIR?')

print('PARA INSERIR DOCUMENTOS DO TIPO LIVRO DIGITE 1 E TECLE [ENTER]')

print(
    'PARA INSERIR DOCUMENTOS DO TIPO TESE, DISSERTAÇÃO OU TCC DIGITE 2 E TECLE [ENTER]')

print('PARA INSERIR DOCUMENTOS DO TIPO ARTIGO DIGITE 3 E TECLE [ENTER]')

print('PARA SAIR DIGITE 0 E TECLE [ENTER]')

opcao = input()

while opcao != '0':

    if opcao == '1':
        autor = input('Nome do autor: ')
        sobrenome = input('Sobrenome: ')
        titulo = input('Título: ')
        sub_tit = input('Subtítulo: ')
        ed = input('Edição: ')
        local = input('Local: ')
        editora = input('Editora: ')
        ano = input('Ano: ')
        print(sobrenome.upper() + ', ' + autor.capitalize() + '. ' + color.BOLD + titulo.capitalize() + color.END
              + ': ' + sub_tit + '. ' + ed + '. ed. ' + local.title() + ': ' + editora.capitalize() + ', ' + ano + '.')
        print('')

    elif opcao == '2':
        autor = input('Nome do autor: ')
        sobrenome = input('SObrenome: ')
        titulo = input('Título: ')
        sub_tit = input('Subtítulo: ')
        ano_dep = input('Ano de depósito: ')
        tipo_trab = input('Tipo de trabalho: ')
        grau = input('Grau: ')
        curso = input('Curso: ')
        instituicao = input('Instituição: ')
        local = input('Local: ')
        ano_apr = input('Ano de apresentação: ')
        print(sobrenome.upper() + ', ' + autor.capitalize() + '. ' + color.BOLD + titulo.capitalize() + color.END
              + ': ' + sub_tit + '. ' + ano_dep + '. ' +
              tipo_trab.title() + ' (' + grau.capitalize() + ' em '
              + curso.title() + ')' + ' - ' + instituicao.title() + ', ' + local.capitalize() + ', ' + ano_apr + '.')
        print('')

    elif opcao == '3':
        autor = input('Nome do autor: ')
        sobrenome = input('Sobrenome: ')
        titulo = input('Título: ')
        sub_tit = input('Subtítulo: ')
        revista = input('Revista: ')
        local = input('Local: ')
        vol = input('Volume: ')
        num = input('Número: ')
        pag_in = input('Página inicial: ')
        pag_fin = input('Página final: ')
        mes = input('Mês: ')
        ano = input('Ano: ')
        print(sobrenome.upper() + ', ' + autor.capitalize() + '. ' + titulo.capitalize() + ': ' + sub_tit + '. '
              + color.BOLD + revista.capitalize() + color.END + ', ' +
              local.capitalize() + ', v. ' + vol + ', n. '
              + num + ', p. ' + pag_in + '-' + pag_fin + ', ' + month.get_month_acronyme(mes) + ', ' + ano + '.')
        print('')

    elif (opcao != '0'):
        print('OPÇÃO SELECIONADA INVÁLIDA!')
        print('')

    print('PARA INSERIR DOCUMENTOS DO TIPO LIVRO DIGITE 1 E TECLE [ENTER]')

    print(
        'PARA INSERIR DOCUMENTOS DO TIPO TESE, DISSERTAÇÃO OU TCC DIGITE 2 E TECLE [ENTER]')

    print('PARA INSERIR DOCUMENTOS DO TIPO ARTIGO DIGITE 3 E TECLE [ENTER]')

    print('PARA SAIR DIGITE 0 E TECLE [ENTER]')

    opcao = input()
