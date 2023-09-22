import functions.registration as reg
import pandas as pd
import classes

while True:
    try:
        usersData = pd.read_excel('sellers.xlsx')
        users_cpf = usersData['CPF'].to_list()

        print('\n\n\nAtivar ponto de venda\n')
        print('Entrar como operador')
        user = input('Usuário: ')
        assert (len(user) == 11 and user.isnumeric())

        user = reg.cpf_format(user)
        assert user in users_cpf

        break

    except AssertionError as error:
        print('Usuário inválido')
    except FileNotFoundError as error:
        print('Nenhum usuário encontrado. Entre em contato a administração')
        exit()
    except ValueError as error:
        print('Informação inserida de forma errada')
    except Exception as error:
        print('Oops! Parece que algo inesperado aconteceu.')


classes.Sale.register_sale(user)
