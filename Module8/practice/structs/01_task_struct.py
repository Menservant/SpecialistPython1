# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
gen = map(float, distances)
mas = []
for el in gen:
    mas.append((el * 3.28084))

print(f"{mas}")
