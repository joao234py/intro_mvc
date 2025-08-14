class Livro:
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

    def __str__(self):
        return f"Livro(ID: {self.id}, Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, ISBN {self.isbn})"