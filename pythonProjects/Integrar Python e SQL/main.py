
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=N1250;"
    "Database=SUCOS_VENDAS;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

cursor = conexao.cursor()

# comando = """INSERT INTO [TABELA DE PRODUTOS]
# ([CODIGO DO PRODUTO], [NOME DO PRODUTO], [EMBALAGEM], [TAMANHO], [SABOR], [PREÇO DE LISTA])
# VALUES ('000000','Light - 350 ml - Melância', 'Lata', '350 ml', 'Melância', 4.56)"""
#
# cursor.execute(comando)
# cursor.commit()

comando2 = """DELETE FROM [TABELA DE PRODUTOS] WHERE [CODIGO DO PRODUTO] = '000000' """

cursor.execute(comando2)
cursor.commit()

