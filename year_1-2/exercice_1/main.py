import functions as f


dados_clientes = [
    list(), # (0) Nome
    list(), # (1) Idade
    list(), # (2) Sexo
    list()  # (3) Número de identificação (ID)
]

dados_veiculos = [
    ['CARRO', 'CARRO'],     # (0) Tipo
    ['CHEVROLET', 'HONDA'], # (1) Marca
    ['CELTA', 'CIVIC'],     # (2) Modelo
    ['IAN0000', 'AAA0000'], # (3) Placa
    [False, False],         # (4) Status
    [73534, 11049],         # (5) Quilometragem atual
    [3, 7],                 # (6) Quantas vezes já foi alugado
    [0, 0]                  # (7) Para quem está alugado (ID)
]

# Dados específicos
lista_quilometragem = list()
lista_feminin_7dias = list()

while True:
    acao = f.menu()

    if acao == 0:
        break

    elif acao == 1:
        f.acao1(dados_clientes, dados_veiculos)

    elif acao == 2:
        f.acao2(dados_clientes, dados_veiculos)

    elif acao == 3:
        f.acao3(dados_clientes, dados_veiculos, lista_quilometragem, lista_feminin_7dias)


if not lista_quilometragem:
    print('Até mais.')

else:
    if f.answerConfirm('Deseja consultar os relatórios? (s/n): '):
        if lista_quilometragem:
            print(f'Média de quilômetros contratados: {sum(lista_quilometragem) / len(lista_quilometragem):.2f}')

        if lista_feminin_7dias:
            print('Clientes do sexo feminino com aluguéis acima de 1 semana:')
            for cliente in lista_feminin_7dias:
                print(cliente)
