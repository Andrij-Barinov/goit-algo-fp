import heapq

# Функція для реалізації алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація словника для зберігання мінімальних відстаней
    dist = {vertex: float('inf') for vertex in graph}
    dist[start] = 0
    
    # Ініціалізація словника для зберігання попередніх вершин
    previous = {vertex: None for vertex in graph}
    
    # Ініціалізація пріоритетної черги (бінарної купи)
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    # Основний цикл алгоритму
    while priority_queue:
        # Отримання вершини з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за збережену, пропускаємо вершину
        if current_distance > dist[current_vertex]:
            continue

        # Оновлення відстаней до сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях, оновлюємо відстань та додаємо в чергу
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    # Повернення словників з мінімальними відстанями та попередніми вершинами
    return dist, previous

# Створення графа у вигляді словника
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Запуск алгоритму Дейкстри від початкової вершини 'A'
start_vertex = 'A'
distances, previous_vertices = dijkstra(graph, start_vertex)

# Виведення результатів
print("Найкоротші відстані від вершини", start_vertex)
for vertex, distance in distances.items():
    print(f"До вершини {vertex}: {distance}")

print("\nПопередні вершини на найкоротших шляхах")
for vertex, previous in previous_vertices.items():
    print(f"До вершини {vertex} через вершину {previous}")
