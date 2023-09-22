from random import randint

#----- Ações de uso geral-----#

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


#-----Leitura de dados-----#

# Veterinários
def ler_vet(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet):
    with open('veterinarios.txt', 'r') as f:
        while True:
            linha = f.readline()
            if linha == '':
                break
            nome_vet.append(linha[:70].rstrip())
            CPFs_Veterinarios.append(linha[71:82])
            cfmv_vet.append(linha[83:87])
            status_vet.append(linha[88:95].lstrip())
            sexo_vet.append(linha[96:98].strip())
            atendendo_vet.append(linha[102:len(linha) - 3].split("', '"))


# Pets
def ler_pets(nome_pet, code_pet, especiesList):
    with open('pets.txt', 'r') as f:
        while True:
            linha = f.readline()
            if linha == '':
                break
            nome_pet.append(linha[:40].rstrip())
            code_pet.append(linha[41:47])
            especiesList.append(linha[48:len(linha) - 1])


# Consultas
def ler_consultas(datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas):
    with open('consultas.txt', 'r') as f:
        i = 0
        while True:
            linha = f.readline()

            if linha == '':
                break

            if i == 7:
                i = 0

            if i == 0:
                datas_consultas.append(linha[:len(linha) - 1])
            elif i == 1:
                cfmvVet_consultas.append(linha[:len(linha) - 1])
            elif i == 2:
                nomeVet_consultas.append(linha[:len(linha) - 1])
            elif i == 3:
                codePet_consultas.append(linha[:len(linha) - 1])
            elif i == 4:
                nomePet_consultas.append(linha[:len(linha) - 1])
            elif i == 5:
                status_consultas.append(linha[:len(linha) - 1])
            elif i == 6:
                valores_consultas.append(float(linha[:len(linha) - 1]))
            i += 1


#-----Gravação de dados-----#

# Veterinários
def gravar_vet(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet):
    with open('veterinarios.txt', 'w', encoding='utf-8') as f:
        for vet in range(len(nome_vet)):
            f.write('{: <70} {} {} {: >7}  {}  {}\n'.format(nome_vet[vet], CPFs_Veterinarios[vet], cfmv_vet[vet], status_vet[vet], sexo_vet[vet], atendendo_vet[vet]))


# Pets
def gravar_pet(nome_pet, code_pet, especiesList):
    with open('pets.txt','w',encoding='utf-8') as f:
        for pet in range(len(nome_pet)):
            f.write(f'{nome_pet[pet]:<40} {code_pet[pet]} {especiesList[pet]}\n')


# Consultas
def gravar_consultas(datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas):
    with open('consultas.txt', 'w', encoding='utf-8') as f:
        for c in range(len(datas_consultas)):
            f.write(f'{datas_consultas[c]}\n')

            f.write(f'{cfmvVet_consultas[c]}\n')
            f.write(f'{nomeVet_consultas[c]}\n')

            f.write(f'{codePet_consultas[c]}\n')
            f.write(f'{nomePet_consultas[c]}\n')

            f.write(f'{status_consultas[c]}\n')
            f.write(f'{valores_consultas[c]}\n')


#----- Ações do menu-----#

# Mostrar o menu
def menu_de_acoes():
    print('''
[ 1 ] Cadastro de veterinários
[ 2 ] Alterar status do funcionário
[ 3 ] Cadastro de pet
[ 4 ] Registrar consulta
[ 5 ] Cancelar consulta

-Relatórios
[ 6 ] Pets
[ 7 ] Veterinários ativos
[ 8 ] Consusltas (por data)
[ 0 ] Sair''')

    try:
        acao = int(input('\n> '))
        assert 0 <= acao <= 8, 'Opção inválida'

    except:
        print('Oops! Algo correu mal :/')

    return acao


