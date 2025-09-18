# 1) listagem
#from turtledemo.rosette import mn_eck

from operacoesbd import *
from ouvidoria import *

conn = criarConexao('127.0.0.1', 'root', 'admin', 'gestao_ouvidoria')
manifestacoes =[]
print("Bem Vindo ao Menu de Manifestações")
while True:
    print(f'\n1) Listar \n2) Adicionar \n3) Pesquisar manifestações \n4) Remover manifestações \n5) Substituir manifestações \n6) Sair')

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        listarManifestacoes(conn)

    elif opcao == 2:
        adicionarManifestacao(conn)

    elif opcao == 3:
        pesquisarManifestacoes(conn)

    elif opcao == 4:
        removerManifestacoes(conn)

    elif opcao == 5:
        editarManifestacoes(conn)

    elif opcao == 6:
        break

    else:
        print(f'\nOpção inválida!')

print(f'Obrigado por utilizar!')
encerrarConexao(conn)