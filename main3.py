turma = {}

def Adicionar_Aluno():
    nome = input("Nome aluno: ")
    if nome in turma:
        print("Aluno já cadastrado")
    else:
        idade = int(input("Idade do aluno: "))


        nota_matematica = float(input("Nota em Matemática: "))
        nota_ciencias = float(input("Nota em Ciências: "))
        nota_historia = float(input("Nota em História: "))
        
        turma[nome] = {
            'idade': idade,
            'notas': (nota_matematica, nota_ciencias, nota_historia)
        }
        print(f"Aluno {nome} adicionado com sucesso!")

def Visualizar_Aluno():
    if not turma:
        print("Nenhum aluno cadastrado")

        return
    
    melhor_aluno = None
    melhor_media = 0

    print("\nLista de Alunos Cadastrados:")

    for nome, dados in turma.items():
        idade = dados['idade']
        notas = dados['notas']

        media = sum(notas) / 3
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Notas: Matemática: {notas[0]}, Ciências: {notas[1]}, História: {notas[2]}")
        print(f"Média: {media:.2f}\n")

def Ver_Resultados():
    if not turma:
        print("Nenhum aluno cadastrado.")
        return
    
    melhor_aluno = None
    melhor_media = 0
    
    for nome, dados in turma.items():
        notas = dados['notas']
        media = sum(notas) / 3
        
        if media > melhor_media:
            melhor_media = media
            melhor_aluno = nome
    
    if melhor_aluno:
        print(f"O aluno com a melhor média é {melhor_aluno}, com média {melhor_media:.2f}.")

def Menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar Aluno")
        print("2 - Ver Turma e médias por aluno")
        print("3 - Ver Resultados (Melhor Média)")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            Adicionar_Aluno()
        elif opcao == '2':
            Visualizar_Aluno()
        elif opcao == '3':
            Ver_Resultados()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

Menu()