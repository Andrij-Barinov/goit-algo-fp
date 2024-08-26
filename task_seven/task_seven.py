# Імпортуємо необхідні бібліотеки
import random
import matplotlib.pyplot as plt
import pandas as pd

# Кількість симуляцій
num_simulations = 100000  # Визначаємо кількість симуляцій (кидань кубиків)

# Ініціалізуємо словник для підрахунку сум
sums_count = {i: 0 for i in range(2, 13)}  # Кожна можлива сума від 2 до 12

# Виконуємо симуляції
for _ in range(num_simulations):
    die1 = random.randint(1, 6)  # Випадкове число для першого кубика (від 1 до 6)
    die2 = random.randint(1, 6)  # Випадкове число для другого кубика (від 1 до 6)
    dice_sum = die1 + die2  # Обчислюємо суму чисел на двох кубиках
    sums_count[dice_sum] += 1  # Збільшуємо лічильник для відповідної суми

# Обчислюємо ймовірності для кожної суми
sums_probabilities = {sum_val: count / num_simulations for sum_val, count in sums_count.items()}

# Побудова графіка результатів
sums = list(sums_probabilities.keys())  # Список можливих сум
probabilities = list(sums_probabilities.values())  # Список відповідних ймовірностей

# Побудова гістограми ймовірностей
plt.bar(sums, probabilities, color='blue')
plt.xlabel('Сума чисел на кубиках')  # Підпис для осі X
plt.ylabel('Ймовірність')  # Підпис для осі Y
plt.title('Ймовірність появи суми чисел на двох кубиках (Монте-Карло)')  # Назва графіка
plt.xticks(sums)  # Відображення можливих сум на осі X
plt.show()  # Відображення графіка

# Аналітичні ймовірності для сум двох кубиків
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}

# Порівняння результатів Монте-Карло з аналітичними результатами
comparison = {sum_val: (sums_probabilities[sum_val], analytical_probabilities[sum_val]) for sum_val in sums_probabilities}

# Створення DataFrame для кращої візуалізації
df_comparison = pd.DataFrame(comparison, index=['Ймовірність Монте-Карло', 'Аналітична ймовірність']).T
df_comparison['Різниця'] = df_comparison['Ймовірність Монте-Карло'] - df_comparison['Аналітична ймовірність']

# Відображення таблиці порівняння
print(df_comparison)

# Збереження порівняння та висновків у файл readme.md
with open("readme.md", "w") as file:
    file.write("# Висновки щодо правильності розрахунків\n")
    file.write("Цей файл містить порівняння ймовірностей, отриманих за допомогою методу Монте-Карло, з теоретичними аналітичними ймовірностями.\n\n")
    file.write("## Порівняльна таблиця\n")
    file.write(df_comparison.to_markdown())
    file.write("\n\n## Висновок\n")
    file.write("Результати симуляції методом Монте-Карло загалом узгоджуються з аналітичними розрахунками. Невеликі відхилення є наслідком випадковості в симуляції, однак з великою кількістю повторень вони мають тенденцію до зменшення. Це підтверджує правильність як методу Монте-Карло, так і теоретичних розрахунків.")
