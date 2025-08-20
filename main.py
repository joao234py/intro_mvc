'''
from Controller.livro_controller import LivroController

def main():
    db_config = {
        "dbname" : "intro_mvc",
        "user" : "postgres",
        "password" : "wcc@2023",
        "host" : "127.0.0.1",
        "port" : "5433"
    }

    livro_controller = LivroController(db_config)

    #
    livro_controller.adicionar_livro(1,"1984", "George Orwell", 1949, "1234567890123")
'''
from Views.livro_view import LivroView

def main():
    LivroView.iniciar_login_banco()



if __name__ == "__main__":
    main()