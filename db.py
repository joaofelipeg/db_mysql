import mysql.connector

config = {
    'user' : 'root',
    'password' : 'admin',
    'host' : 'localhost',
    'database' : 'db_alunos',
}

conn = mysql.connector.connect(**config)
if conn.is_connected():
    print("Banco de Dados conectado!")
cursor = conn.cursor()

op = input("1 - Pesquisar aluno \n 2 - Cadastrar aluno \n 3 - Deletar Casdastro \n 4 - Atualizar o cadastro ")
if op == ("1"):
    id = input("Digite o id do aluno: ")
    cursor.execute(f"SELECT * from tabela_alunos where id = {id}")
    result = cursor.fetchall()
    for now in result:
        print(now)
    conn.commit()

elif op == ("2"):
    id = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = int(input("Digite o cpf do aluno: "))
    cursor.execute(f"INSERT INTO `db_alunos`.`tabela_alunos` (nome_alunos, idade, cpf) VALUES ('{id}', {idade}, '{cpf}');")
    conn.commit()

elif op == ("3"):
    id = input("Digite o id do aluno :")
    cursor.execute(f"DELETE from tabela_alunos where id = {id};")
    conn.commit()
    

elif op == ("4"):
    id = input("Digite o id do aluno :")
    cpf = int(input("Digite o novo cpf: "))
    cursor.execute(f"UPDATE tabela_alunos SET cpf = '{cpf}' WHERE id = '{id}';")
    conn.commit()


cursor.close()
