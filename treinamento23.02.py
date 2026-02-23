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




