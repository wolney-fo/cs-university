from random import sample


# Letra A
qtd_dezenas = int(input('Quantidade de dezenas (15-18): '))
while not (15 <= qtd_dezenas <= 18):
    print('Digite apenas números de 15 a 18!!')
    qtd_dezenas = int(input('Quantidade de dezenas (15-18): '))


# Letra B
numeros_aposta = list()
for n in range(qtd_dezenas):
    num = int(input(f'{n + 1}º dezena: '))
    while not (0 < num <= 25) or (num in numeros_aposta):
        if num in numeros_aposta:
            print('Não repita números!!')
        else:
            print('Digite apenas dígitos de 1 a 25!!')
        num = int(input(f'{n + 1}º dezena: '))
    numeros_aposta.append(num)


# Letra C
surpresinha_1 = sample(range(1, 26), 18)
surpresinha_2 = sample(range(1, 26), 18)


# Letra D
resultado = sample(range(1, 26), 18)


# Tratamento
numeros_aposta.sort()
surpresinha_1.sort()
surpresinha_2.sort()
resultado.sort()


print(f'''

Aposta 1:
{numeros_aposta}

Surpresinha 1:
{surpresinha_1}

Surpresinha 2:
{surpresinha_2}

||| RESULTADO: {resultado} |||''')
