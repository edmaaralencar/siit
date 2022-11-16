import random
import time
from os import system

from auth_functions import acesso_conta, criar_conta, select_users
from mock_data import roteiros
from sql_functions import connect_to_database, get_attractions
from credits_functions import siit, credit

connection = connect_to_database()
atracoes = get_attractions(connection)
contas = []

system('cls')

meu_roteiro = []
meus_roteiros = []

roteiro_aleatorio = []
menu = {
    1: 'Roteiros',
    2: 'Roteiro Personalizado',
    3: 'Roteiro Aleatório',
    0: 'Sair'
}
#MENU PRINCIPAL
def menu_principal(not_first_run):
    system('cls') 
    siit()

    contas = select_users(connection)

    logado = False
    firstRun = True

    if not_first_run:
        firstRun = False
        logado = True
    else:
        firstRun = True

    if firstRun == True:
        while logado == False:
            print("\nLOGIN\n",
                "1 - Entrar\n",
                "2 - Criar nova conta",
                "\n 0 - Sair")
            login_opcao = int(input("\nDigite sua opção: "))
            if login_opcao == 2:
                criar_conta(contas, connection)

            elif login_opcao == 1:
                contas = select_users(connection)
                logado = acesso_conta(contas)
            elif login_opcao == 0:
                credit()
                exit()
    print('\n')

    while logado == True:
        for key in menu.keys():
            print (key, '-', menu[key])
        opcao = int(input('\nDigite sua opção: '))
        if opcao == 0:
            credit()
            exit()
        elif opcao == 1:
            menu_roteiros()
        elif opcao == 2:
            menu_meu_roteiro()
        elif opcao == 3:
            role_aleatorio()
        else:
            print("\nOpcão inválida")

