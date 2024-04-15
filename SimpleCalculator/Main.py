from SimpleCalculator.calculator import calcular_operacao, exibir_menu


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
