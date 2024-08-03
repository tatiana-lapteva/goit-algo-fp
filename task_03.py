"""
Завдання 3. Дерева, алгоритм Дейкстри
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
використовуючи бінарну купу. Завдання включає створення графа, використання піраміди 
для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.
"""

import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  

    def dijkstra(self, start):
        # Ініціалізація мін-купи
        heap = []
        heapq.heappush(heap, (0, start))
        
        # Ініціалізація відстаней та батьківських вершин
        distances = {vertex: float('infinity') for vertex in self.edges}
        distances[start] = 0
        parents = {vertex: None for vertex in self.edges}
        
        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_vertex
                    heapq.heappush(heap, (distance, neighbor))
        
        return distances, parents


if __name__ == "__main__":

    graph = Graph()
    edges = [
        ('A', 'B', 4), ('A', 'H', 8), ('B', 'C', 8), ('B', 'H', 11), ('C', 'D', 7), 
        ('C', 'I', 2), ('C', 'F', 4), ('D', 'E', 9), ('D', 'F', 14), ('E', 'F', 10),
        ('F', 'G', 2), ('G', 'H', 1), ('G', 'I', 6), ('H', 'I', 7)
    ]

    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    start_vertex = 'A'
    distances, parents = graph.dijkstra(start_vertex)

    print(f"Відстані від вершини {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"Вершина {vertex}: {distance}")

    print("\nБатьківські вершини:")
    for vertex, parent in parents.items():
        print(f"Вершина {vertex}: {parent}")
