# Дан взвешенный граф.
# Необходимо ответить на следующие вопросы:
# 
# 1. Найти длину всех наикротчайших маршрутов из 'Home' в любую точку на графе? (Просто применить алгоритм Дейкстры)
# 2. Найту как выглядит самый кротчайший маршрут из 'Home' в 'Theater' (вывести последовательность прохождения вершин)?
# Подсказка:
# Удобно хранить значения о пройденном маршруте в виде словаря, где ключ - это текущая вершина, а значение - вершина, из которой мы попали в текущую
# Потом в конце нужно будет просто пройтись по такому словарю от финиша к старту и развернуть его.
#
# Входные данные:
# city_map = {
#     'Home': {'Park': 2, 'School': 5, 'Mail': 10},
#     'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
#     'School': {'Home': 5, 'Library': 6, 'Mail': 2},
#     'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
#     'Library': {'School': 6, 'Hospital': 1},
#     'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
#     'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
#     'Museum': {'Park': 4, 'Shop': 5},
#     'Shop': {'Museum': 5, 'Theater': 1},
#     'Theater': {'Shop': 1, 'Cafe': 8},
#     'Office': {'Cafe': 7, 'Hospital': 4}
# }
city_map = {
    'Home': {'Park': 2, 'School': 5, 'Mail': 10},
    'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
    'School': {'Home': 5, 'Library': 6, 'Mail': 2},
    'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
    'Library': {'School': 6, 'Hospital': 1},
    'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
    'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
    'Museum': {'Park': 4, 'Shop': 5},
    'Shop': {'Museum': 5, 'Theater': 1},
    'Theater': {'Shop': 1, 'Cafe': 8},
    'Office': {'Cafe': 7, 'Hospital': 4}
}

start = 'Home'
finish = 'Theater'

import math

dist = {}
prev = {}
unvisited = set(city_map.keys())

for v in city_map:
    dist[v] = math.inf
dist[start] = 0

while unvisited:
    current = None
    current_dist = math.inf
    for v in unvisited:
        if dist[v] < current_dist:
            current_dist = dist[v]
            current = v

    if current is None:
        break

    if current == finish:
        break
    unvisited.remove(current)

    for neighbor, weight in city_map[current].items():
        if neighbor in unvisited:
            new_dist = dist[current] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current
print("Длины кратчайших путей от Home:")
for v in dist:
    print(f"{v}: {dist[v]}")

# 2. Восстановить путь от start до finish
if finish not in prev and finish != start:
    print("Путь от Home до Theater не найден")
else:
    path = []
    current = finish
    while current != start:
        path.append(current)
        current = prev[current]
    path.append(start)
    path.reverse()

    print("Кратчайший путь от Home до Theater:")
    print(path)