# Ação 1 - Cadastrar veterinários
def acao1(nome_vet, CPFs_Veterinarios, cfmv_vet, sexo_vet, status_vet, atendendo_vet):
    print('---CADASTRAR VETERINÁRIO---')
    emptyList = ['0']

    try:
        cfmv = input('CFMV: ')
        assert cfmv.isnumeric() and len(cfmv) == 4, 'CFMV inválido'
        assert cfmv not in cfmv_vet, 'CFMV já cadastrado'

        cpf = input('CPF: ')
        assert cpf.isnumeric() and len(cpf) == 11, 'CPF inválido'
        assert not cpf in CPFs_Veterinarios, 'Este CPF já foi cadastrado'

        nome = input('Nome: ').strip()
        assert len(nome) <= 70
        nome = remover_caracteres_especiais(nome)

        sexo = input('Sexo[F(Feminino)/M(Masculino)]: ').upper()
        assert sexo == 'F' or sexo == 'M'

        status = input('Status (ativo/inativo): ').upper()
        assert status == 'ATIVO' or status == 'INATIVO'

        nome_vet.append(nome)
        CPFs_Veterinarios.append(cpf)
        cfmv_vet.append(cfmv)
        sexo_vet.append(sexo)
        status_vet.append(status)
        atendendo_vet.append(emptyList)

        with open('veterinarios.txt', 'a') as f:
            f.write('{: <70} {} {} {: >7}  {}  {}\n'.format(nome, cpf, cfmv, status, sexo, emptyList))

        print(f'\n✔ {nome.title()} ({cfmv}) cadastrado com sucesso')

    except:
        print('Oops! Algo correu mal :/')


# Ação 2 - Alterar o status do veterinário
def acao2(nome_vet, CPFs_Veterinarios, cfmv_vet, sexo_vet, status_vet, atendendo_vet):
    print('---ALTERAR STATUS DO VETERINÁRIO---')

    try:
        cfmv = input('CFMV: ')
        assert cfmv.isnumeric() and len(cfmv) == 4, 'CFMV inválido'
        assert cfmv in cfmv_vet, 'CFMV não encontrado'

        index_v = cfmv_vet.index(cfmv)

        if status_vet[index_v] == 'ATIVO':
            if answerConfirm(f'{nome_vet[index_v]} está ATIVO. Tornar INATIVO? (s/n): '):
                status_vet[index_v] = 'INATIVO'
                print(f'{nome_vet[index_v]} agora está INATIVO')
            else:
                print('Operação cancelada')
        else:
            if answerConfirm(f'{nome_vet[index_v]} está INATIVO. Tornar ATIVO? (s/n): '):
                status_vet[index_v] = 'ATIVO'
                print(f'{nome_vet[index_v]} agora está ATIVO')
            else:
                print('Operação cancelada')

        gravar_vet(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet)


    except:
        print('Oops! Algo correu mal :/')


#Ação 3 - cadastrar pets
def acao3(nome_pet,code_pet,especiesList):
    try:
        print('---CADASTRAR PET---')

        especie = input('Espécie: ')
        especie = remover_caracteres_especiais(especie)
        assert especie == 'CACHORRO' or especie == 'GATO' or especie == 'PASSARO'

        nome = input('Nome: ')
        assert 0 < len(nome) <= 40, 'Digite até 40 caracteres'
        nome = remover_caracteres_especiais(nome)

        code = randint(1, 999999)
        while code in code_pet:
            code = randint(1, 999999)
        code = str(code)
        code = code.rjust(6, '0')

        nome_pet.append(nome)
        code_pet.append(code)
        especiesList.append(especie)

        gravar_pet(nome_pet, code_pet, especiesList)

        print(f'\n✔ O {especie.title()} {nome} foi cadastrado com sucesso :)\nCódigo de identificação: {code}')

    except:
        print('Oops! Algo correu mal :/')


