# para treinar a fatiação de strings

s = "Python"
s1 = " é uma linguagem de programação"

print(s[0]) 
print (s[1])
print (s[-1])
print (s[0:3])
print (s[2:])
print (s[:4])
print (len(s))
print (s + s1)
print (s * 3)

#com listas 
L = list("Alo mundo")
print(L)
L[0] = "O"
print(L)


# para treinar a função startswith que diz se a string começa com um determinado prefixo ou não. Retorna True ou False.
nome = 'João da Silva'
nome.startswith("João")
print(nome.startswith("João"))
print(nome.startswith("Rodrigues"))

# para treinar a função endswith que diz se a string termina com um determinado sufixo ou não. Retorna True ou False.
print(nome.endswith("Silva"))
print(nome.endswith("Rodrigues"))

#padronizando a string para maiúscula ou minúscula

s = "Python é uma Linguagem de Programação"
s.lower() # para deixar a string toda em minúscula
s.upper() # para deixar a string toda em maiúscula
print(s.lower())
print(s.upper())


 # para substituir uma parte da string por outra
A = "João comprou um carro mo da hora."
s.replace("mo da hora", "muito legal")
print(A.replace("mo da hora", "muito legal"))


# para encontrar a posição de uma substring dentro da string. Retorna o índice da primeira ocorrência ou -1 se não for encontrada.
A.find("carro") 
print(A.find("carro"))


# para contar quantas vezes uma substring aparece na string. Retorna o número de ocorrências.

s = "um tigre, dois tigres, três tigres"
p = 0
while (p>-1):
    p = s.find("tigres", p)
    if p > -1:
        print(p)
        p += len("tigres")
        
print(s.count("tigres")) 


#Parâmetro opcional (valor padrão). Crie uma função que faz uma saudacao para uma pessoa.
# Os parâmetros são nome e prefixo da saudação. Assuma o prefixo "Olá", caso não seja fornecido o prefixo da saudação.

def saudacao(nome, prefixo="Olá"):
    return f"{prefixo} {nome}!"
print(saudacao("João"))
print(saudacao("Maria", "Oi"))

# Nomeação de parâmetros.
# Crie uma função que receba a largura e a altura como parâmetros
# e retorne o cálculo da área do retângulo. Utilize a nomeação de parâmetros.
# Chame a função só com os parâmetros; com um parâmetro nomeado; e com dois parâmetros nomeados.

def area_retangulo(largura, altura):
    return largura * altura

print(area_retangulo(10, 5))
print(area_retangulo(largura=10, altura=5))
print(area_retangulo(altura=5, largura=10))


#Packing de parâmetros (*args). 
# Crie uma função que some todos os números passados
# como parâmetros para qualquer quantidade de números.
# Use o empacotamento. Teste a função com diferentes quantidades de parâmetros.

def somar_numeros(*args):
    total = 0
    for num in args:
        total += num
    return total

print(somar_numeros(1, 2, 3))
print(somar_numeros(10, 20, 30, 40))
print(somar_numeros(5))


# Unpacking de parâmetros. 
# Crie uma função que receba dois parâmetros:
# base e expoente, e que calcule a potência da base pelo expoente.
# A passagem de parâmetros será via o desempacotamento de uma lista
# com exatamente dois valores.
# Teste também o mesmo desempacotamento com dicionário com exatamente duas chaves-valores.

def potencia(base, expoente):
    return base ** expoente


lista = [2, 3]
print(potencia(*lista))

dicionario = {"base": 2, "expoente": 3}
print(potencia(**dicionario))


# Função como parâmetro. Crie duas funções que calculem, respectivamente,
# o dobro e o quadrado de um número. Crie outra função que receba como parâmetro um valor e uma função,
# e que aplique essa função do parâmetro neste valor. Teste passado a função "dobro" e a função "quadrado".

def dobro(x):
    return 2 * x

def quadrado(x):
    return x ** 2

def aplicar_funcao(valor, funcao):
    return funcao(valor)

print(aplicar_funcao(5, dobro))
print(aplicar_funcao(5, quadrado))

# Recursão. Crie uma função recursiva que receba um valor inteiro como parâmetro e 
# implemente a operação de multiplicação somente com base na operação de adição.

def multiplicacao(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiplicacao(a, b - 1)
    else:
        return -multiplicacao(a, -b)
print(multiplicacao(5, 3))
print(multiplicacao(5, -3))


# Várias funções como parâmetros.
# Crie uma função chamada pipeline(x, *funcs) que aplique várias funções em sequência.
# Ou seja, "*funcs" vai associar uma sequência de diversas funções, inclusive nenhuma.
# Se a chamada for pipeline(10, f1, f2, f3), o resultado deve ser: f3(f2(f1(x))).

def pipeline(x, *funcs):
    for func in funcs:
        x = func(x)
    return x
def f1(x):
    return x + 1
def f2(x):
    return x * 2
def f3(x):
    return x ** 2
print(pipeline(10, f1, f2, f3))
print(pipeline(10, f2, f1))
print(pipeline(10))


#procedimento é uma função sem retorno, ou seja, que não tem a palavra-chave "return" em seu corpo.

def saudacao_procedimento(nome):
    print(f"Olá, {nome}!")

saudacao_procedimento("João")

#escreva uma função que retorne o maior de dois numeros valores esperados:

def maior(a, b):
    if a > b:
        return a
    else:
        return b
    
print(maior(5, 6))
print(maior(2, 1))
print(maior(7, 7))

#escreva uma funcao que receba dois numeros e retorne true se o primeiro for maior que o segundo, e false caso contrário:


def maior_que(a, b):
    return a > b
print(maior_que(8, 4))
print(maior_que(7, 3))
print(maior_que(5, 5))


#escreva a funcao que receba o lado de um quadrado e retorne a area do quadrado:

def area_quadrado(lado):
    return lado ** 2
print(area_quadrado(4))
print(area_quadrado(9))
print(area_quadrado(12))



