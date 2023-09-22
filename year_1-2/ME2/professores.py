from webbrowser import open_new as wb
from datetime import datetime
from time import sleep
import pandas as pd

def login():
    while True:
        try:
            df = pd.read_excel('disciplinas.xlsx')
            matrList = df['MATRICULAPROF'].to_list()
            nomeList = df['NOME'].to_list()

            matricula = int(input('Matrícula do professor: '))
            assert 1000 <= matricula <= 9999

            index = matrList.index(matricula)

            disciplina = nomeList[index]

        except ValueError as error:
            print('🤨 Matrícula inválida!!')
        except AssertionError as error:
            print('🕵️‍♂ Usuário não encontrado')
        except FileNotFoundError as error:
            print('🔍 Nenhuma matrícula encontrado')
            exit()
        except Exception as error:
            print('Oops! Parece que algo inesperado aconteceu.')
            exit()

        else:
            return disciplina

disciplina = login()

while True:
    print(f'''

A ACADEMIA DE ARACAJU 🏫
📖: {disciplina}

[ 1 ] Fazer chamada
[ 0 ] Sair
''')

    while True:
        try:
            acao = int(input('> '))
            assert (acao == 1) or (acao == 0)

        except ValueError as error:
            pass
        except AssertionError as error:
            print('(0/1)', end='')

        else:
            break


    if acao == 0:
            break


    if acao == 1:
        data = datetime.now()
        data = str(data.day) + '/' + str(data.month) + '/' + str(data.year)
        alunData = pd.read_excel('alunos.xlsx')
        fileName = 'CHAMADA_' + disciplina.replace(' ', '-').upper() + '-' + data.replace('/', '-') + '.docx'
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write(f'Chamada {disciplina.title()}                                  {data}\n\n')
            for a in range(len(alunData)):
                x = input(f'[{alunData.loc[a, "MATRICULA"]}] {alunData.loc[a, "NOME"]} (P/F): ').upper()
                while (x != 'P') and (x != 'F'):
                    x = input(f'[{alunData.loc[a, "MATRICULA"]}] {alunData.loc[a, "NOME"]} (P/F): ').upper()
                if x == 'P':
                    f.write(f'[{alunData.loc[a, "MATRICULA"]}] {alunData.loc[a, "NOME"]} PRESENTE\n')
                else:
                    f.write(f'[{alunData.loc[a, "MATRICULA"]}] {alunData.loc[a, "NOME"]} FALTOU\n')

        print('⬇️Salvando arquivo')
        sleep(1)

        wb(fileName)
