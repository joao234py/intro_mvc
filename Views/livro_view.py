class LivroView:
    def mostrar_livro(self, livro):
        print(livro)
    
    def mostrar_livros(self, livros):
        for livro in livros:
            self.mostrar_livro(livro)