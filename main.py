import pyodbc

dados_conexao = (

    "Driver={SQL Server};"
    "Server=BOOKE20\MSSQLSERVER01;"
    "Database=AdventureWorks2017;"

)

conexao = pyodbc.connect(dados_conexao)
print("Conexao com banco de dados ok")

cursor = conexao.cursor()

#comando = """insert into Forms(nome, email, telefone, sexo, data_nasc, cidade, estado, endereco)
#values
#('Lucas', 'llucas.andrads@gmail.com', '11900000000', 'M', '09/01/1997', 'Sao Paulo', 'SP', 'Av. Paulista 1000')"""

#cursor.execute(comando)
#cursor.commit()

