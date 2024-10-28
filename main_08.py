class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Função: {self.funcao}, Salário: R${self.salario:.2f}"

class Quarto:
    def __init__(self, numero, preco_diaria):
        self.numero = numero
        self.preco_diaria = preco_diaria
        self.status = "disponível"  # Status inicial do quarto

    def __str__(self):
        return f"Quarto {self.numero}, Preço: R${self.preco_diaria:.2f}, Status: {self.status}"

class Reserva:
    def __init__(self, nome_hospede, dias_estadia, quarto):
        self.nome_hospede = nome_hospede
        self.dias_estadia = dias_estadia
        self.quarto = quarto  # Armazena um objeto Quarto
        quarto.status = "ocupado"  # Marca o quarto como ocupado ao fazer a reserva

    def calcular_conta(self):
        return self.dias_estadia * self.quarto.preco_diaria

    def __str__(self):
        return f"Hóspede: {self.nome_hospede}, Dias de Estadia: {self.dias_estadia}, Quarto: {self.quarto.numero}"

class Hotel:
    def __init__(self):
        self.funcionarios = [] 
        self.quartos = []       
        self.reservas = []      

    
    def adicionar_funcionario(self, nome, funcao, salario):
        funcionario = Funcionario(nome, funcao, salario)
        self.funcionarios.append(funcionario)

    
    def adicionar_quarto(self, numero, preco_diaria):
        quarto = Quarto(numero, preco_diaria)
        self.quartos.append(quarto)

    def mostrar_quartos_disponiveis(self):
        return [quarto for quarto in self.quartos if quarto.status == "disponível"]

    def fazer_reserva(self, nome_hospede, dias_estadia):
        quartos_disponiveis = self.mostrar_quartos_disponiveis()
        if quartos_disponiveis:
            quarto = quartos_disponiveis[0]  # Atribui o primeiro quarto disponível
            reserva = Reserva(nome_hospede, dias_estadia, quarto)
            self.reservas.append(reserva)
            return reserva
        else:
            print("Desculpe, todos os quartos estão ocupados.")
            return None

    def finalizar_reserva(self, reserva):
        total = reserva.calcular_conta()
        reserva.quarto.status = "disponível"
        return total

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

if __name__ == "__main__":

    hotel = Hotel()

    while True:
        print("\nBem-vindo ao sistema de gerenciamento do Hotel!")
        print("Escolha uma opção:")
        print("1 - Adicionar Funcionário")
        print("2 - Adicionar Quarto")
        print("3 - Mostrar Quartos Disponíveis")
        print("4 - Fazer Reserva")
        print("5 - Finalizar Reserva")
        print("6 - Listar Funcionários")
        print("0 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            # Adicionar Funcionário
            nome = input("Nome do funcionário: ")
            funcao = input("Função do funcionário: ")
            salario = float(input("Salário do funcionário: "))
            hotel.adicionar_funcionario(nome, funcao, salario)
            print(f"Funcionário {nome} adicionado com sucesso!")

        elif opcao == "2":
            # Adicionar Quarto
            numero = int(input("Número do quarto: "))
            preco_diaria = float(input("Preço por diária: "))
            hotel.adicionar_quarto(numero, preco_diaria)
            print(f"Quarto {numero} adicionado com sucesso!")

        elif opcao == "3":
            # Mostrar Quartos Disponíveis
            quartos_disponiveis = hotel.mostrar_quartos_disponiveis()
            if quartos_disponiveis:
                print("\nQuartos disponíveis:")
                for quarto in quartos_disponiveis:
                    print(quarto)
            else:
                print("Nenhum quarto disponível no momento.")

        elif opcao == "4":
            # Fazer Reserva
            nome_hospede = input("Nome do hóspede: ")
            dias_estadia = int(input("Número de dias de estadia: "))
            reserva = hotel.fazer_reserva(nome_hospede, dias_estadia)
            if reserva:
                print(f"Reserva realizada com sucesso para {nome_hospede} no quarto {reserva.quarto.numero}.")
            else:
                print("Não foi possível fazer a reserva. Todos os quartos estão ocupados.")

        elif opcao == "5":
            # Finalizar Reserva
            nome_hospede = input("Nome do hóspede para finalizar a reserva: ")
            reserva_encontrada = None
            for reserva in hotel.reservas:
                if reserva.nome_hospede == nome_hospede:
                    reserva_encontrada = reserva
                    break
            if reserva_encontrada:
                total = hotel.finalizar_reserva(reserva_encontrada)
                print(f"Reserva finalizada. Total a pagar: R${total:.2f}")
            else:
                print("Reserva não encontrada para o hóspede informado.")

        elif opcao == "6":
            # Listar Funcionários
            print("\nLista de Funcionários:")
            hotel.listar_funcionarios()

        elif opcao == "0":
            # Sair
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")
