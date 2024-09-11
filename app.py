import mysql.connector
import funcoes as func 

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '$enhaF0rte',
    'database': 'ouvidoria'
}

def conectar_db():
    return mysql.connector.connect(**db_config)

while True:
    print("\n=== Ouvidoria Unifacisa ===")
    print("1. Criar ocorrência")
    print("2. Listar ocorrências")
    print("3. Atualizar ocorrência")
    print("4. Deletar ocorrência(s)")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    conexao = conectar_db()
    cursor = conexao.cursor()

    if opcao == '1':
        func.criar()

        # tipo_ocorrencia = input("Tipo de ocorrência (1-Elogio, 2-Sugestão, 3-Reclamação): ")
        # descricao = input("Descrição da ocorrência: ")
        # cpf_email = input("CPF ou email do aluno: ")

        # sql = "INSERT INTO ocorrencias (tipo, descricao, cpf_email) VALUES (%s, %s, %s)"
        # valores = (tipo_ocorrencia, descricao, cpf_email)
        # cursor.execute(sql, valores)
        # conexao.commit()
        # print("Ocorrência registrada com sucesso!")

    elif opcao == '2':
        func.listar()
        # cursor.execute("SELECT * FROM ocorrencias")
        # ocorrencias = cursor.fetchall()
        # if not ocorrencias:
        #     print("Nenhuma ocorrência registrada.")
        # else:
        #     print("\nOcorrências registradas:")
        #     for ocorrencia in ocorrencias:
        #         print(f"ID: {ocorrencia[0]}")
        #         print(
        #             f"Tipo: {'Elogio' if ocorrencia[1] == '1' else 'Sugestão' if ocorrencia[1] == '2' else 'Reclamação'}")
        #         print(f"Descrição: {ocorrencia[2]}")
        #         print(f"CPF/Email: {ocorrencia[3]}\n")

    elif opcao == '3':
        id_ocorrencia = int(input("Digite o ID da ocorrência a ser atualizada: "))
        print("O que deseja atualizar?")
        print("1. Tipo")
        print("2. Descrição")
        opcao_atualizacao = input("Digite o número da opção: ")
        if opcao_atualizacao == '1':
            novo_tipo = input("Novo tipo (1-Elogio, 2-Sugestão, 3-Reclamação): ")
            sql = "UPDATE ocorrencias SET tipo = %s WHERE id = %s"
            valores = (novo_tipo, id_ocorrencia)
        elif opcao_atualizacao == '2':
            nova_descricao = input("Nova descrição: ")
            sql = "UPDATE ocorrencias SET descricao = %s WHERE id = %s"
            valores = (nova_descricao, id_ocorrencia)
        else:
            print("Opção inválida.")
            continue
        cursor.execute(sql, valores)
        conexao.commit()
        print("Ocorrência atualizada com sucesso!")

    elif opcao == '4':
        print("1. Deletar uma ocorrência específica")
        print("2. Deletar todas as ocorrências")
        opcao_delecao = input("Digite o número da opção: ")
        if opcao_delecao == '1':
            id_ocorrencia = int(input("Digite o ID da ocorrência a ser deletada: "))
            sql = "DELETE FROM ocorrencias WHERE id = %s"
            valores = (id_ocorrencia,)
        elif opcao_delecao == '2':
            sql = "DELETE FROM ocorrencias"
            valores = None
        else:
            print("Opção inválida.")
            continue
        cursor.execute(sql, valores)
        conexao.commit()
        print("Ocorrência(s) deletada(s) com sucesso!")

    elif opcao == '5':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

    cursor.close()
    conexao.close()
