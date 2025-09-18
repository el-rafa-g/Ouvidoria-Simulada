from operacoesbd import *

def listarManifestacoes(conn):
    print(f'\nLista de manifestações')
    consulta = "select * from ouvidoriaBD;"
    manifestacoes = listarBancoDados(conn, consulta)

    if len(manifestacoes) == 0:
        print(f"\nNão existem manifestações cadastradas")
    else:
        for item in manifestacoes:
            print(f'\nCódigo da Manifestação: {item[0]}\nTipo da Manifestação: {item[2]}\nAssunto da Manifestação: {item[3]} \nManifestação: {item[4]}')

def adicionarManifestacao(conn):
    nome = input("Digite o seu nome: ").capitalize()
    confirmacao = [1,2,3]
    tipo = int(input(f'Selecione o tipo da sua manifestção \n1) Reclamação \n2) Elogio \n3) Sugestão\n: '))
    if tipo == 1:
        tipo = str('Elogio')
    elif tipo == 2:
        tipo = str('Reclamação')
    elif tipo == 3:
        tipo = str('Sugestão')
    else:
        print(f'Número inválido, digite novamente!')

    assunto = input("Digite o assunto: ").capitalize()
    manifestacao = input("Digite a manifestação: ").capitalize()

    respondente = int(input(f'\nQual respondente te atendeu? \n1) Evandro \n2) Matheus \n3) Rafael\n: '))
    if respondente == 1:
        respondente = str('Evandro')
    elif respondente == 2:
        respondente = str('Matheus')
    elif respondente == 3:
        respondente = str('Rafael')
    else:
        print(f'Número inválido, digite novamente!')

    insere = 'insert into ouvidoriaBD(nome,tipo,assunto,manifestacao,respondente) values(%s,%s,%s,%s,%s)'
    valores = [nome, tipo, assunto, manifestacao, respondente]
    novaManifestacao = insertNoBancoDados(conn, insere, valores)
    print(f'Nova manifestação adicionada com sucesso.')

def pesquisarManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação: '))
    comando = "select * from ouvidoriaBD where codigo = %s"
    lista = [codigo]
    manifestacoes = listarBancoDados(conn, comando, lista)

    if len(manifestacoes) != 0:
        # Aqui, já sabemos que 'manifestacoes' contém a manifestação que corresponde ao código
        print(f'\nA manifestação pesquisada é: {manifestacoes[0]}.')
    else:
        print(f'A manifestação não existe!')

def removerManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação que deseja remover: '))
    comando = "select * from ouvidoriaBD where codigo = %s"
    lista = [codigo]
    manifestacoes = listarBancoDados(conn, comando, lista)

    if len(manifestacoes) > 0:
        # Exibe a manifestação encontrada para confirmação
        print(f'A manifestação encontrada é: {manifestacoes[0]}')

        confirmacao = int(input(f'Deseja remover esta manifestação? 1- Sim 2- Não: '))
        if confirmacao == 1:
            # Remover manifestação
            comando = "delete from ouvidoriaBD where codigo = %s"
            lista = [codigo]
            # Executando o comando de remoção no banco de dados
            listarBancoDados(conn, comando, lista)
            print(f'Manifestação {manifestacoes[0]} removida com sucesso.')
        elif confirmacao == 2:
            print(f'Manifestação não foi removida!')
        else:
            print(f'Opção inválida!')
    else:
        print(f'A manifestação com o código {codigo} não foi encontrada!')

