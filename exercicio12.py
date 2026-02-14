def semanas(horas_semanais):
    if horas_semanais > 10 or horas_semanais <= 0:
        return "erro"
    return 200 / horas_semanais

h = float(input())
print(semanas(h))