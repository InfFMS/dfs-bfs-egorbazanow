# Напишите алгоритм поиска в ширину (BFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать BFS — обход графа в ширину.
# 2.Вернуть самый коротки маршрут от точки старта до точки назначения.

# Пример входных данных
# city_map = {  
#     'Home': ['Park', 'School', 'Mail'],  
#     'Park': ['Home', 'Museum', 'Cafe'],  
#     'School': ['Home', 'Library', 'Mail'],  
#     'Mail': ['Home', 'School', 'Hospital'],  
#     'Library': ['School', 'Hospital'],  
#     'Hospital': ['Library', 'Mail', 'Office'],  
#     'Cafe': ['Park', 'Theater', 'Office'],  
#     'Museum': ['Park', 'Shop'],  
#     'Shop': ['Museum', 'Theater'],  
#     'Theater': ['Shop', 'Cafe'],  
#     'Office': ['Cafe', 'Hospital']  
# }
# start = "Home"
# finish = "Theater"
#
# Пример выходных данных
# ['Home', 'Park', 'Cafe', 'Theater']
from collections import deque

city_map = {
    'Home': ['Park', 'School', 'Mail'],
    'Park': ['Home', 'Museum', 'Cafe'],
    'School': ['Home', 'Library', 'Mail'],
    'Mail': ['Home', 'School', 'Hospital'],
    'Library': ['School', 'Hospital'],
    'Hospital': ['Library', 'Mail', 'Office'],
    'Cafe': ['Park', 'Theater', 'Office'],
    'Museum': ['Park', 'Shop'],
    'Shop': ['Museum', 'Theater'],
    'Theater': ['Shop', 'Cafe'],
    'Office': ['Cafe', 'Hospital']
}

start = str(input())
finish = str(input())

queue = deque()
queue.append([start])
visited = set()

while queue:
    path = queue.popleft()
    node = path[-1]

    if node == finish:
        print(path)
        break

    if node not in visited:
        visited.add(node)
        for neighbor in city_map[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append(new_path)
