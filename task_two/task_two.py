import turtle
import math

def draw_tree(t, branch_length, angle, level):
    if level > 0:
        # Малюємо основну гілку
        t.forward(branch_length)
        # Поворот вліво і малювання лівої гілки
        t.left(angle)
        draw_tree(t, branch_length * 0.7, angle, level - 1)
        # Повертаємося до вихідної точки
        t.right(2 * angle)
        # Малюємо праву гілку
        draw_tree(t, branch_length * 0.7, angle, level - 1)
        # Повертаємося до початкового положення
        t.left(angle)
        t.backward(branch_length)

def pythagoras_tree(level):
    # Ініціалізуємо вікно turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Налаштовуємо turtle
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Повертаємо на 90 градусів, щоб малювати вверх
    
    # Запускаємо малювання дерева
    draw_tree(t, 100, 30, level)
    
    # Завершуємо малювання
    turtle.done()

if __name__ == "__main__":
    # Просимо користувача ввести рівень рекурсії
    level = int(input("Введіть рівень рекурсії (рекомендується від 1 до 10): "))
    pythagoras_tree(level)