def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості для кожної страви
    items_by_ratio = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    selected_items = []  # Список обраних страв
    total_cost = 0  # Змінна для відстеження поточної вартості

    # Перебір страв у порядку спадання співвідношення калорій до вартості
    for item, info in items_by_ratio:
        if total_cost + info["cost"] <= budget:  # Перевірка, чи не перевищуємо бюджет
            selected_items.append(item)  # Додаємо страву до обраного набору
            total_cost += info["cost"]  # Оновлюємо загальну вартість
    
    return selected_items  # Повертаємо список обраних страв

def dynamic_programming(items, budget):
    n = len(items)  # Кількість страв
    items_list = list(items.keys())  # Список назв страв
    
    # Ініціалізація таблиці для динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнення таблиці dp
    for i in range(1, n + 1):
        item = items_list[i-1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        
        for j in range(1, budget + 1):
            if cost <= j:
                # Вибір між включенням та виключенням страви для максимізації калорійності
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + calories)
            else:
                # Якщо вартість страви перевищує поточний бюджет, залишаємо попереднє значення
                dp[i][j] = dp[i-1][j]

    # Відновлення оптимального набору страв
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:  # Перевірка, чи була страва включена в оптимальний набір
            selected_items.append(items_list[i-1])
            j -= items[items_list[i-1]]["cost"]  # Зменшуємо бюджет на вартість включеної страви
    
    return selected_items  # Повертаємо список обраних страв

# Приклад даних
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Приклад бюджету
budget = 100

# Виведення результатів роботи обох алгоритмів
print("Greedy Algorithm Result:", greedy_algorithm(items, budget))
print("Dynamic Programming Result:", dynamic_programming(items, budget))
