#/////////////////////////////////
#// Gerais ///////////////////////
#/////////////////////////////////

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


# Tratamento de palavras
def remover_caracteres_especiais(palavra):
    palavra = palavra.lower().replace('â', 'a').replace('ã', 'a').replace('á', 'a').replace('à', 'a').replace('ä', 'a')
    palavra = palavra.replace('ê', 'e').replace('é', 'e').replace('è', 'e').replace('ë', 'e')
    palavra = palavra.replace('î', 'i').replace('í', 'i').replace('ì', 'i').replace('ï', 'i')
    palavra = palavra.replace('ô', 'o').replace('õ', 'o').replace('ó', 'o').replace('ò', 'o').replace('ö', 'o')
    palavra = palavra.replace('û', 'e').replace('ú', 'e').replace('ù', 'e').replace('ü', 'e').upper()

    return palavra



#/////////////////////////////////
#// Import e export //////////////
#/////////////////////////////////

#----- Importações -----#
def ler_usuarios(nome_clientes, CPFs_clientes, reservas_clientes):
    reservas = []
    with open('clientes.txt', 'r') as f:
        while True:
            linha = f.readline()
            if linha == '':
                break
            nome_clientes.append(linha[:70].rstrip().title())
            CPFs_clientes.append(linha[71:82])
            reservas_clientes.append(linha[85:len(linha) - 3].split("', '"))


def ler_maquinas(codigo, tipo, marca, modelo, ano, valor, status):
    with open('maquinas.txt', 'r') as f:
        i = 0
        while True:
            linha = f.readline()

            if linha == '':
                break

            if i == 7:
                i = 0

            if i == 0:
                codigo.append(linha[:len(linha) - 1])
            elif i == 1:
                tipo.append(linha[:len(linha) - 1])
            elif i == 2:
                marca.append(linha[:len(linha) - 1])
            elif i == 3:
                modelo.append(linha[:len(linha) - 1])
            elif i == 4:
                ano.append(linha[:len(linha) - 1])
            elif i == 5:
                valor.append(float(linha[:len(linha) - 1]))
            elif i == 6:
                status.append(linha[:len(linha) - 1])
            i += 1


#----- Exportações -----#
def exportar_usuarios(nome_clientes, CPFs_clientes, reservas_clientes):
    with open('clientes.txt', 'w', encoding='utf-8') as f:
        for c in range(len(nome_clientes)):
            f.write('{: <70} {} {}\n'.format(nome_clientes[c].upper(), CPFs_clientes[c], reservas_clientes[c]))


def exportar_maquinas(codigo, tipo, marca, modelo, ano, valor, status):
    with open('maquinas.txt', 'w', encoding='utf-8') as f:
        for m in range(len(codigo)):
            f.write('{}\n{}\n{}\n{}\n{}\n{:.2f}\n{}\n'.format(codigo[m], tipo[m], marca[m], modelo[m], ano[m], valor[m], status[m]))


#/////////////////////////////////
#////// Ações ////////////////////
#/////////////////////////////////

# Mostrar o menu
def menu_de_acoes():
    print('''
[ 1 ] Cadastro de Clientes
[ 2 ] Cadastro de Máquinas para Aluguel
[ 3 ] Registro de Aluguel

- Relatórios
[ 4 ] Relatório de Clientes
[ 5 ] Relatório de Máquinas
[ 6 ] Relatório de Alugueis
[ 0 ] Sair''')
    try:
        acao = int(input('\n> '))
        assert 0 <= acao <= 6, 'Opção inválida'

    except:
        print('Oops! Algo correu mal :/')

    return acao


# Ação 1 - Cadastro de clientes
def acao1(nome_clientes, CPFs_clientes, reservas_clientes):     
    informacoes_cliente = {}
    reservas = ['0']

    try:
        print('---CADASTRO DE CLIENTES---')
        nome = input('Nome: ')
        assert len(nome) <= 70, 'Digite menos de 70 caracteres'
        nome = remover_caracteres_especiais(nome)

        cpf = input('CPF (Apenas os números): ')
        assert cpf.isnumeric(), 'Digite apenas números'
        assert len(cpf) == 11, 'CPF inválido'
        assert not cpf in CPFs_clientes, 'Este CPF já foi cadastrado'

        nome_clientes.append(nome)
        CPFs_clientes.append(cpf)
        reservas_clientes.append(reservas)

        with open('clientes.txt', 'a') as f:
            f.write('{: <70} {} {}\n'.format(nome, cpf, reservas))

        print('\n✔ Cliente registrado com sucesso')

    except:
        print('Oops! Algo correu mal :/')


