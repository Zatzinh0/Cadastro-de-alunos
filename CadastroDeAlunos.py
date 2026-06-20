alunos = []

def cadastrar_aluno(x):
        nome = input("Digite o nome do aluno: ").title()
        alunos.append(nome)
        print(x)

while True:
    print("\n 1. Cadastrar Aluno")
    print("\n 2. Consultar Login")
    print("\n 3. Sair")

    escolha_do_usuario = int(input("\n Digite o valor desejado: "))

    if escolha_do_usuario == 1:
        cadastrar_aluno("Nome cadastrado com sucesso, deseja realizar um novo cadastro? Se sim digite y, se não digite n")
        novo_cadastro_opção = input("y ou n: ").lower()
        
        if novo_cadastro_opção == "y":
            cadastrar_aluno("Aluno cadastrado com sucesso!")
    
        elif novo_cadastro_opção == "n":
            print("OK, obrigado pela a preferência e volte sempre!")
            break

        else:
            print("digite somente y/n")
            

    elif escolha_do_usuario == 2:
        consultar_login = input("Digite o nome do Aluno:").title()

        if consultar_login in alunos:
            print(f"O {consultar_login} já é cadastrado com sucesso")
        
        else:
            print("Aluno não encontrado, deseja cadastrar? Se sim digite y, se não digite n")
            novo_cadastro_de_aluno_não_identificado = input("").lower()

            if novo_cadastro_de_aluno_não_identificado == "y":
                cadastrar_aluno("Parabens, o aluno foi cadastrado com sucesso!")

            elif novo_cadastro_de_aluno_não_identificado == "n":
                print("Obrigado, volte sempre")
                break

            else:
                print("digite somente y/n")

    elif escolha_do_usuario == 3:
        print("Ok, até mais")
        break

    else:
        print("Formato invalido")