import functions


# Veterinários
nome_vet = []
CPFs_Veterinarios = []
cfmv_vet = []
status_vet = []
sexo_vet = []
atendendo_vet = []
functions.ler_vet(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet)

# Pets
nome_pet = []
code_pet = []
especiesList = []
functions.ler_pets(nome_pet, code_pet, especiesList)

# Consultas
datas_consultas = []
cfmvVet_consultas = []
nomeVet_consultas = []
codePet_consultas = []
nomePet_consultas = []
status_consultas = []
valores_consultas = []
functions.ler_consultas(datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas)


while True:
    try:
        acao = functions.menu_de_acoes()
        #acao = 0

        if acao == 0:
            break

        elif acao == 1:
            functions.acao1(nome_vet, CPFs_Veterinarios, cfmv_vet, sexo_vet, status_vet, atendendo_vet)

        elif acao == 2:
            functions.acao2(nome_vet, CPFs_Veterinarios, cfmv_vet, sexo_vet, status_vet, atendendo_vet)

        elif acao == 3:
            functions.acao3(nome_pet, code_pet, especiesList)

        elif acao == 4:
            functions.acao4(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet, nome_pet, code_pet, especiesList, datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas)

        elif acao == 5:
            functions.acao5(nome_vet, CPFs_Veterinarios, cfmv_vet, status_vet, sexo_vet, atendendo_vet, code_pet, datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas)

        elif acao == 6:
            functions.acao6(nome_pet, code_pet, especiesList)

        elif acao == 7:
            functions.acao7(nome_vet, CPFs_Veterinarios, cfmv_vet, sexo_vet, status_vet, atendendo_vet)

        else:
            functions.acao8(datas_consultas, cfmvVet_consultas, nomeVet_consultas, codePet_consultas, nomePet_consultas, status_consultas, valores_consultas)

    except:
        print('Oops! Algo correu mal :/')
0