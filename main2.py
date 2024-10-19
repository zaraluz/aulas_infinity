def menu():
    print("\n===== MENU =====")
    print("1. Adicionar equipe e pontuações")
    print("2. Exibir classificação final")
    print("3. Sair")
    return input("Escolha uma opção: ")

def adicionar_equipe(equipes):
    nome = input("Nome da equipe: ")
    pontuacoes = input("Digite as pontuações separadas por vírgula: ")
    # Converte as pontuações de string para uma lista de inteiros
    pontuacoes = list(map(int, pontuacoes.split(',')))
    equipes.append((nome, pontuacoes))  # Adiciona a equipe e suas pontuações à lista

def calcular_medias(equipes):
    medias = []
    for equipe, pontuacoes in equipes:
        media = sum(pontuacoes) / len(pontuacoes)  # Calcula a média das pontuações
        medias.append((equipe, media))  # Armazena a equipe e sua média
    return medias

def exibir_classificacao(equipes):
    medias = calcular_medias(equipes)
    classificacao = sorted(medias, key=lambda x: x[1], reverse=True)  # Ordena em ordem decrescente
    print("\n===== Classificação Final =====")
    for equipe, media in classificacao:
        print(f"{equipe}: {media:.2f}")

def main():
    equipes = []  # Lista para armazenar as equipes e suas pontuações
    while True:
        opcao = menu()
        
        if opcao == '1':
            adicionar_equipe(equipes)
        elif opcao == '2':
            if not equipes:
                print("Nenhuma equipe foi adicionada ainda!")
            else:
                exibir_classificacao(equipes)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
