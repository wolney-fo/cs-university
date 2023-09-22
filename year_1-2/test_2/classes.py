from webbrowser import open_new as wb
import functions.registration as reg
import functions.general as gn
from datetime import datetime, date
import pandas as pd

todayDate = date.today()
currentYear = todayDate.year


class Seller:
    def __init__(self):
        pass

    @classmethod
    def register_seller(self):
        try:
            sellersData = pd.read_excel('sellers.xlsx')
            sellersCpfs = sellersData['CPF'].to_list()

        except FileNotFoundError as error:
            sellersData = pd.DataFrame(columns=['NOME', 'CPF', 'NASCIMENTO', 'ENDEREÇO'])
            sellersCpfs = list()

        print('| Cadastrar vendedor |\n')
        while True:
            try:
                name = input('Nome: ')

                cpf = reg.cpf_validation(inuse=True, list=sellersCpfs)

                dataNas = input('Data de nascimento (dd/mm/aaaa): ')
                assert (dataNas[:2].isnumeric() and dataNas[3:5].isnumeric() and dataNas[6:].isnumeric()) and (
                            dataNas[2] == '/' and dataNas[5] == '/')
                assert (0 < int(dataNas[:2]) <= 31) and (0 < int(dataNas[3:5]) <= 12) and (
                        1920 <= int(dataNas[6:]) <= (currentYear - 18))
                dataNas = datetime(int(dataNas[6:]), int(dataNas[3:5]), int(dataNas[:2]))

                address = reg.address_validation()

            except AssertionError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except ValueError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except Exception as error:
                print('Oops! Parece que algo inesperado aconteceu.')

            else:
                try:
                    info = [name, cpf, dataNas, address]
                    sellersData.loc[len(sellersData)] = info
                    sellersData.to_excel('sellers.xlsx', index=False)

                    print('\n✔️ Vendedor cadastrado com sucesso')
                    break
                except Exception as error:
                    print('Oops! Parece que algo inesperado aconteceu.')
                    break


class Client:
    def __init__(self):
        pass

    @classmethod
    def register_client(self):
        try:
            clientsData = pd.read_excel('clients.xlsx')
            clientsCpfs = clientsData['CPF'].to_list()
        except FileNotFoundError as error:
            clientsData = pd.DataFrame(columns=['NOME', 'CPF', 'NASCIMENTO', 'ENDEREÇO'])
            clientsCpfs = list()

        print('| Cadastrar cliente |\n')
        while True:
            try:
                name = input('Nome: ')

                cpf = reg.cpf_validation(inuse=True, list=clientsCpfs)

                dataNas = input('Data de nascimento (dd/mm/aaaa): ')
                assert (dataNas[:2].isnumeric() and dataNas[3:5].isnumeric() and dataNas[6:].isnumeric()) and (
                        dataNas[2] == '/' and dataNas[5] == '/')
                assert (0 < int(dataNas[:2]) <= 31) and (0 < int(dataNas[3:5]) <= 12) and (
                        1920 <= int(dataNas[6:]) <= (currentYear - 18))
                dataNas = datetime(int(dataNas[6:]), int(dataNas[3:5]), int(dataNas[:2]))

                address = reg.address_validation()

            except AssertionError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except ValueError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except Exception as error:
                print('Oops! Parece que algo inesperado aconteceu.')

            else:
                try:
                    info = [name, cpf, dataNas, address]
                    clientsData.loc[len(clientsData)] = info

                    clientsData.to_excel('clients.xlsx', index=False)

                    print('\n✔️ Cliente cadastrado com sucesso')
                    break
                except Exception as error:
                    print('Oops! Parece que algo inesperado aconteceu.')
                    break


