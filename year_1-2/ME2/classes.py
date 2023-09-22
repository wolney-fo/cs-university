import pandas as pd
import datetime


todayDate = datetime.date.today()
currentYear = todayDate.year


class Professor:
    def __init__(self):
        profData = pd.read_excel('professores.xlsx')

        print('| ➕👩‍🏫 | Cadastrar professor')
        while True:
            try:
                nome = input('Nome: ').strip().title()

                dataNas = input('Data de nascimento (dd/mm/aaaa): ')
                assert (dataNas[:2].isnumeric() and dataNas[3:5].isnumeric() and dataNas[6:].isnumeric()) and (
                            dataNas[2] == '/' and dataNas[5] == '/')
                assert (0 < int(dataNas[:2]) <= 31) and (0 < int(dataNas[3:5]) <= 12) and (
                            1920 <= int(dataNas[6:]) <= (currentYear - 18))
                dataNas = datetime.datetime(int(dataNas[6:]), int(dataNas[3:5]), int(dataNas[:2]))

                matricula = profData.loc[len(profData) - 1, 'MATRICULA'] + 1

            except AssertionError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except Exception as error:
                print('Oops! Parece que algo inesperado aconteceu.')

            else:
                try:
                    dados = [nome, dataNas, matricula]
                    profData.loc[len(profData)] = dados

                    profData.to_excel('professores.xlsx', index=False)

                    print(f'\nProfessor(a) {nome.title()} cadastrado com sucesso')
                    break
                except:
                    print('Oops! Parece que algo inesperado aconteceu.')
                    break


        self.nome = nome
        self.dataNas = dataNas
        self.matricula = matricula


class Aluno:
    def __init__(self):
        alunData = pd.read_excel('alunos.xlsx')

        print('| ➕🎒 | Cadastrar aluno')
        while True:
            try:
                nome = input('Nome: ').strip().title()

                dataNas = input('Data de nascimento (dd/mm/aaaa): ')
                assert (dataNas[:2].isnumeric() and dataNas[3:5].isnumeric() and dataNas[6:].isnumeric()) and (
                        dataNas[2] == '/' and dataNas[5] == '/')
                assert (0 < int(dataNas[:2]) <= 31) and (0 < int(dataNas[3:5]) <= 12) and (
                        1920 <= int(dataNas[6:]))
                dataNas = datetime.datetime(int(dataNas[6:]), int(dataNas[3:5]), int(dataNas[:2]))

                matricula = alunData.loc[len(alunData) - 1, 'MATRICULA'] + 1

            except AssertionError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except Exception as error:
                print('Oops! Parece que algo inesperado aconteceu.')

            else:
                try:
                    dados = [nome, dataNas, matricula]
                    alunData.loc[len(alunData)] = dados

                    alunData.to_excel('alunos.xlsx', index=False)

                    print(f'\n✔ Aluno(a) {nome.title()} cadastrado com sucesso')
                    break
                except:
                    print('Oops! Parece que algo inesperado aconteceu.')
                    break


        self.nome = nome
        self.dataNas = dataNas
        self.matricula = matricula


class Disciplina:
    def __init__(self):
        discData = pd.read_excel('disciplinas.xlsx')

        print('| ➕📖 | Cadastrar disciplina')
        while True:
            try:
                codigo = discData.loc[len(discData) - 1, 'CODIGO'] + 1

                nome = input('Nome: ').strip().title()

                matriculaProf = int(input('Matrícula do professor: '))
                assert 1000 <= matriculaProf <= 9999

            except AssertionError as error:
                print('🤔 Parece que alguma informação foi inserida errada\n')
            except Exception as error:
                print('Oops! Parece que algo inesperado aconteceu.')

            else:
                try:
                    dados = [nome, matriculaProf, codigo]
                    discData.loc[len(discData)] = dados

                    discData.to_excel('disciplinas.xlsx', index=False)

                    print(f'\n✔ Matéria cadastrada com sucesso')
                    break
                except:
                    print('Oops! Parece que algo inesperado aconteceu.')
                    break

        self.codigo = codigo
        self.nome = nome
        self.matricula = matriculaProf
