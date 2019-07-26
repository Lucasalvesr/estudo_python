# a=int(input("Digite o primeiro número: "))
# b=int(input("Digite o seguindo número: "))
# print("a soma é", a+b)
# a=int(input("Digite o primeiro número: "))
# b=int(input("Digite o seguindo número: "))
# print("A subtraçaõ é", a-b)
# a=int(input("Digite o primeiro número: "))
# b=int(input("Digite o seguindo número: "))
# print("A multiplicação é", a*b)
# a=int(input("Digite o primeiro número: "))
# b=int(input("Digite o seguindo número: "))
# print("A divisão é" + str(a/b))

# a=type(input("O tipo do dado dijitado e: "))
# print(a)
#
# d = input("Digite aldo: ")
# f = type(int(d))
# print(f)

# a=2.12
# b=3.1435643
# print("o valor é %.2f" % b)
#
# def teste():
#     return "a"
# def teste2():
#     return 3
# print(teste())
# print(teste2())
#
#
#
# if 2 == 3:
#     print("voce está correto")
# else:
#     print("você esta errado")


# if c == 1:
#     print(a + b)
# elif c == 2:
#     print(a - b)
# elif c == 3:
#     print(a * b)
# elif c == 4:
#     print(a / b)

def soma(a, b):
    c = a + b
    return c
def subtração(a, b):
    c = a - b
    return c
def multiplicaão(a, b):
    c = a * b
    return c
def divisão (a, b):
    c = a / b
    return c
def calculo(a, b, c):
    if c == 1:
        print(soma(a, b))
    elif c == 2:
        print(subtração(a,b))
    elif c == 3:
        print(multiplicaão(a, b))
    elif c == 4:
        print(divisão(a, b))

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("digite um dos operadores, exemplo 1 para +, 2 para -, 3 para * ou 4 para /: "))
calculo(a, b, c)




