# Дан список курсов университета и их пререквизитов. Нужно определить,
# можно ли окончить все курсы, и если да, то вывести один из возможных порядков их изучения.
#
# Формат ввода:
# Первая строка: n (число курсов), m (число зависимостей).
# Следующие m строк: a b (курс b требует прохождения курса a).
#
# Формат вывода:
# Если циклов нет, вывести любой допустимый порядок курсов.
# Если есть цикл, вывести -1.

# Пример 1 (нет циклов)
# Ввод:
# 4 3
# 1 2
# 2 3
# 1 4
# Граф:
# 1 → 2 → 3
# 1 → 4
# Вывод:
# 1 2 4 3  # Или 1 4 2 3

# Пример 2 (есть цикл)
# Ввод:
# 3 3
# 1 2
# 2 3
# 3 1
# Граф:
# 1 → 2 → 3 → 1 (цикл!)
# Вывод:
# -1
n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
indegree = {i: 0 for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    node = queue.pop(0)
    result.append(node)
    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

if len(result) == n:
    print(*result)
else:
    print(-1)