# ROTEIROS PRONTOS
def menu_roteiros():
    system('cls')
    while True:
        print("\nROTEIROS\n")
        for roteiro in roteiros:
            print(roteiro["ID"], "-", roteiro["NOME"])
        print("0 - Voltar")
        opcao = int(input('\nDigite sua opção: '))
        for roteiro in roteiros:
            if opcao == roteiro['ID']:
                system('cls')
                print(f"\n{roteiro['NOME']}\n")
                for atracao in roteiro['ATRACOES']:
                    print(atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
                print("1 - Exportar Roteiro\n"
                      "0 - Voltar\n")
                print_roteiro = int(input("Digite sua opção: "))
                if print_roteiro == 1: #EXPORTA TXT DO ROTEIRO
                    export = open(f"{roteiro['NOME']}.txt","a", encoding="utf8")
                    for atracao in roteiro['ATRACOES']:
                        export.write(f"{atracao['NOME']}\n")
                        export.write(f"\t {atracao['DESCRICAO']} \n")
                    export.close()
                    system('cls')
                    menu_roteiros()
                elif print_roteiro ==0:
                    system('cls')
                    menu_roteiros()
            elif opcao == 0:
                system('cls')
                menu_principal(True)

#ROTEIRO PERSONALIZADOS
def menu_meu_roteiro():
    system('cls')
    while True:
        opcao = int(input('\nMEUS ROTEIROS\n\n'
                            '1 - Buscar passeios\n'
                            '2 - Ver meu roteiro\n'
                            '3 - Ver roteiros salvos\n'
                            '0 - Voltar\n'
                            '\nDigite sua opção: '))
        #1 - BUSCAR PASSEIOS
        if opcao== 1:
            buscar_passeios()
        #2 - VER MEU ROTEIRO
        elif opcao == 2:
            system('cls')
            if len(meu_roteiro)==0:
                print("\n Não há atrações adicionadas ao seu roteiro")
                time.sleep(1)
                print(".\n")
                time.sleep(1)
                print(".\n")
                menu_meu_roteiro()
            else:
                for atracao in meu_roteiro:
                    print("\n", atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")

                print("1 - Salvar meu roteiro\n"
                      "0 - Voltar\n")
                save_roteiro = int(input("Digite sua opção: "))
                if save_roteiro == 1:
                    id=0
                    for roteiro in meus_roteiros:
                        if roteiro['ID']>id:
                            id=roteiro['ID']
                    nome = input("Digite o nome do seu roteiro: ")
                    meu_roteiro_copy=meu_roteiro.copy()
                    meus_roteiros_dict = {"ID": id+1 ,
                                        "NOME": nome,
                                        "ATRACOES": meu_roteiro_copy
                                        }
                    meus_roteiros.append(meus_roteiros_dict)
                    meu_roteiro.clear()
                    system('cls')
                elif save_roteiro ==0:
                    menu_meu_roteiro()
        #VER ROTEIROS SALVOS
        elif opcao == 3:
            if len(meus_roteiros)==0:
                print("\nNão há roteiros salvos")
                time.sleep(1)
                print(".\n")
                time.sleep(1)
                print(".\n")
                menu_meu_roteiro()
            else:
                system('cls')
                while True:
                    print("\nMEUS ROTEIROS\n")
                    for roteiro in meus_roteiros:
                        print(roteiro["ID"], "-", roteiro["NOME"])
                    print("\n0 - Voltar")
                    opcao = int(input('\nDigite sua opção: '))
                    for roteiro in meus_roteiros:
                        if opcao == roteiro['ID']:
                            system('cls')
                            print(f"\n{roteiro['NOME']}\n")
                            for atracao in roteiro['ATRACOES']:
                                print(atracao['NOME'])
                                print("\t",atracao['DESCRICAO'],"\n")
                            del_roteiro=int(input("1 - Exportar roteiro\n"
                                                "0 - Voltar\n"
                                                "\nDigite sua opção: "))
                            if del_roteiro == 1:
                                export = open(f"{roteiro['NOME']}.txt","a", encoding="utf8")
                                for atracao in roteiro['ATRACOES']:
                                    export.write(f"{atracao['NOME']}\n")
                                    export.write(f"\t {atracao['DESCRICAO']} \n")
                                export.close()
                            else:
                                menu_meu_roteiro()
                        elif opcao == 0:
                            system('cls')
                            menu_meu_roteiro()
        #4 - VOLTAR
        elif opcao==0:
            system('cls')
            menu_principal(True)

def role_aleatorio():
    system('cls')
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    time.sleep(1)
    print(".\n")
    num_atracoes_alea=random.randint(2,4)
    roteiro_aleatorio = random.sample(atracoes,k=num_atracoes_alea)
    print("Roteiro Aleatório\n")
    for n, atracao in enumerate(roteiro_aleatorio):
        print(n+1,atracao['NOME'])
        print("\t",atracao['DESCRICAO'],"\n")
    print("1 - Salvar roteiro?\n"
          "0 - Voltar\n")
    save=int(input("Digite sua opção: "))
    if save == 1:
        id=0
        for roteiro in meus_roteiros:
            if roteiro['ID']>id:
                id=roteiro['ID']
        nome = input("Digite o nome do seu roteiro: ")
        meu_roteiro_copy=roteiro_aleatorio.copy()
        meus_roteiros_dict = {"ID": id+1 ,
                            "NOME": nome,
                            "ATRACOES": meu_roteiro_copy
                            }
        meus_roteiros.append(meus_roteiros_dict)
        system('cls')
        
    elif save == 0:
        menu_principal(True)

def buscar_passeios():
    system('cls')
    while True:
        print("\nFILTROS\n"
                "1 - Por horário\n"
                "2 - Por tipo\n"
                "3 - Todos os passeios\n"
                "0 - Voltar\n")
        opcao_filtro= int(input("\nDigite sua opção: "))
        if opcao_filtro==0:
            menu_meu_roteiro()
        elif opcao_filtro==3:
            for atracao in atracoes:
                print(atracao["ID"], "-", atracao["NOME"])
            print("0 - Voltar")
            opcao = int(input('\nDigite sua opção: '))
            system('cls')
            print()
            for atracao in atracoes:
                if opcao == atracao['ID']:
                    print(atracao['ID'], atracao['NOME'])
                    print("\t",atracao['DESCRICAO'],"\n")
                    save = int(input("1 - Deseja adicionar esta atração ao seu roteiro?\n"
                            "0 - Voltar.\n"
                            "\nDigite sua opção: "))
                    if save == 1:
                        meu_roteiro.append(atracao)
                        buscar_passeios()
                    elif save == 0:
                        buscar_passeios()
        elif opcao_filtro==2:
            system('cls')
            print("\nTIPO\n"
            "1 - Praias\n"
            "2 - Alimentação\n"
            "3 - Balada\n"
            "4 - Compras\n"
            "0 - Voltar\n")
            opcao_tipo = int(input("Digite sua opção: "))
            if opcao_tipo==0:
                system('cls')
                buscar_passeios()
            if opcao_tipo==1:
                tipo("praia")
            if opcao_tipo==2:
                tipo("alimentação")
            if opcao_tipo==3:
                tipo("balada")
            if opcao_tipo==4:
                tipo("compras")
                
        elif opcao_filtro == 1:
            system('cls')
            print("\nHORÁRIO\n"
                "1 - Dia\n"
                "2 - Noite\n"
                "0 - Voltar")
            opcao = int(input("Digite sua opção: "))
            if opcao==0:
                buscar_passeios()
            if opcao==1:
                horario("dia")
            if opcao==2:
                horario("noite")
def horario(turno):
    system('cls')
    for atracao in atracoes:
        if turno in atracao['HORARIOS']:
                print(atracao["ID"], "-", atracao["NOME"])
    print("0 - Voltar")
    opcao = int(input('\nDigite sua opção: '))
    system('cls')
    for atracao in atracoes:
        if opcao == atracao['ID']:
            print(atracao['ID'], atracao['NOME'])
            print("\t",atracao['DESCRICAO'],"\n")
            save = int(input("\n1 - Deseja adicionar esta atração ao seu roteiro?\n"
                    "0 - Voltar.\n"
                    "\nDigite sua opção: "))
            if save == 1:
                meu_roteiro.append(atracao)
                buscar_passeios()
            elif save == 0:
                buscar_passeios() 
def tipo(categoria):
    system('cls')
    for atracao in atracoes:
        if categoria in atracao['TIPO']:
            print(atracao["ID"], "-", atracao["NOME"])
    print("0 - Voltar")
    opcao = int(input('\nDigite sua opção: '))
    system('cls')
    for atracao in atracoes:
        if opcao == atracao['ID']:
            print(atracao['ID'], atracao['NOME'])
            print("\t",atracao['DESCRICAO'],"\n")
            save = int(input("1 - Deseja adicionar esta atração ao seu roteiro?\n"
                    "0 - Voltar.\n"
                    "\nDigite sua opção: "))
            if save == 1:
                meu_roteiro.append(atracao)
                buscar_passeios()
            elif save == 0:
                buscar_passeios()
menu_principal(False)