class Machine:
    def __init__(self):
        pass

    @classmethod
    def register_product(self):
        fileNotFound = False
        try:
            products = pd.read_excel('products.xlsx')
            productsCodes = products['CÓDIGO'].to_list()
        except FileNotFoundError as error:
            products = pd.DataFrame(columns=['CÓDIGO', 'DESCRIÇÃO', 'VALOR', 'QUANTIDADE'])
            fileNotFound = True
            productsCodes = list()

        print('📦 Estoque')

        if not fileNotFound:
            while True:
                try:
                    choice = input('[ N ] Cadastrar novo produto || [ A ] Adicionar ao estoque\n> ').upper()
                    assert choice == 'N' or choice == 'A'
                    break
                except AssertionError as error:
                    print('❗ Resposta inválida')
        else:
            choice = 'N'

        if choice == 'N':
            while True:
                try:
                    print('> Novo produto\n')
                    description = input('Descrição: ')

                    if fileNotFound is True:
                        code = 1
                    elif fileNotFound is False:
                        code = productsCodes[-1] + 1

                    value = float(input('Valor unitário: R$'))
                    assert 0 < value

                    qty = int(input('Quantidade: '))
                    assert 0 < qty

                except AssertionError as error:
                    print('🤔 Parece que alguma informação foi inserida errada\n')
                except ValueError as error:
                    print('🤔 Parece que alguma informação foi inserida errada\n')
                except Exception as error:
                    print('Oops! Parece que algo inesperado aconteceu.')

                else:
                    products.loc[len(products)] = [code, description, value, qty]

                    products.to_excel('products.xlsx', index=False)

                    print('\n✔️ Produto cadastrado com sucesso')
                    break

        elif choice == 'A':
            while True:
                try:
                    print('> Adicionar ao estoque')

                    productsQuantity = products['QUANTIDADE'].to_list()
                    productsDescriptions = products['DESCRIÇÃO'].to_list()

                    code = int(input('Código do produto: '))
                    assert code in productsCodes

                    index_m = productsCodes.index(code)

                    print(
                        f'Produto: {productsDescriptions[index_m]}\nCódigo: {code}\nQuantidade atual: {productsQuantity[index_m]}\n')
                    qty = int(input('Quantidade a adicionar: '))
                    assert 0 < qty

                except AssertionError as error:
                    print('🤔 Parece que alguma informação foi inserida errada\n')
                except ValueError as error:
                    print('🤔 Parece que alguma informação foi inserida errada\n')
                except Exception as error:
                    print('Oops! Parece que algo inesperado aconteceu.')

                else:
                    qty += productsQuantity[index_m]

                    products.loc[index_m] = [code, productsDescriptions[index_m], products.loc[index_m, 'VALOR'], qty]

                    products.to_excel('products.xlsx', index=False)

                    print('\n✔️ Estoque atualizado')
                    break


