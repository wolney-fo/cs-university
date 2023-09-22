def cpf_format(cpf):
    cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    return cpf


def cpf_validation(inuse=False, list=list):
    while True:
        try:
            cpf = input('CPF: ')
            assert (len(cpf) == 11 and cpf.isnumeric()) or (len(cpf) == 14 and (cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-') and cpf[:3].isnumeric() and cpf[4:7].isnumeric() and cpf[8:11].isnumeric() and cpf[12:].isnumeric())
            cpf = cpf_format(cpf)

            if inuse:
                if cpf in list:
                    while True:
                        try:
                            print('\nCPF já cadastrado!!')
                            cpf = input('CPF: ')
                            assert len(cpf) == 11 and cpf.isnumeric()
                            cpf = cpf_format(cpf)
                            if not cpf in list:
                                break
                        except AssertionError:
                            print('CPF inválido. Tente novamente.')
                        except Exception as error:
                            print('Oops! Algo inesperado aconteceu.')

        except AssertionError:
            print('CPF inválido. Tente novamente.')
        except Exception as error:
            print('Oops! Algo inesperado aconteceu.')
        else:
            return cpf


def address_validation():
    street = input('Rua/Avenida: ').title()
    numb = input('Número: ')
    district = input('Bairro: ').title()
    zip_code = input('CEP: ')
    town = input('Município: ').title()
    fu = input('Estado: ').title()
    address = f'{street}, {numb} - {district}, {town} - {fu}, {zip_code}'

    return address


def cpf_validator(list):
    while True:
        try:
            cpf = input('CPF: ')
            assert (len(cpf) == 11 and cpf.isnumeric()) or (len(cpf) == 14 and (cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-') and cpf[:3].isnumeric() and cpf[4:7].isnumeric() and cpf[8:11].isnumeric() and cpf[12:].isnumeric())
            cpf = cpf_format(cpf)

            if cpf in list:
                return cpf, client_name
            else:
                print('Cliente não encontrado')

        except AssertionError:
            print('CPF inválido. Tente novamente.')
        except Exception as error:
            print('Oops! Algo inesperado aconteceu.')
