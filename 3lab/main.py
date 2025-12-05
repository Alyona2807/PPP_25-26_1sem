def recursive_shortest_path(graph, start, end, visited=None, path=None, min_path=None, min_distance=float('inf')):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    else:
        path = path + [start]

    # Помечаем текущую вершину как посещённую
    visited.add(start)

    # Если достигли целевую вершину
    if start == end:
        # Вычисляем сумму расстояний по текущему маршруту
        distance = 0
        for i in range(len(path) - 1):
            src = path[i]
            dst = path[i + 1]
            weight = graph[src][dst]
            distance += weight
        print(f"Текущий путь: {path} с расстоянием: {distance}")

        # Обновляем минимальный маршрут
        if distance < min_distance:
            min_distance = distance
            min_path = list(path)
        return min_path, min_distance

    # Проходим по смежным вершинам
    for neighbor in range(len(graph)):
        if graph[start][neighbor] != 0 and neighbor not in visited:
            print(f"Обработка маршрута: {path} -> Вершина: {neighbor}")
            candidate_path, candidate_distance = recursive_shortest_path(
                graph,
                neighbor,
                end,
                visited=set(visited),
                path=list(path),
                min_path=min_path,
                min_distance=min_distance
            )
            # Обновляем минимальный путь, если нашли лучше
            if candidate_path is not None and candidate_distance < min_distance:
                min_path = candidate_path
                min_distance = candidate_distance

    return min_path, min_distance

# Пример таблицы смежности (веса, 0 — отсутствие ребра)
graph = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]

start_vertex = 0
end_vertex = 4

# Запуск поиска
shortest_path, shortest_distance = recursive_shortest_path(graph, start_vertex, end_vertex)
print(f"\nКратчайший путь: {shortest_path} с расстоянием: {shortest_distance}")