class Sale:
    def __init__(self):
        pass

    @classmethod
    def register_sale(self, user):
        data = datetime.now()
        data = str(data.day) + '/' + str(data.month) + '/' + str(data.year)

        print('░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('░░┌──┬┐░░░┌──┐░┌┐░░┌┐░░░░░░')
        print('░░└┐┌┤└┬─┐│┌┐├┬┼┼┐┌┘├─┬┬┐░░')
        print('░░░│││││┴┤│┌┐││││└┤┼│┴┤┌┘░░')
        print('░░░└┘└┴┴─┘└──┴─┴┴─┴─┴─┴┘░░░')
        print('░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('Material de construção LTDA\n\n')

        print('----------------')
        print('||| 🪙 Caixa |||')
        print('----------------')
        print(f'🗓️: {data}')
        print(f'🚹: {user}')
        print('PDV - ONLINE\n\n')

        while True:
            try:
                clientsData = pd.read_excel('clients.xlsx')
                clients_cpf = clientsData['CPF'].to_list()

                productsData = pd.read_excel('products.xlsx')
                products_codes = productsData['CÓDIGO'].to_list()
                products_value = productsData['VALOR'].to_list()
                products_qutny = productsData['QUANTIDADE'].to_list()

                cpf = str(input('Cliente (CPF): '))
                assert (cpf == '0') or (len(cpf) == 11 and cpf.isnumeric())

                print('')

                if cpf == '0':
                    print('\nPDV - OFFLINE')
                    break

                cpf = reg.cpf_format(cpf)

                if cpf in clients_cpf:  # Cliente cadastrado
                    purchase_items = pd.DataFrame(columns=['CÓDIGO', 'QTD', 'V UNITÁRIO', 'V TOTAL'])
                    amount = 0
                    while True:
                        try:
                            productCode = int(input('Produto: '))
                            a = 0
                            assert (productCode == 0) or (productCode in products_codes)

                            if productCode == 0:
                                break

                            p = products_codes.index(productCode)

                            if products_qutny[p] <= 0:
                                print('❌ Produto fora de estoque')

                            qty = int(input(f'Quantidade (1-{products_qutny[p]}): '))
                            a = 1
                            assert 1 <= qty <= products_qutny[p]

                            price = products_value[p] * qty
                            amount += price

                            info = [productCode, qty, products_value[p], price]
                            purchase_items.loc[len(purchase_items)] = info

                        except AssertionError as error:
                            if a == 0:
                                print('🔍 Produto não encontrado.')
                            elif a == 1:
                                print('❌ Quantidade superior ao estoque.')

                    # Exibir os itens
                    print('\n\n')
                    print(purchase_items)
                    print(f'------ Total: | R${amount:.2f} |')

                    if gn.answerConfirm('\nConfirmar compra? (s/n): '):
                        # Alterar o estoque e definir comissão
                        for i in range(len(purchase_items)):
                            index_p = products_codes.index(purchase_items.loc[i, 'CÓDIGO'])
                            productsData.loc[index_p, 'QUANTIDADE'] -= purchase_items.loc[i, 'QTD']
                        productsData.to_excel('products.xlsx', index=False)

                        # Salvar as comissões
                        try:
                            commissionsData = pd.read_excel('commissions.xlsx')
                            with open('getcode.txt', 'r') as f:
                                code = int(f.read())
                            code += 1
                        except FileNotFoundError:
                            commissionsData = pd.DataFrame(
                                columns=['CÓDIGO', 'DATA', 'VENDEDOR', 'V. TOTAL', 'V. COMISSÃO'])
                            code = 1
                        finally:
                            try:
                                sellersData = pd.read_excel('sellers.xlsx')
                                sellers_cpf = sellersData['CPF'].to_list()

                                index_u = sellers_cpf.index(user)

                                user = sellersData.loc[index_u, 'NOME']

                                commission = amount * 0.1

                                info = [code, todayDate, user, amount, commission]
                                commissionsData.loc[len(commissionsData)] = info
                                commissionsData.to_excel('commissions.xlsx', index=False)

                                with open('getcode.txt', 'w', encoding='UTF-8') as f:
                                    f.write(f'{code}')

                                # Salvar cupom fiscal
                                data = datetime.now()
                                data = str(data.day) + '-' + str(data.month) + '-' + str(data.year)

                                fileName = 'Venda' + '-' + str(code) + '_' + str(data) + '.txt'

                                with open(fileName, 'w', encoding='utf-8') as f:
                                    f.write('                           | CUMPOM FISCAL |                         \n')
                                    f.write(f'Data: {data}\n')
                                    f.write('Descrição                                QTD   V. Unitário   V. Total\n')
                                    f.write('---------------------------------------------------------------------\n')
                                    for pr in range(len(purchase_items)):
                                        index_p = products_codes.index(purchase_items.loc[pr, 'CÓDIGO'])
                                        description = productsData.loc[index_p, 'DESCRIÇÃO']
                                        f.write('{: <40}  {: ^3}  R${: <6}  R${: <6}\n'.format(description, purchase_items.loc[pr, 'QTD'], purchase_items.loc[pr, 'V UNITÁRIO'], purchase_items.loc[pr, 'V TOTAL']))
                                    f.write(f'Valor total: R${amount}')

                                wb(fileName)

                            except FileNotFoundError as error:
                                print('Parece que alguns arquivos sumiram e o sistema está funcionando mal')
                                exit()

                        print('\n\n😄🛍️ Volte sempre')

                # Cliente não cadastrado
                else:
                    print('Cliente não cadastrado não cadastrado')
                    if gn.answerConfirm('Gostaria de cadastra-lo agora?'):
                        Client.register_client()

            except FileNotFoundError as error:
                print('❌ Nenhum cliente foi cadastrado ainda')
                break
            except ValueError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except Exception as error:
                print('Oops! Parece que algo inesperado aconteceu.')
