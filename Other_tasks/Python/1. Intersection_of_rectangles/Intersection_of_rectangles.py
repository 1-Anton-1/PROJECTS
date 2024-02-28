def intersection_of_rectangles(x, y, w, h):
    """
    Функция нахождения области пересечения нового прямоугольника с заданным
    ((x, y, w, h) = (0, 0, 1000, 500))
    :param x: Координата x левого нижнего угла нового прямоугольника
    :param y: Координата y левого нижнего угла нового прямоугольника
    :param w: Ширина нового прямоугольника
    :param h: Высота нового прямоугольника
    :return: Вывод или None (пересечения нет) или x, y, w, h - для области пересечения
    """
    if x == 1000:
        if y == 500:
            return x, y, 0, 0  # Пересечение точка
        if 0 < y and y + h > 0:
            return x, y, 0, min(abs(abs(y) - h), 500)  # Пересечение отрезок
        if 0 < y < 500 and abs(y) - h > 0:
            return x, y, 0, min(abs(abs(y) - h), 500)  # Пересечение отрезок
    if y == 500:
        if x < 0 and x + w > 0:
            return 0, y, min(abs(abs(x) - w), 1000), 0  # Пересечение отрезок
        if 0 < x < 1000 and abs(x) - w > 0:
            return x, y, min(abs(abs(x) - w), 1000), 0  # Пересечение отрезок
    if 0 <= x < 1000 and 0 <= y < 500:  # Для I-ой четверти
        return x, y, min(1000 - x, w), min(500 - y, h)
    if x < 0 <= y < 500:  # Для II-ой четверти
        if w - abs(x) < 0:
            return None
        return 0, y, min(abs(x + w), 1000), min(500 - y, h)
    if x < 0 > y:  # Для III-ой четверти
        if h - abs(y) < 0 or w - abs(x) < 0:
            return None
        return 0, 0, min(abs(x + w), 1000), min(abs(y + h), 500)
    if y < 0 <= x < 1000:  # Для IV-ой четверти
        if h - abs(y) < 0:
            return None
        return x, 0, min(1000 - x, 1000), min(abs(y + h), 500)
    return None


# Tests:
print('Tests for I четверти координат:')
print(f'(x=800, y=400, w=400, h=200): {intersection_of_rectangles(800, 400, 400, 200)}')  # Есть пересечение, находим закрашенную область
print(f'(x=1200, y=400, w=400, h=200): {intersection_of_rectangles(1200, 400, 400, 200)}')  # Есть пересечение, находим закрашенную область
print(f'(x=1000, y=400, w=400, h=200): {intersection_of_rectangles(1000, 400, 400, 200)}')  # Пересечение - отрезок параллельный оси ординат
print()

print('Tests for II четверти координат:')
print(f'(x=-100, y=10, w=1000, h=500): {intersection_of_rectangles(-100, 10, 1000, 500)}')
print(f'(x=-10, y=600, w=400, h=200): {intersection_of_rectangles(-10, 600, 400, 200)}')
print(f'(x=-200, y=400, w=800, h=20): {intersection_of_rectangles(-200, 400, 800, 20)}')
print()

print('Tests for III четверти координат:')
print(f'(x=-100, y=-100, w=1000, h=500): {intersection_of_rectangles(-100, -100, 1000, 500)}')
print(f'(x=-10, y=-500, w=50, h=1000): {intersection_of_rectangles(-10, -500, 50, 1000)}')
print(f'(x=-1000, y=-200, w=5000, h=1000): {intersection_of_rectangles(-1000, -200, 5000, 1000)}')
print()

print('Tests for IV четверти координат:')
print(f'(x=0, y=-100, w=1000, h=500): {intersection_of_rectangles(0, -100, 1000, 500)}')
print(f'(x=10, y=-600, w=1000, h=500): {intersection_of_rectangles(10, -600, 1000, 500)}')
print(f'(x=100, y=-200, w=1000, h=1000): {intersection_of_rectangles(100, -200, 1000, 1000)}')
print()

print('Tests на краевые эффекты:')
print(f'(x=-800, y=500, w=1200, h=200): {intersection_of_rectangles(-800, 500, 1200, 200)}')  # Пересечение - отрезок параллельный оси абцисс
print(f'(x=1000, y=50, w=40, h=2000): {intersection_of_rectangles(1000, 50, 40, 2000)}')  # Пересечение - отрезок параллельный оси ординат
print(f'(x=1000, y=500, w=400, h=200): {intersection_of_rectangles(1000, 500, 400, 200)}')  # Пересечение - точка
