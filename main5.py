def Processador_texto(texto, **kwargs):

    operacoes = {
        "contar_palavras": lambda texto: len(texto.split()),
        "contar_letras": lambda texto: len([char for char in texto if char.isalpha()]),
        "inverter_texto": lambda texto: texto[::-1],
        "substituir_palavra": lambda texto, velha, nova: texto.replace(velha, nova)
    }

    resultado = texto

    for operacao, valor in kwargs.items():
        if operacao == "contar_palavras":
            print(f"Contagem de palavras: {operacoes['contar_palavras'](resultado)}")
        elif operacao == "contar_letras":
            print(f"Contagem de letras: {operacoes['contar_letras'](resultado)}")
        elif operacao == "inverter_texto":  
            resultado = operacoes["inverter_texto"](resultado)
            print(f"Texto invertido: {resultado}")  
        elif operacao == "substituir_palavra":
            velha_palavra = valor.get('velha') 
            nova_palavra = valor.get('nova')   
            resultado = operacoes["substituir_palavra"](resultado, velha_palavra, nova_palavra)
            print(f"Texto após substituição: {resultado}")  

    return resultado

def exibir_menu():
    print("\nEscolha uma operação:")
    print("1. Contar palavras")
    print("2. Contar letras")
    print("3. Substituir palavra")
    print("4. Inverter o texto")
    print("5. Sair")

def main():
    texto = input("Insira um texto ou frase: ")
    
    while True:
        exibir_menu()
        escolha = input("Digite a sua escolha (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Saindo do programa...")
            break
        
        kwargs = {}
        if escolha == '1':  
            kwargs["contar_palavras"] = True
        elif escolha == '2': 
            kwargs["contar_letras"] = True
        elif escolha == '4':
            kwargs["inverter_texto"] = True
        elif escolha == '3': 
            velha_palavra = input("Digite a palavra a ser substituída: ")
            nova_palavra = input("Digite a nova palavra: ")
            kwargs["substituir_palavra"] = {"velha": velha_palavra, "nova": nova_palavra}
        else:
            print("Escolha inválida, tente novamente.")
            continue
        texto = Processador_texto(texto, **kwargs)

        

if __name__ == "__main__":
    main()
