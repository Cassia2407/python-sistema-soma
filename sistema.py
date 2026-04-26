print("=== Sistema de Cálculo ===")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2

print("A soma é:", soma)

if n1 > n2:
    print("O maior número é:", n1)
elif n2 > n1:
    print("O maior número é:", n2)
else:
    print("Os dois números são iguais")