from Database.db import Database
from Views.livro_view import LivroView
class LivroController:
    def __init__(self, db_config):
        self.db = Database(
            db_config["dbame"],
            db_config["user"],
            db_config["password"],
            db_config["host"],
            db_config["port"]
       )
        self.criar_tabela_senao_existir()
        self.view = LivroView()

    def criar_tabela_senao_existir(self):
        conn = self.db.connect()
        if conn: 
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS livros(
                id SERIAL PRIMARY KEY,
                titulo VARCHAR(20) NOT NULL,
                autor VARCHAR(20) NOT NULL,
                ano INTEGER,
                isbn VARCHAR(13)
            );
        """)
        conn.commit()
        cur.close()
        conn.close()

    def adicionar_livro(self,id, titulo, autor, ano, isbn):
            conn = self.db.connect()
            if conn:
                cur = conn.cursor() # cur é um objeto a aprtir de uma conexão com o banco de dados
                # execute(): Método do cursor que executa uma consulta SQL passada por argumento 
                cur.execute(
                    # %s é um placeholder que será substituido pelos valores da tupla a seguir
                    # O psycopg2 substitui esse %s por valores reais de forma segura, evitando injeção de SQL
                    "INSERT INTO livros(id, titulo, autor, ano, isbn) VALUES (%s,%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING;"
                    (id, titulo, autor, ano, isbn)
                )
                conn.commit()
                cur.close()
                conn.close()
                print("Livro adicionado com sucesso!")
            else:
                print("erro ao conectar ao banco de dados.")
    def listar_livros(self, livros):
            self.view.mostrar_livros(livros)
