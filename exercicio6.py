def verifica_valor(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "valor nulo"

def main():
    numero = int(input())
    resultado = verifica_valor(numero)
    print(resultado)

if __name__ == "__main__":
    main()