#Ação 4 - Agendar consulta
def acao4(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet, nome_pet, code_pet, especiesList, datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas
):
    print('---AGENDAR CONSULTA---')

    try:
        cfmv = input('CFMV do veterinário: ')
        assert len(cfmv) == 4, 'CFMV inválido'
        assert cfmv in cfmv_vet, 'CFMV não cadastrado'

        index_v = cfmv_vet.index(cfmv)

        if status_vet[index_v] == 'ATIVO':
            data = input('Data (apenas os números):')
            assert data.isnumeric(), 'Digite apenas números'
            assert (0 < int(data[:2]) <= 31 and 0 < int(data[2:4]) <= 12 and 2021 <= int(data[4:]) < 2023) or (len(data) == 8), 'Data inválida'

            code = input('Código do pet: ')
            assert len(code) == 6, 'Código inválido'
            assert code in code_pet, 'Pet não encontrado'

            index_p = code_pet.index(code)

            if especiesList[index_p] == 'CACHORRO':
                valor = 100.0
            elif especiesList[index_p] == 'GATO':
                valor = 120.0
            elif especiesList[index_p] == 'PASSARO':
                valor = 150.0

            print('''
---Detalhes da consulta---
Paciente: {}
Espécie: {}

Veterinário: {}

Data: {}/{}/{}
Valor da consulta: R${:.2f}\n'''.format(nome_pet[index_p], especiesList[index_p], nome_vet[index_v], data[:2], data[2:4], data[4:], valor))

            if answerConfirm('Confirmar consulta? (s/n): '):
                atendendo_vet[index_v].append(code_pet[index_p])

                # Salvar consultas
                datas_consultas.append(data)

                cfmvVet_consultas.append(cfmv_vet[index_v])
                nomeVet_consultas.append(nome_vet[index_v])

                codePet_consultas.append(code_pet[index_p])
                nomePet_consultas.append(nome_pet[index_p])

                status_consultas.append('ATIVO')
                valores_consultas.append(valor)

                with open('consultas.txt', 'a') as f:
                    f.write(f'{data}\n')

                    f.write(f'{cfmv_vet[index_v]}\n')
                    f.write(f'{nome_vet[index_v]}\n')

                    f.write(f'{code_pet[index_p]}\n')
                    f.write(f'{nome_pet[index_p]}\n')

                    f.write(f'ATIVO\n')
                    f.write(f'{valor}\n')

                gravar_vet(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet)

                print('\n✔ Consulta marcada')

            else:
                print('Consulta não foi marcada')

        elif status_vet[index_v] == 'INATIVO':
            print('Veterinário INATIVO. Por favor, escolha outro.')

    except:
        print('Oops! Algo correu mal :/')



# Ação 5 - Cancelar consulta
def acao5(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet, code_pet, datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas):
    print('---CANCELAR CONSULTA---')

    data = input('Data marcada: ')
    assert data.isnumeric(), 'Digite apenas números'
    assert (0 < int(data[:2]) <= 31 and 0 < int(data[2:4]) <= 12 and 2021 <= int(data[4:]) < 2023) or (len(data) == 8), 'Data inválida'
    assert data in datas_consultas, 'Não foram encontradas consultas nesta data'

    cfmv = input('CFMV do veterinário: ')
    assert len(cfmv) == 4, 'CFMV inválido'
    assert cfmv in cfmv_vet, 'CFMV não cadastrado'
    assert cfmv in cfmvVet_consultas, 'Este veterinário não tem consultas na data informada'

    code = input('Código do pet: ')
    assert len(code) == 6, 'Código inválido'
    assert code in code_pet, 'Pet não encontrado'
    assert code in codePet_consultas, 'Este pet não tem consultas na data informada'

    index_v = cfmv_vet.index(cfmv)  # Index do veterinário

    index_c = codePet_consultas.index(code)  # Index em consultas

    if answerConfirm(
            f'Cancelar a consulta de {nomePet_consultas[index_c]} na data {data[:2]}/{data[2:4]}/{data[4:]}? (s/n): '):
        atendendo_vet[index_v].remove(code)

        status_consultas[index_c] = 'INATIVA'

        valores_consultas[index_c] = 0.0

        gravar_consultas(datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas)
        gravar_vet(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet)

        print('\n✔️ Consulta cancelada')

    else:
        print('\n❌ Operação cancelada')


