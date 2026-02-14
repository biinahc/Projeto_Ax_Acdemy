
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media
nota1 = float(input())
nota2 = float(input())  
nota3 = float(input())
media_final = calcular_media(nota1, nota2, nota3)

print("{:.2f}".format(media_final))