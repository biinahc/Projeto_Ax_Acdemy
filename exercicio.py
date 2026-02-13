
import sys
import io
import math

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def area_retangulo(lado1, lado2):
    return lado1 * lado2

def hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

print("1. Área do Retângulo")
print("2. Hipotenusa do triângulo retângulo")

opcao = int(input("Escolha uma opção: "))

valor1 = float(input())
valor2 = float(input())

if opcao == 1:
    resultado = area_retangulo(valor1, valor2)
elif opcao == 2:
    resultado = hipotenusa(valor1, valor2)
else:
    print("Opção inválida")
    exit()

print("{:.2f}".format(resultado))