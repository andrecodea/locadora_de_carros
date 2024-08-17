import os
import time

# Lista de carros disponíveis para aluguel, com modelo e preço por dia.
carros = [
    ("Chevrolet Tracker", 120), 
    ("Chevrolet Onix", 90), 
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85), 
    ("Hyundai Tucson", 120), 
    ("Fiat Uno", 60), 
    ("Fiat Mobi", 70), 
    ("Fiat Pulse", 130)
]

# Lista de carros alugados
alugados = []

# Função para exibir a lista de carros disponíveis
def mostrar_lista_de_carros(lista_de_carros):
    for i, (modelo, preco) in enumerate(lista_de_carros):
        print(f"[{i}] {modelo} - R$ {preco} /dia")

# Função principal para executar o programa
def main():
    while True:
        os.system("cls")
        print("=============")
        print("Seja bem-vindo(a) à locadora de carros!")
        print("=============")
        print()
        print("[0] - Mostrar portfólio\n[1] - Alugar um carro\n[2] - Devolver um carro\n")
        op = input("Escolha uma opção: ")

        os.system("cls")

        if op == "0":
            mostrar_lista_de_carros(carros)

        elif op == "1":
            if not carros:
                print("Nenhum carro disponível para aluguel.")
            else:
                mostrar_lista_de_carros(carros)
                print()
                cod_car = int(input("Escolha o código do carro: "))
                os.system("cls")
                dias = int(input("Por quantos dias você deseja alugar este carro? "))
                os.system("cls")
                valor_total = dias * carros[cod_car][1]
                print(f"Você escolheu {carros[cod_car][0]} por {dias} dias.")
                print()
                print(f"O valor total do aluguel será R$ {valor_total}. Deseja alugar?")
                print()
                conf = input("Digite [0] para SIM ou [1] para NÃO: ")

                if conf == "0":
                    os.system("cls")
                    alugados.append(carros.pop(cod_car))
                    print(f"Parabéns, você alugou o {alugados[-1][0]} por {dias} dias.")
                else:
                    os.system("cls")
                    print("Operação cancelada.")

        elif op == "2":
            if not alugados:
                print("Não há carros a serem devolvidos.")
            else:
                print("Segue a lista de carros alugados:")
                mostrar_lista_de_carros(alugados)
                print()
                cod_dev = int(input("Qual carro você deseja devolver? "))
                print()
                print(f"Obrigado por devolver o carro {alugados[cod_dev][0]}.")
                carros.append(alugados.pop(cod_dev))

        else:
            print("Opção inválida.")

        print("\n==========")
        print()
        if input("Digite [1] para SAIR ou qualquer outra tecla para CONTINUAR: ") == "1":
            print("Finalizando programa...")
            time.sleep(1)
            print("Obrigado por usar a nossa locadora, volte sempre!")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()
