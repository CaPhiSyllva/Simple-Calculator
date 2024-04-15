def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero.")
    return x / y

def exibir_menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def calcular_operacao(opcao, num1, num2):
    operacoes = {
        '1': adicionar,
        '2': subtrair,
        '3': multiplicar,
        '4': dividir,
    }
    
    if opcao not in operacoes:
        print("Opção inválida.")
        return
    
    try:
        resultado = operacoes[opcao](num1, num2)
        simbolos_operacoes = {'1': '+', '2': '-', '3': '*', '4': '/'}
        simbolo = simbolos_operacoes[opcao]
        print(f"{num1} {simbolo} {num2} = {resultado}")
    except ValueError as e:
        print(e)

def main():
    exibir_menu()
    escolha = input("Digite sua escolha (1/2/3/4): ")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Os números inseridos não são válidos.")
        return
    
    calcular_operacao(escolha, num1, num2)

if __name__ == "__main__":
    main()



