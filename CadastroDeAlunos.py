alunos = []  # Lista que armazena os nomes dos alunos cadastrados

# Função responsável por cadastrar um aluno
def cadastrar_aluno(x):
    nome = input("Digite o nome do aluno: ").title()  # Solicita o nome e padroniza com inicial maiúscula
    alunos.append(nome)  # Adiciona o nome na lista de alunos
    print(x)  # Exibe uma mensagem passada como parâmetro

# Loop principal do sistema (menu)
while True:
    print("\n 1. Cadastrar Aluno")  # Opção 1 do menu
    print("\n 2. Consultar Login")   # Opção 2 do menu
    print("\n 3. Sair")              # Opção 3 do menu

    escolha_do_usuario = int(input("\n Digite o valor desejado: "))  # Captura a escolha do usuário

    # Opção 1: cadastrar aluno
    if escolha_do_usuario == 1:
        cadastrar_aluno("Nome cadastrado com sucesso, deseja realizar um novo cadastro? Se sim digite y, se não digite n")
        # Após o cadastro inicial, pergunta se deseja cadastrar outro aluno

        novo_cadastro_opção = input("y ou n: ").lower()  # Resposta do usuário

        if novo_cadastro_opção == "y":
            cadastrar_aluno("Aluno cadastrado com sucesso!")  # Cadastra outro aluno

        elif novo_cadastro_opção == "n":
            print("OK, obrigado pela a preferência e volte sempre!")  # Encerra o programa
            break

        else:
            print("digite somente y/n")  # Validação de entrada inválida

    # Opção 2: consultar aluno cadastrado
    elif escolha_do_usuario == 2:
        consultar_login = input("Digite o nome do Aluno: ").title()  # Solicita nome para consulta

        if consultar_login in alunos:
            print(f"O {consultar_login} já é cadastrado com sucesso")  # Confirma existência do aluno
        
        else:
            print("Aluno não encontrado, deseja cadastrar? Se sim digite y, se não digite n")
            novo_cadastro_de_aluno_não_identificado = input("").lower()  # Opção do usuário

            if novo_cadastro_de_aluno_não_identificado == "y":
                cadastrar_aluno("Parabens, o aluno foi cadastrado com sucesso!")  # Cadastra novo aluno

            elif novo_cadastro_de_aluno_não_identificado == "n":
                print("Obrigado, volte sempre")  # Encerra o programa
                break

            else:
                print("digite somente y/n")  # Validação de entrada inválida

    # Opção 3: sair do sistema
    elif escolha_do_usuario == 3:
        print("Ok, até mais")  # Mensagem de encerramento
        break  # Finaliza o loop

    # Caso o usuário digite uma opção inválida
    else:
        print("Formato invalido")  # Tratamento de entrada incorreta
