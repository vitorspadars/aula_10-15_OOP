import sqlite3

class BancoDeDadosSQLite:
    def __init__(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = sqlite3.connect(self.nome_arquivo)
            print("Conexão estabelecida com sucesso!")
        except sqlite3.Error as e:
            print("Erro ao conectar ao bando de dados: ", e)

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada.")

    def executar_query(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print("Query executada com sucesso!")
        except sqlite3.Error as e:
            print("Erro ao executar a query: ", e)


# exemplo

if __name__ == "__main__":
    nome_arquivo = "exemplo.db"
    banco = BancoDeDadosSQLite(nome_arquivo)
    banco.conectar()


    # criando uma tabela

    create_table_query = """
    CREATE TABLE IF NO EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """

    banco.executar_query(create_table_query)

        # Inserindo dados na tabela
    insert_query = """
    INSERT INTO usuarios (nome, email) VALUES
    ('João', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """
    banco.executar_query(insert_query)

    banco.desconectar()