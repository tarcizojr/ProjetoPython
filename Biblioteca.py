import time
from datetime import date
from datetime import datetime


def tit(txt):
    a = len(txt)
    print('-' * a)
    print(txt)
    print('-' * a)

    return date.today()


livros_todos = [{'Guerra e Paz', 'Liev Tolstói'}, {'Dom Casmurro', 'Machado de Assis'},{'Quincas Borba', 'Machado de Assis'}]  # Representa a Quantidade Que livros da Biblioteca
livros_pegos = []  # Representa os Livros ja Pegos
livros_disponiveis = ['Guerra e Paz']  # Representa os Livros ainda disponiveis na biblioteca
cadastros = ['tj', 'kj']

data = date.today()
now = datetime.now()

a1 = 'm'  # 'a1' representa 'Peimeira Ação' a primeira ação do usuario, que escolhe no menu oque deseja fazer
# 'a2' representa a 'Segunda ação' esta segunda açâo varia de acordo com a primeira opção escolhida

while (a1 == 'm'):  # Primeiro dia de Cog. 23/10/2020. Foi feito o menu inicial, a opção, 'a', 'b', 's'
    print('''
    |---------- MENU INICIAL----------|   
    | (a) Adicionar Livro a Biblioteca|
    | (b) Todos so Livros             |
    | (c) Livros Disponiveis          |
    | (d) Pegar Livro                 |
    | (e) Criar um Cadastro Pessoal   |
    | (s) Sair                        |                     
    |---------------------------------|

    ''')
    a1 = input('''Qual a acão que deseja execultar?''')  # opção ok

    # ---------- Adicionar livro ---------

    while (a1 == 'a'):

        print(tit('Adicionar Livro a Biblioteca'))  # opção ok
        nome = input('Nome do Livro:')
        altor = input('Nome do Altor:')

        livros_todos += [{nome, altor}]
        print('Um momento...')
        time.sleep(1)
        print('Livro Adicionado a Biblioteca')

        # Continuar adicionando livros ou voltar ao Menu
        adicionar = input('Deseja Adicionar Mais Livros(a) ou ir Para o Menu Inicial (m)?')  # opção ok

        if adicionar == 'a':
            a1 == 'a'
        elif adicionar == 'm':
            a1 = 'm'

    # ---------Todos os Livros Da Biblioteca -------------

    if a1 == 'b':

        print(tit('Todos os Livros Da Biblioteca'))
        for i in (livros_todos):
            print(i)

        voltar_menu = input('Deseja Voltar ao Menu (m) ou sair do programa (s)?')  # opção ok

        if voltar_menu == 'm':
            a1 = 'm'


        elif voltar_menu == 's':
            print('Saindo do Programa ...')
            time.sleep(2)
            print('Programa Fechado')
            break

    # --------Livros Disponiveis-----

    elif a1 == 'c':

        print(tit('Livros Disponiveis'))  # mostrar quais os livros ainda n foram pegos

        for i in livros_disponiveis:
            print(i)  # printar todos os (livros - lisvros pegos)

        p_m = input('Deseja ir para o Menu (m) ou sair (s)?')

        if p_m == 'm':  # oção 'm' está funcionando
            a1 = 'm'

        elif p_m == 's':
            break

    # --------Pegar Livro---------

    elif a1 == 'd':

        print(tit('Pegar Livro'))
        livro = input('Qual livro voce deseja pegar?')

        if livro in livros_disponiveis:
            print('{} Esta disponivel'.format(livro))  # ver se a pessoa tem cadastro na biblioteca, caso não criar um
            # mperguntar se o livros esta fisponivel para ser pego

            confirmar = input('Deseja realmente pegar este livro {} ? sim(s) não (n):'.format(livro))
            if confirmar == 's':
                nome = input('Seu nome:')

                if nome in cadastros:
                    print('Espere um Momento')
                    time.sleep(2)
                    livros_pegos.append(livro)
                    livros_disponiveis.remove(livro)
                    print('Cadastro Confirmado')
                    time.sleep(2)
                    print('Livro Pego com Sucesso')
                    print('Hoje é dia {} o Livro {} deve ser Devolvido daqui a 7 dias uteis'.format(data, livro))
                    print(
                        'No dia {}-{}-{} ou devera ser feita a atualização'.format((now.day * 7), now.month, now.year))

                    saida = input('Deseja voltar ao menu Principal (m) ou sair (s)?')
                    if saida == 'm':
                        a1 = 'm'


                    elif saida == 's':
                        break

                else:
                    print('Você não esta no Cadastro de Pessoas \nVolte ao Menu e se Cadastre ou Tente Novamente')
                    time.sleep(1)
                    a1 = 'm'


        else:  # pegar in livros_disponiveis == False:
            print('{} Não esta disponivel'.format(livro))
            print('Tente Novamente')
            time.sleep(1)
            a1 = 'm'

        # -------Cadastro Pessoal-------

    elif a1 == 'e':
        print(tit('Cadastro Pessoal'))  # cadastro de pessoas

        nome = input('Nome:')
        idade = input('Idade:')
        end = input('Endereço:')
        tel = input('Telefone:')

        cadastros += (
        {'Nome:', nome, 'Idade:', idade, 'Endereço:', end, 'Telefone:', tel})  # esta preenchendo aleatoriamente

        print('Nome:', nome, 'Idade:', idade, 'Endereço:', end, 'Telefone:', tel)

        print('Espere um Momento')
        time.sleep(2)
        print('Cadastro Feito')
        menu = input('Deseja Voltar ao Menu Inicial (m) ou Sair (s)?')

        if menu == 'm':
            time.sleep(1)
            a1 = 'm'
        elif menu == 's':
            break




    # --------- Sair do Programa ------------

    elif (a1 == 's'):
        print('Saindo do Programa ...')
        time.sleep(2)
        print('Programa Fechado')  # opção ok
        break
