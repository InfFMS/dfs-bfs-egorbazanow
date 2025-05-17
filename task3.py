# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D
# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена
graf = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": [],
    "D": []
}
indegree = {}
for v in graf:
    indegree[v] = 0

for v in graf:
    for u in graf[v]:
        indegree[u] += 1
queue = []
for v in graf:
    if indegree[v] == 0:
        queue.append(v)
result = []
while queue:
    node = queue.pop(0)
    result.append(node)
    for neighbor in graf[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
print(result)