# Ação 6 - Relatório de pets
def acao6(nome_pet,code_pet,especiesList):
    print('---RELATÓRIO DE PETS---')
    try:
        print('''
NOME                                     | CODIGO | ESPECIE
-------------------------------------------------------------''')     # Exibir
        for p in range(len(nome_pet)):
            print(f'{nome_pet[p].ljust(40, " ")} | {code_pet[p]} | {especiesList[p]}')

        with open('Relatorio_Pets.txt', 'w', encoding='utf-8') as f:  # Salvar
            f.write('''
NOME                                     | CODIGO | ESPECIE
-------------------------------------------------------------\n''')
            for p in range(len(nome_pet)):
                f.write(f'{nome_pet[p].ljust(40, " ")} | {code_pet[p]} | {especiesList[p]}\n')

        print('\n✔️ Salvo')

    except:
        print('Oops! Algo correu mal :/')


# Ação 7 - Relatório de veterinários ativos
def acao7(nome_vet, CPFs_Veterinarios, cfmv_vet, sexo_vet, status_vet, atendendo_vet):
    try:
        print('---RELATÓRIO DE VETERINÁRIOS ATIVOS---')
        print('''
NOME                                                                   CPF         CFMV  STATUS SEX PACIENTES
---------------------------------------------------------------------------------------------------------------''')
        for v in range(len(CPFs_Veterinarios)):
            if status_vet[v] == 'ATIVO':
                print('{: <70} {} {} {: >7}  {}  {}'.format(nome_vet[v], CPFs_Veterinarios[v], cfmv_vet[v], status_vet[v], sexo_vet[v], atendendo_vet[v]))

        with open('Relatorio_Veterinarios.txt', 'w', encoding='utf-8') as f:
            f.write('''NOME                                                                   CPF         CFMV  STATUS SEX PACIENTES
---------------------------------------------------------------------------------------------------------------\n''')
            for v in range(0, len(CPFs_Veterinarios)):
                if status_vet[v] == 'ATIVO':
                    f.write('{: <70} {} {} {: >7}  {}  {}\n'.format(nome_vet[v], CPFs_Veterinarios[v], cfmv_vet[v], status_vet[v], sexo_vet[v], atendendo_vet[v]))

        print('\n✔️ Salvo')

    except:
        print('Oops! Algo correu mal :/')


# Ação 8 - Relatório de consultas
def acao8(datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas):
    print('---RELATÓRIO DE CONSULTAS---')

    data = input('Data: ')
    assert data.isnumeric(), 'Digite apenas números'
    assert (0 < int(data[:2]) <= 31 and 0 < int(data[2:4]) <= 12 and 2021 <= int(data[4:]) < 2023) or (len(data) == 8), 'Data inválida'

    if not data in datas_consultas:
        print(f'Não foram agendadas consultas no dia {data[:2]}/{data[2:4]}/{data[4:]}')

    elif data in datas_consultas:
        nomeArquivo = 'Relatorio_Consultas_' + data + '.txt'
        print('''
DATA        CFMV  VETERINARIO                                                             C. PET  PET                                       STATUS   V. CONSULTA
-----------------------------------------------------------------------------------------------------------------------------------------------------------------''')
        receita_diaria = 0
        with open(nomeArquivo, 'w', encoding='utf-8') as f:
            f.write('''DATA        CFMV  VETERINARIO                                                             C. PET  PET                                       STATUS   V. CONSULTA
-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n''')
            for c in range(len(datas_consultas)):
                if datas_consultas[c] == data:
                    receita_diaria += valores_consultas[c]
                    print('{}/{}/{}  {}  {: <70}  {}  {: <40}  {: >7}  R${:.2f}'.format(data[:2], data[2:4], data[4:], cfmvVet_consultas[c], nomeVet_consultas[c], codePet_consultas[c], nomePet_consultas[c], status_consultas[c], valores_consultas[c]))
                    f.write('{}/{}/{}  {}  {: <70}  {}  {: <40}  {: >7}  R${:.2f}\n'.format(data[:2], data[2:4], data[4:], cfmvVet_consultas[c], nomeVet_consultas[c], codePet_consultas[c], nomePet_consultas[c], status_consultas[c], valores_consultas[c]))
            print('\n-------------------------------------\nValor arrecadado: R${:.2f}'.format(receita_diaria))
            f.write('\n-------------------------------------\nValor arrecadado: R${:.2f}'.format(receita_diaria))

            print('\n✔️ Salvo')
