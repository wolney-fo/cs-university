from random import randint



with open('palavras.txt', 'r') as f:
    palavras = []
    while True:
        palavra = f.readline()
        if palavra == '':
            break
        palavras.append(palavra[:-1])


palavra = palavras[randint(0, 277)]

del palavras

palavra_mascarada = ['_' for letra in palavra]

x = ('_' for letra in palavra)


erros_contador = 0
letras_usadas = list()


print('\n\n\nVocê tem 3 chances.\nBoa sorte 😉\n')


for l in x:
    print(l, end='')
print(f'\n{len(palavra)} letras\n')


while True:
    if not '_' in palavra_mascarada:
        print('VITÓRIA!! 🎊🎊🎊')
        break


    letra = input('Letra: ').upper()
    assert len(letra) == 1


    while letra in letras_usadas:
        print('\nVocê já tentou essa letra 😶')
        letra = input('Letra: ').upper()
        assert len(letra) == 1

    letras_usadas.append(letra)


    print('\nTentativas:', letras_usadas)


    if letra in palavra:
        for l in range(len(palavra)):
            if palavra[l] == letra:
                palavra_mascarada[l] = letra

        print('\n', palavra_mascarada)

    else:
        erros_contador += 1

        if erros_contador == 1:
            print('  ______\n  |   😦\n  |\n  |\n---------')
            print('Restam duas chance')
        elif erros_contador == 2:
            print('  ______\n  |   😰\n  |   |\n  |\n---------')
            print('Resta uma chance')
        else:
            print('  ______\n  |   💀\n  |   |\n  |   /\ \n---------')
            print('FIM DE JOGO')
            print(f"A palavra era '{palavra}'")
            break

        print('\n', palavra_mascarada)
        print('Errou 😓')
