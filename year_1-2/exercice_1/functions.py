#Receber Sim ou Não de uma pergunta
def answerConfirm(quest):
    valid_abswers_pt = ('S', 'N')
    while True:
        try:
            answer = input(quest).upper()
            assert answer in valid_abswers_pt
            if answer == 'S' or answer == 'Y':
                return True
            else:
                return False
        except:
              print(f"'{answer}' não é uma resposta válida")


# Menu de ações
def menu():
    print('''
LoCar 🚗 🚙

[ 1 ] Cadastrar cliente
[ 2 ] Cadastrar um veículo
[ 3 ] Registrar aluguel
[ 0 ] Sair
''')
    acao = int(input('> '))
    assert 0 <= acao <= 9

    return acao


# Ação 1 - Cadastro de clientes
def acao1(dados_clientes, dados_veiculos):
    print('CADASTRAR CLIENTE')

    nome = input('Nome: ').upper().strip()
    assert '-' not in nome
    assert len(nome) <= 70, 'Digite até 70 caracteres'

    idade = int(input('Idade: '))
    assert 0 < idade <= 130
    assert idade >= 18, 'O cliente precisa ser maior de idade para alugar um veículo!!'

    sexo = input('Sexo: ').upper().strip()
    assert sexo == 'F' or sexo == 'M'

    dados_clientes[0].append(nome)
    dados_clientes[1].append(idade)
    dados_clientes[2].append(sexo)

    dados_clientes[3].append(len(dados_clientes[0]))

    print(f'\n✔️ Cliente {nome} cadastrado com sucesso')


# Ação 2 - Cadastro de veículos
def acao2(dados_clientes, dados_veiculos):
    print('CADASTRAR VEÍCULOS')

    tipo = input('Tipo: (Carro/Moto): ').upper().strip()
    assert len(tipo) <= 5 and (tipo == 'CARRO' or tipo == 'MOTO')

    marca = input('Marca: ').upper().strip()
    assert len(marca) <= 40, 'Digite até 40 caracteres!'

    modelo = input('Modelo: ').upper().strip()
    assert len(modelo) <= 40, 'Digite até 40 caracteres!'

    placa = input('Placa (AAA0000): ').upper().strip()
    assert len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric(), 'Placa inválida!'

    quilometragem = int(input('Quilometragem: '))
    assert quilometragem > 0

    dados_veiculos[0].append(tipo)
    dados_veiculos[1].append(marca)
    dados_veiculos[2].append(modelo)
    dados_veiculos[3].append(placa)
    dados_veiculos[4].append(False) # Status
    dados_veiculos[5].append(quilometragem)
    dados_veiculos[6].append(0) # Quantas vezes já foi alugado
    dados_veiculos[7].append(0) # Para quem está alugado

    print('\n✔️ Veículo cadastrado com sucesso')


# Ação 3 - Registrar aluguel
def acao3(dados_clientes, dados_veiculos, lista_quilometragem, lista_feminin_7dias ):
    print('REGISTRAR ALUGUEL')

    idCliente = int(input('Cliente (ID): '))
    assert 0 <= idCliente, 'ID inválido'
    assert idCliente in dados_clientes[3], 'Cliente não encontrado'

    index_c = idCliente - 1

    placa = input('Placa: ')
    assert len(placa) == 7 and placa[:3].isalpha() and placa[3:].isnumeric(), 'Placa inválida!'
    assert placa in dados_veiculos[3], 'Veículo não encontrado'

    index_v = dados_veiculos[3].index(placa)

    if not dados_veiculos[4][index_v]:
        qtd_dias = int(input('Dias contratados (até 30): '))
        assert 0 < qtd_dias <= 30, 'Aluguel negado'

        quilometragem = int(input('Quilometragem: '))
        assert 0 < quilometragem, 'Quilometragem inválida'

        valorTotal = (70 * qtd_dias) + (0.1 * quilometragem)

        print(f'''
Detalhes do pedido:
Cliente: {dados_clientes[0][index_c]}
Veículo: {dados_veiculos[1][index_v]} {dados_veiculos[2][index_v]} ({dados_veiculos[0][index_v]})

Dias contratados: {qtd_dias}
Quilometragem contratada: {quilometragem}

> Valor total: R${valorTotal:.2f}''')

        if answerConfirm('Confirmar (s/n): '):
            dados_veiculos[4][index_v] = True             # Alterar o status
            dados_veiculos[5][index_v] += quilometragem   # Adicionar a quilometragem do veículo
            dados_veiculos[6][index_v] += 1               # Contar quantas vezes foi alugado
            dados_veiculos[7][index_v] = idCliente        # Identificar o cliente

            lista_quilometragem.append(quilometragem)

            if (dados_clientes[2][index_c] == 'F') and (qtd_dias > 7):
                lista_feminin_7dias.append(dados_clientes[0][index_c])

            print('\n✔️ Aluguel confirmado')

        else:
            print('\n❌ Operação cancelada')

    else:
        print('Veículo indisponível!')
