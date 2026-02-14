def numero_perfeito(n):
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    return soma_divisores == n

def main():
    numero = int(input())
    print(numero_perfeito(numero))

if __name__ == "__main__":
    main()