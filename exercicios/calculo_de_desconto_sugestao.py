
def obterFracionarioDaPorcentagem(porcentagemDecimal):
    return porcentagemDecimal/100

def calculaValorDoDesconto(precoCheio, porcentagemDesconto):
    return precoCheio * porcentagemDesconto
#
def calculaValorComDesconto(precoCheio, valorDoDesconto):
    return precoCheio - valorDoDesconto

# def subtracao(numero1, numero2):
#     return numero1 - numero2

def main():
    print("Bem Vindo")
    valorProduto = float(input("Digite o custo do produto: "))
    porcentagemDesconto = float(input("Digite o valor do desconto em %: "))
    fracionario = obterFracionarioDaPorcentagem(porcentagemDesconto)

    valorASerDescontado = calculaValorDoDesconto(valorProduto, fracionario)

    resultado = calculaValorComDesconto(valorProduto, valorASerDescontado)
    # resultado = subtracao(valorProduto, valorASerDescontado)
    print(resultado)

if __name__== "__main__":
    main()