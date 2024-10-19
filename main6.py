class Livro:
    def __init__(self, titulo, autor, id_livro, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.id_livro = id_livro
        self.num_copias = num_copias # A princípio, todos os livros estão disponíveis.

    def emprestar(self):
        if self.num_copias > 0:
            self.num_copias -= 1
            return True
        return False

    def devolver(self):
        self.num_copias += 1

class Membro:
    def __init__ (self, nome, numero_membro):
        self.nome = nome 
        self.numero_membro = numero_membro
        self.historico =[]

    def registrar_emprestimo(self,livro):
        self.historico.append(livro)

    def mostrar_historico(self, livro):
        for livro in self.historico:
            print (f"Título:{livro.titulo}; Autor: {livro.autor}; ID: {livro.id_livro}")

class Biblioteca:
    def __init__(self):
        self.catalago = []
        self.membros = []
    
    def adicionar_livro(self, livro):
        self.catalogo.append(livro)
    
    def adicionar_mebro(self, membro):
        self.membros.append(membro)

    def emprestar_livro(Self,id_livro, numero_membro):
        self.id_livro

class Biblioteca:
    def __init__(self):
        self.catalogo = []  # Lista de livros disponíveis.
        self.membros = []   # Lista de membros cadastrados.

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def emprestar_livro(self, id_livro, numero_membro):
        livro = next((l for l in self.catalogo if l.id_livro == id_livro), None)
        membro = next((m for m in self.membros if m.numero_membro == numero_membro), None)

        if livro and membro:
            if livro.emprestar():
                membro.registrar_emprestimo(livro)
                print(f"O livro '{livro.titulo}' foi emprestado para {membro.nome}.")
            else:
                print(f"O livro '{livro.titulo}' não está disponível.")
        else:
            print("Livro ou membro não encontrado.")

    def devolver_livro(self, id_livro, numero_membro):
        livro = next((l for l in self.catalogo if l.id_livro == id_livro), None)
        membro = next((m for m in self.membros if m.numero_membro == numero_membro), None)
        if livro and membro:
            livro.devolver()
            print(f"O livro '{livro.titulo}' foi devolvido.")
        else:
            print("Livro não encontrado.")

    def pesquisar_livro(self, termo):
        resultados = [l for l in self.catalogo if termo.lower() in l.titulo.lower() or termo.lower() in l.autor.lower()]

        if resultados:
            print("Livros encontrados:")
            for livro in resultados:
                status = "Disponível" if livro.disponivel else "Emprestado"
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, ID: {livro.id_livro}, Status: {status}")
        else:
            print("Nenhum livro encontrado.")


def menu():
    biblioteca = Biblioteca()  # Cria uma instância da biblioteca

    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Adicionar Membro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Pesquisar Livro")
        print("6. Mostrar Histórico de Empréstimos de um Membro")
        print("7. Sair")

        escolha = input("Escolha uma opção (1-7): ")

        if escolha == '1':
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            id_livro = input("ID do Livro: ")
            num_copias = int(input("Número de cópias: "))
            livro = Livro(titulo, autor, id_livro, num_copias)
            biblioteca.adicionar_livro(livro)
            print(f"Livro '{titulo}' adicionado com sucesso!")

        elif escolha == '2':
            nome = input("Nome do Membro: ")
            numero_membro = input("Número do Membro: ")
            membro = Membro(nome, numero_membro)
            biblioteca.adicionar_membro(membro)
            print(f"Membro '{nome}' adicionado com sucesso!")

        elif escolha == '3':
            id_livro = input("ID do Livro para Emprestar: ")
            numero_membro = input("Número do Membro: ")
            biblioteca.emprestar_livro(id_livro, numero_membro)

        elif escolha == '4':
            id_livro = input("ID do Livro para Devolver: ")
            biblioteca.devolver_livro(id_livro)

        elif escolha == '5':
            termo = input("Digite o título ou autor do livro a pesquisar: ")
            biblioteca.pesquisar_livro(termo)

        elif escolha == '6':
            numero_membro = input("Digite o número do membro: ")
            membro = next((m for m in biblioteca.membros if m.numero_membro == numero_membro), None)
            if membro:
                membro.mostrar_historico()
            else:
                print("Membro não encontrado.")

        elif escolha == '7':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Para executar o menu
if __name__ == "__main__":
    menu()
