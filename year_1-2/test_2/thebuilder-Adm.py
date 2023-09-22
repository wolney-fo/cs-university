from webbrowser import open_new as wb
import functions.general as gen
import pandas as pd
import classes


while True:
    print('''
               ░░░░░░░░░░░░░░░░░░░░░░░░░░░
               ░░┌──┬┐░░░┌──┐░┌┐░░┌┐░░░░░░
               ░░└┐┌┤└┬─┐│┌┐├┬┼┼┐┌┘├─┬┬┐░░
               ░░░│││││┴┤│┌┐││││└┤┼│┴┤┌┘░░
               ░░░└┘└┴┴─┘└──┴─┴┴─┴─┴─┴┘░░░
               ░░░░░░░░░░░░░░░░░░░░░░░░░░░
               Material de construção LTDA


 _______________________Cadastrar_______________________
 |   Clientes           Produtos        Usuário caixa  |
 |   [ 1 ]               [ 2 ]                  [ 3 ]  |
 -------------------------------------------------------

 ______________________Relatórios_______________________
 |  Vendedores     Produtos     Clientes    Comissões  |
 |    [ 4 ]          [ 5 ]       [ 6 ]        [ 7 ]    |
 -------------------------------------------------------

  
 [ 0 ] Sair''')

    while True:
        try:
            acao = int(input('\n> '))
            assert 0 <= acao <= 7
            break

        except AssertionError as error:
            pass
        except Exception as error:
            print('Oops! Parece que algo inesperado aconteceu.')

    if acao == 0:
        break

    elif acao == 1:
        classes.Client.register_client()

    elif acao == 2:
        classes.Machine.register_product()

    elif acao == 3:
        classes.Seller.register_seller()

    elif acao == 4:
        try:
            wb('sellers.xlsx')
        except TypeError as error:
            print('Nenhum vendedor cadastrado ainda.')
            if gen.answerConfirm('Gostaria de registrar agora? (s/n): '):
                classes.Seller.register_seller()
        except FileNotFoundError as error:
            print('Nenhum vendedor cadastrado ainda.')
            if gen.answerConfirm('Gostaria de registrar agora? (s/n): '):
                classes.Seller.register_seller()

    elif acao == 5:
        try:
            products = pd.read_excel('products.xlsx')
            print(products)
            del products
        except FileNotFoundError as error:
            print('Nenhum produto cadastrado ainda.')
            if gen.answerConfirm('Gostaria de registrar agora? (s/n): '):
                classes.Machine.register_product()

    elif acao == 6:
        try:
            wb('clients.xlsx')
        except TypeError as error:
            print('Nenhum cliente cadastrado ainda.')
            if gen.answerConfirm('Gostaria de registrar agora? (s/n): '):
                classes.Client.register_client()
        except FileNotFoundError as error:
            print('Nenhum cliente cadastrado ainda.')
            if gen.answerConfirm('Gostaria de registrar agora? (s/n): '):
                classes.Client.register_client()

    elif acao == 7:
        break

    elif acao == 8:
        try:
            commissions = pd.read_excel('commissions.xlsx')
            print(commissions)
            del commissions
        except FileNotFoundError as error:
            print('Nenhuma venda feita ainda.')
