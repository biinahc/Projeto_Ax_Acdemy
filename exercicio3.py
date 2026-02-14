def calcula_percentual(num, perc):
    return (num * perc) / 100

def main():

    numero = float(input())

    percentual = float(input())
    
    resultado = calcula_percentual(numero, percentual)
    print("{:.2f}".format(resultado))

if __name__ == "__main__":
    main()