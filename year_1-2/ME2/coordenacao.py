import classes


while True:
    print('''

A ACADEMIA DE ARACAJU 🏫
🚹: Coordenação

[ 1 ] Cadastrar professores
[ 2 ] Cadastrar alunos
[ 3 ] Cadastrar disciplinas
[ 0 ] Sair
''')

    while True:
        try:
            acao = int(input('> '))
            assert 0 <= acao <= 3

        except ValueError as error:
            pass
        except AssertionError as error:
            print('(0-3)', end='')
        else:
            break

    if acao == 0:
        break

    elif acao == 1:
        classes.Professor()

    elif acao == 2:
        classes.Aluno()

    elif acao == 3:
        classes.Disciplina()
