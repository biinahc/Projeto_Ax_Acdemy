def converte_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

def main():
    h = int(input())
    m = int(input())
    s = int(input())
    
    total = converte_para_segundos(h, m, s)
    print("{} segundos".format(total))

if __name__ == "__main__":
    main()