"""def editarManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação que deseja substituir: '))
    comando = "select * from ouvidoriaBD where codigo = %s"
    lista = [codigo]
    manifestacoes = listarBancoDados(conn, comando, lista)
    if len(manifestacoes) > 0:
        confirmacao = int(input(f'Deseja substituir "{manifestacoes[0]}"? 1- Sim 2- Não: '))
        if confirmacao == 1:
            comando = 'update ouvidoriaBD set tipo = %s, assunto = %s, manifestacao = %s where codigo = %s'
            tipo = int(input(f'Selecione o tipo da sua manifestação \n1) Reclamação \n2) Elogio \n3) Sugestão\n: '))
            if tipo == 1:
                tipo = str('Reclemação')
            elif tipo == 2:
                tipo = str('Elogio')
            elif tipo == 3:
                tipo = str('Sugestão')
            else:
                print(f'Número inválido, digite novamente!')
            assunto = input("Digite o assunto: ").capitalize()
            manifestacao = input("Digite a manifestação: ").capitalize()


            lista = [tipo, assunto, manifestacao, codigo]



            manifestacoes = listarBancoDados(conn, comando, lista)



            for item in manifestacoes:
                print(f'Substituído para: Assunto: {item[3]} \nManifestação: {item[4]}')
        elif confirmacao == 2:
            print(f'Manifestação não foi substituída!')
        else:
            print(f'Opção inválida!')
    else:
        print(f'Não existe manifestação com esse código!')


def editarManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação que deseja substituir: '))
    comando = "select * from ouvidoriaBD where codigo = %s"
    lista = [codigo]
    manifestacoes = listarBancoDados(conn, comando, lista)

    if len(manifestacoes) > 0:  # Verifica se a manifestação foi encontrada
        print(f'Manifestação encontrada: {manifestacoes[0]}')

        confirmacao = int(input(f'Deseja substituir essa manifestação? 1- Sim 2- Não: '))

        if confirmacao == 1:
            # Pergunta os novos dados para a manifestação
            tipo = int(input(f'Selecione o tipo da sua manifestação \n1) Reclamação \n2) Elogio \n3) Sugestão\n: '))

            # Corrigir digitação e atribuição do tipo
            if tipo == 1:
                tipo = 'Reclamação'
            elif tipo == 2:
                tipo = 'Elogio'
            elif tipo == 3:
                tipo = 'Sugestão'
            else:
                print(f'Número inválido, digite novamente!')
                return  # Se o tipo for inválido, retorna e não continua a execução

            assunto = input("Digite o assunto: ").capitalize()
            manifestacao = input("Digite a manifestação: ").capitalize()

            # Atualiza a manifestação no banco
            comando_atualizcao = 'UPDATE ouvidoriaBD SET tipo = %s, assunto = %s, manifestacao = %s WHERE codigo = %s'
            lista_atualizacao = [tipo, assunto, manifestacao, codigo]

            # Executa o comando de atualização
            cursor = conn.cursor()
            cursor.execute(comando_atualizcao, lista_atualizacao)
            conn.commit()  # Confirma a alteração no banco de dados
            print(f'Manifestação com código {codigo} foi substituída com sucesso.')

        elif confirmacao == 2:
            print(f'Manifestação não foi substituída!')
        else:
            print(f'Opção inválida!')

    else:
        print(f'Não existe manifestação com o código {codigo}!')"""


def editarManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação que deseja substituir: '))

    # Consultar a manifestação com o código informado
    comando = "select * from ouvidoriaBD where codigo = %s"
    lista = [codigo]
    manifestacoes = listarBancoDados(conn, comando, lista)

    if len(manifestacoes) > 0:  # Verifica se a manifestação foi encontrada
        print(f'Manifestação encontrada: {manifestacoes[0]}')

        confirmacao = int(input(f'Deseja substituir essa manifestação? 1- Sim 2- Não: '))

        if confirmacao == 1:
            # Pergunta os novos dados para a manifestação
            tipo = int(input(f'Selecione o tipo da sua manifestação \n1) Reclamação \n2) Elogio \n3) Sugestão\n: '))

            # Corrigir digitação e atribuição do tipo
            if tipo == 1:
                tipo = 'Reclamação'
            elif tipo == 2:
                tipo = 'Elogio'
            elif tipo == 3:
                tipo = 'Sugestão'
            else:
                print(f'Número inválido, digite novamente!')
                return  # Se o tipo for inválido, retorna e não continua a execução

            assunto = input("Digite o assunto: ").capitalize()
            manifestacao = input("Digite a manifestação: ").capitalize()

            # Comando SQL de atualização
            comando = 'update ouvidoriaBD set tipo = %s, assunto = %s, manifestacao = %s where codigo = %s'
            lista = [tipo, assunto, manifestacao, codigo]

            # Reutilizando a função para executar comandos SQL
            resultado = atualizarBancoDados(conn, comando, lista)

            if resultado:
                print(f'Manifestação com código {codigo} foi substituída com sucesso.')
            else:
                print('Erro ao substituir a manifestação.')

        elif confirmacao == 2:
            print(f'Manifestação não foi substituída!')
        else:
            print(f'Opção inválida!')

    else:
        print(f'Não existe manifestação com o código {codigo}!')


