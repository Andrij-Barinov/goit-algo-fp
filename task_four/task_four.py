import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас Node для створення вузлів дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла (використовується для візуалізації)
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

# Функція для додавання вузлів і зв'язків у граф, що представляє дерево
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо вузол у граф з його ідентифікатором, кольором і значенням
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:  # Якщо існує лівий дочірній вузол
            graph.add_edge(node.id, node.left.id)  # Додаємо зв'язок з лівим дочірнім вузлом
            l = x - 1 / 2 ** layer  # Визначаємо позицію лівого вузла на графіку
            pos[node.left.id] = (l, y - 1)  # Зберігаємо позицію
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Рекурсивно додаємо дочірні вузли
        if node.right:  # Якщо існує правий дочірній вузол
            graph.add_edge(node.id, node.right.id)  # Додаємо зв'язок з правим дочірнім вузлом
            r = x + 1 / 2 ** layer  # Визначаємо позицію правого вузла на графіку
            pos[node.right.id] = (r, y - 1)  # Зберігаємо позицію
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Рекурсивно додаємо дочірні вузли
    return graph  # Повертаємо граф

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створюємо направлений граф
    pos = {tree_root.id: (0, 0)}  # Початкова позиція для кореневого вузла
    tree = add_edges(tree, tree_root, pos)  # Додаємо вузли та зв'язки в граф

    # Отримуємо кольори для кожного вузла
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    # Отримуємо значення для міток кожного вузла
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    # Візуалізація графіка
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()  # Відображаємо графік

# Функція для вставки елемента в бінарну купу
def insert_heap(root, value):
    if root is None:  # Якщо кореня немає, створюємо новий вузол
        return Node(value)
    else:
        # Якщо значення менше поточного вузла, йдемо вліво
        if value < root.val:
            if root.left is None:  # Якщо лівого дочірнього вузла немає, створюємо його
                root.left = Node(value)
            else:
                insert_heap(root.left, value)  # Рекурсивно вставляємо в ліве піддерево
        else:
            # Якщо значення більше або дорівнює поточному вузлу, йдемо вправо
            if root.right is None:  # Якщо правого дочірнього вузла немає, створюємо його
                root.right = Node(value)
            else:
                insert_heap(root.right, value)  # Рекурсивно вставляємо в праве піддерево
    return root  # Повертаємо корінь дерева

# Функція для побудови бінарної купи з масиву значень
def build_heap(values):
    if not values:  # Якщо масив порожній, повертаємо None
        return None
    root = Node(values[0])  # Створюємо кореневий вузол з першого значення масиву
    for value in values[1:]:  # Вставляємо інші значення в купу
        insert_heap(root, value)
    return root  # Повертаємо корінь дерева

# Побудова бінарної купи з масиву значень
heap_values = [15, 10, 8, 12, 20, 6, 25, 30]
heap_root = build_heap(heap_values)

# Візуалізація бінарної купи
draw_tree(heap_root)
