import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from collections import deque
import time

# Клас Node для створення вузлів дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Функція для додавання вузлів і зв'язків у граф
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = colors if colors else [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для побудови бінарної купи з масиву значень
def build_heap(values):
    if not values:
        return None
    root = Node(values[0])
    for value in values[1:]:
        insert_heap(root, value)
    return root

# Функція для вставки елемента в бінарну купу
def insert_heap(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.val:
            if root.left is None:
                root.left = Node(value)
            else:
                insert_heap(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                insert_heap(root.right, value)
    return root

# Функція для отримання градієнта кольорів
def get_color_gradient(n, start_color, end_color):
    colors = list(mcolors.LinearSegmentedColormap.from_list("", [start_color, end_color])(np.linspace(0, 1, n)))
    return [mcolors.rgb2hex(color) for color in colors]

# Функція для обходу дерева в ширину (BFS)
def bfs(tree_root):
    queue = deque([tree_root])
    visited = []
    while queue:
        node = queue.popleft()  # Виймаємо елемент з початку черги
        visited.append(node)
        if node.left:
            queue.append(node.left)  # Додаємо лівого нащадка до черги
        if node.right:
            queue.append(node.right)  # Додаємо правого нащадка до черги
    return visited

# Функція для обходу дерева в глибину (DFS)
def dfs(tree_root):
    stack = [tree_root]
    visited = []
    while stack:
        node = stack.pop()  # Виймаємо елемент з кінця стеку
        visited.append(node)
        if node.right:
            stack.append(node.right)  # Додаємо правого нащадка до стеку
        if node.left:
            stack.append(node.left)  # Додаємо лівого нащадка до стеку
    return visited

# Функція для скидання кольору всіх вузлів
def reset_colors(tree_root, default_color="skyblue"):
    if tree_root is not None:
        tree_root.color = default_color
        reset_colors(tree_root.left, default_color)
        reset_colors(tree_root.right, default_color)

# Візуалізація обходу дерева
def visualize_traversal(tree_root, traversal_func, start_color="#00008B", end_color="#ADD8E6"):
    visited_nodes = traversal_func(tree_root)
    color_gradient = get_color_gradient(len(visited_nodes), start_color, end_color)

    for i, node in enumerate(visited_nodes):
        node.color = color_gradient[i]
        draw_tree(tree_root, colors=[n.color for n in visited_nodes])
        time.sleep(1)  # Додаємо затримку, щоб бачити кожен крок обходу

# Побудова бінарної купи з масиву значень
heap_values = [15, 10, 8, 12, 20, 6, 25, 30]
heap_root = build_heap(heap_values)

# Візуалізація обходу в ширину (BFS)
print("BFS Traversal:")
visualize_traversal(heap_root, bfs)

# Скидання кольорів вузлів перед наступним обходом
reset_colors(heap_root)

# Візуалізація обходу в глибину (DFS)
print("DFS Traversal:")
visualize_traversal(heap_root, dfs)
