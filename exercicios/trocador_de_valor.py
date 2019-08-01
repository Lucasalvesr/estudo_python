a = input("Digite algo para o parâmetro a: ")
b = input("Digite algo para o parâmetro b: ")
c = int(input("Digite o número 1 para ver o parâmetro a ou ou o numero 2 para ver o parâmetro b: "))
def troca_a_para_b(a,b):
    a = b
    return a

def troca_b_para_a(a,b):
    b = a
    return b

if c == 1:
    print("O parâmetro a é: ",troca_a_para_b(a,b))
elif c == 2:
    print("O parâmetro b é: ",troca_b_para_a(a,b))

print(a)
print(b)
