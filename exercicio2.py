def verifica_paridade(numero):
    if numero % 2 == 0:
        return "P"
    else:
        return "I"

def main():
    n = int(input())
    resultado = verifica_paridade(n)
    print(resultado)

if __name__ == "__main__":
    main()