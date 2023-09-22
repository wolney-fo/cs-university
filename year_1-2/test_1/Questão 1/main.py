import functions


# Informações de clientes
reservas_clientes = []
nome_clientes = []
CPFs_clientes = []
functions.ler_usuarios(nome_clientes, CPFs_clientes, reservas_clientes)

#Informações das máquinas
codigo = []
tipo = []
marca = []
modelo = []
ano = []
valor = []
status = []
functions.ler_maquinas(codigo, tipo, marca, modelo, ano, valor, status)


while True:
    try:
        acao = functions.menu_de_acoes()

        if acao == 0:
            print('Até mais!')
            break

        elif acao == 1: # Cadastro de clientes
            functions.acao1(nome_clientes, CPFs_clientes, reservas_clientes)

        elif acao == 2: # Cadastro de máquinas
            functions.acao2(codigo,tipo,marca,modelo,ano,valor,status)

        elif acao == 3: # Registro de aluguel
            functions.acao3(nome_clientes, CPFs_clientes, reservas_clientes, codigo, tipo, marca, modelo, ano, valor, status)

        elif acao == 4: # Relatório de clientes
            functions.acao4(nome_clientes, CPFs_clientes, reservas_clientes)

        elif acao == 5: # Relatório de clientes
            functions.acao5(codigo, tipo, marca, modelo, ano, valor, status)

        elif acao == 6: # Relatório de reservas
            functions.acao6()

    except:
        print('Oops! Algo correu mal :/')