# Ação 2 - Cadastro de máquinas
def acao2(codigo, tipo, marca, modelo, ano, valor, status):
    try:
        print('---CADASTRO DE MÁQUINAS---')

        code = int(input('Código (4 números): '))
        assert 0 < code <= 9999
        code = str(code).rjust(4, '0')
        
        type = input('Tipo de máquina:\n[ P ] Perfurador\n[ D ] Demolidor\n[ C ] Compactador\nEscolha um tipo (p/d/c): ').upper()
        assert type == 'P' or type == 'D' or type == 'C', 'Digite um tipo válido'

        if type == 'P':
            type = 'PERFURADOR'
        elif type == 'D':
            type = 'DEMOLIDOR'
        else:
            type = 'COMPACTADOR'
        
        mark = input('Digite a marca da máquina: ').upper()
        assert len(mark) <= 15
        
        model = input('Digite o modelo: ').upper()
        assert len(model) <= 10
        
        year = int(input('Digite o ano de fabricação: '))
        assert 0 < year <= 2021
        
        value = float(input('Digite o valor da diária: R$'))
        assert 0 < value
        
        st = input('Status ([D]isponível/[I]ndisponível): ').upper()
        assert st == 'I' or st == 'D', 'Digite um status válido'

        if st == 'I':
            st = 'INDISPONIVEL'
        else:
            st = 'DISPONIVEL'

        codigo.append(str(code))
        tipo.append(type)
        status.append(st)
        marca.append(mark)
        modelo.append(model)
        ano.append(str(year))
        valor.append(str(value))

        with open('maquinas.txt', 'a',encoding='utf-8') as f:
            f.write('{}\n{}\n{}\n{}\n{}\n{:.2f}\n{}\n'.format(code, type, mark, model, year, value, st))
        
        print('\n✔ Máquina registrada com sucesso')
    except:
        print('Algo deu errado :/')


# Ação 3 - Requisição de aluguel
def acao3(nome_clientes, CPFs_clientes, reservas_clientes, codigo, tipo, marca, modelo, ano, valor, status):
    try:
        print('---REQUISIÇÃO DE ALUGUEL---')

        print('Máquina:')
        code = input('Código da máquina: ')
        assert code.isnumeric()
        assert len(code) == 4
        assert code in codigo

        index_m = codigo.index(code)

        if status[index_m] == 'INDISPONIVEL':
            print('❌ Esta máquina está indisponível. Tente escolher outra')
        else:
            print('\nInformações do cliente: ')

            cpf = input('CPF: ')
            assert cpf.isnumeric()
            assert len(cpf) == 11
            assert cpf in CPFs_clientes

            index_c = CPFs_clientes.index(cpf)

            dias_contrat = int(input('\nDias contratados (max. 30): '))
            assert 0 < dias_contrat <= 30

            if answerConfirm(
                    f'Confirma o aluguel do {tipo[index_m]} ({codigo[index_m]}) para {nome_clientes[index_c]} ({CPFs_clientes[index_c]}) por {dias_contrat} dias? (s/n): '):

                status[index_m] = 'INDISPONIVEL'
                reservas_clientes[index_c].append(codigo[index_m])

                exportar_usuarios(nome_clientes, CPFs_clientes, reservas_clientes)
                exportar_maquinas(codigo, tipo, marca, modelo, ano, valor, status)

                valor_total = valor[index_m] * dias_contrat

                with open('Relatorio_Alugueis.txt', 'a') as f:
                    f.write(
                        f'{nome_clientes[index_c].ljust(70, " ")}  {codigo[index_m]}  {tipo[index_m].ljust(11, " ")}  R${valor_total}\n')

                print('''
✔ Contrato feito com sucesso:

Dias contratados: {}
Valor da diária: R${:.2f}
- Valor total: R${:.2f}

Máquina: {}
Código: {}

Cliente: {} ({})'''.format(dias_contrat, valor[index_m], valor_total, tipo[index_m],
                               codigo[index_m], nome_clientes[index_c], CPFs_clientes[index_c]))

            elif not answerConfirm(
                    f'Confirma o aluguel do {tipo[index_m]} ({codigo[index_m]}) para {nome_clientes[index_c]} ({CPFs_clientes[index_c]}) por {dias_contrat} dias? (s/n): '):
                print('Requisição cancelada')

    except:
        print('Oops! Algo correu mal :/')


# Ação 4 - Relatório de clientes
def acao4(nome_clientes, CPFs_clientes, reservas_clientes):
    print('''
NOME                                                                   CPF         ALUGUEIS
---------------------------------------------------------------------- ----------- ----------''')
    for cliente in range(len(nome_clientes)):
         print('{: <70} {} {}'.format(nome_clientes[cliente], CPFs_clientes[cliente], reservas_clientes[cliente]))

    with open('Relatorio_Clientes.txt', 'w', encoding='utf-8') as f:
        f.write('''NOME                                                                   CPF         ALUGUEIS
---------------------------------------------------------------------- ----------- ----------\n''')
        for cliente in range(0, len(nome_clientes)):
            f.write('{: <70} {} {}\n'.format(nome_clientes[cliente], CPFs_clientes[cliente], reservas_clientes[cliente]))

    print('\n✔️ Salvo')


# Ação 5 - Relatório de máquinas
def acao5(codigo, tipo, marca, modelo, ano, valor, status):
    print('''
CODIGO  TIPO         MARCA            MODELO      ANO     V. DIA   STATUS
--------------------------------------------------------------------------------''')
    for m in range(len(codigo)):
         print('{}    {: <11}  {: <15}  {: <10}  {:0>4}  {: >8.2f}   {: <12}'.format(codigo[m], tipo[m], marca[m], modelo[m], ano[m], valor[m], status[m]))

    with open('Relatorio_Maquinas.txt', 'w', encoding='utf-8') as f:
        f.write('''CODIGO  TIPO         MARCA            MODELO      ANO     V. DIA   STATUS
--------------------------------------------------------------------------------\n''')
        for m in range(0, len(codigo)):
            f.write('{}    {: <11}  {: <15}  {: <10}  {:0>4}  {: >8.2f}   {: <12}\n'.format(codigo[m], tipo[m], marca[m], modelo[m], ano[m], valor[m], status[m]))

    print('\n✔️ Salvo')


# Ação 6 - Relatório de reservas
def acao6():
    with open('Relatorio_Alugueis.txt', 'r') as f:
        contents = f.read()
    print(contents)
