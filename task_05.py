"""
Використовуючи код із завдання 4 для побудови бінарного дерева, 
необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами, 
використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних 
до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні 
має отримувати унікальний колір, який візуально відображає порядок обходу.
"""


import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.value = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.value) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)
    return node


def collect_bfs_steps(node):
    steps = []
    values = []
    if not node:
        return steps, values
    
    queue = deque([node])
    while queue:
        current = queue.popleft()
        steps.append(current)
        values.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return steps, values


def collect_dfs_steps(node):
    steps = []
    values = []
    if not node:
        return steps, values
    
    stack = [node]
    while stack:
        current = stack.pop()
        steps.append(current)
        values.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return steps, values


def generate_colors(base_color, num_tints):
    base_rgb = tuple(int(base_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    tints = []
    for i in range(num_tints): 
        factor = i / (num_tints)
        tint_rgb = tuple(base_rgb[j] + (1 - base_rgb[j]) * factor for j in range(3))
        tints.append(tint_rgb)
    return tints[:num_tints]


def assign_colors_to_nodes(colors, path):
    for step, color in zip(path, colors):
        step.color = color
    return [step.color for step in path]


def draw_tree_traversal(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    plt.title(title, fontsize=20)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    plt.show()



if __name__ == "__main__":

    # Create Tree
    data = [2, 3, 6, 1, 7, 3, 8, 1, 5]
    heapq.heapify(data)
    tree = heap_to_tree(data)


    # Generate tints:
    tints = generate_colors("1296F0", len(data))


    # Visualize BFS
    bfs, bfs_values = collect_bfs_steps(tree)

    # assign colors:
    list = assign_colors_to_nodes(tints, bfs)

    print(f"Breadth-first search order: {bfs_values}")
    draw_tree_traversal(tree, "Breadth-first search")
    print()

    # Visualize DFS

    dfs, dfs_values = collect_dfs_steps(tree)

    # assign colors:
    list = assign_colors_to_nodes(tints, dfs)

    print(f"Depth-first search order: {dfs_values}")
    draw_tree_traversal(tree, "Depth-first search")
