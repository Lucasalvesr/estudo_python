import sys

def soma(x, y):
    return x + y
def subtracao(x, y):
    return x - y
def divisao(x, y):
    return x / y
def multiplicacao(x, y):
    return x * y

def calculo(numero1, numero2, operacao):
    if operacao == "+":
        return soma(numero1, numero2)
    elif operacao == "-":
        return subtracao(numero1, numero2)
    elif operacao == "*":
        return multiplicacao(numero1, numero2)
    elif operacao == "/":
        return divisao(numero1, numero2)

def main():
    if len(sys.argv) == 4 :
        numero1 = sys.argv[1]
        numero2 = sys.argv[2]
        operacao = sys.argv[3]
    else:
        numero1 = input("Digite um número: ")
        operacao = input("Digite a operação desejada: ( + , - , * , / ): ")
        numero2 = input("Digite o segundo numero: ")

    resultado = calculo(int(numero1), int(numero2), operacao)
    print(resultado)

if __name__== "__main__":
    main()