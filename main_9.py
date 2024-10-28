class Livro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.emprestado = False

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"Título: {self.titulo} | Autor: {self.autor} | ID: {self.id} | Status: {status}"


class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

    def adicionar_historico(self, livro):
        self.historico_emprestimos.append(livro)

    def __str__(self):
        return f"Número de Membro: {self.numero_membro} | Nome: {self.nome}"


class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = {}

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def registrar_membro(self, membro):
        self.membros[membro.numero_membro] = membro

    def emprestar_livro(self, titulo, numero_membro):
        livros_encontrados = [livro for livro in self.catalogo if titulo.lower() in livro.titulo.lower()]
        membro = self.membros.get(numero_membro)

        if not livros_encontrados:
            print("Livro não encontrado.")
            return
        if not membro:
            print("Membro não registrado.")
            return

        print("Livros encontrados:")
        for livro in livros_encontrados:
            print(livro)

        escolha = input("Digite o título completo do livro que deseja emprestar: ")
        livro_emprestado = next((livro for livro in livros_encontrados if livro.titulo.lower() == escolha.lower()), None)

        if livro_emprestado:
            if livro_emprestado.emprestado:
                print("Livro já emprestado.")
            else:
                livro_emprestado.emprestado = True
                membro.adicionar_historico(livro_emprestado)
                print(f"Livro '{livro_emprestado.titulo}' emprestado a {membro.nome}.")
        else:
            print("Título de livro inválido. Tente novamente.")
        
    def devolver_livro(self, titulo):
        livro = next((livro for livro in self.catalogo if livro.titulo.lower() == titulo.lower()), None)

        if not livro:
            print("Livro não encontrado.")
            return
        if not livro.emprestado:
            print("Livro já está disponível.")
            return

        livro.emprestado = False
        print(f"Livro '{livro.titulo}' devolvido à biblioteca.")

    def listar_catalogo(self):
        if not self.catalogo:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.catalogo:
                print(livro)

    def listar_membros(self):
        if not self.membros:
            print("Nenhum membro cadastrado.")
        else:
            for membro in self.membros.values():
                print(membro)

    def ver_historico_membro(self, numero_membro):
        membro = self.membros.get(numero_membro)
        if not membro:
            print("Membro não encontrado.")
        else:
            print(f"Histórico de empréstimos de {membro.nome}:")
            if not membro.historico_emprestimos:
                print("Nenhum empréstimo registrado.")
            else:
                for livro in membro.historico_emprestimos:
                    print(livro)


def menu():
    bibli = Biblioteca()
    
    while True:
        print("\n=== Sistema de Gerenciamento da Biblioteca ===")
        print("1. Adicionar Livro")
        print("2. Registrar Membro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Listar Catálogo de Livros")
        print("6. Listar Membros")
        print("7. Ver Histórico de Empréstimos por Membro")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            id = input("ID do livro: ")
            livro = Livro(titulo, autor, id)
            bibli.adicionar_livro(livro)
            print(f"Livro '{titulo}' adicionado ao catálogo.")

        elif opcao == '2':
            nome = input("Nome do membro: ")
            numero_membro = input("Número do membro: ")
            membro = Membro(nome, numero_membro)
            bibli.registrar_membro(membro)

        elif opcao == '3':
            titulo = input("Título do livro a ser emprestado: ")
            numero_membro = input("Número do membro: ")
            bibli.emprestar_livro(titulo, numero_membro)

        elif opcao == '4':
            titulo = input("Título do livro a ser devolvido: ")
            bibli.devolver_livro(titulo)

        elif opcao == '5':
            bibli.listar_catalogo()

        elif opcao == '6':
            bibli.listar_membros()

        elif opcao == '7':
            numero_membro = input("Número do membro: ")
            bibli.ver_historico_membro(numero_membro)

        elif opcao == '0':
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
