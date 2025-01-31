#1. Написати функцію draw_line, яку можна буде викликати так: draw_line(20, '@', true) 
# і при цьому намалюється горизонтальна лінія, що складається з 20 «собачок». Якщо передати в останньому параметрі false — лінія стане вертикальною.
def draw_line(number, symbol, horizontal):
    if horizontal:
        print(number * symbol)
    else:
        for _ in range(number):
            print(symbol)
draw_line(20, '@', True)
draw_line(20, '@', False)

#2. Написати функцію draw_rectangle, яка виводить на екран прямокутник. Функція приймає такі параметри: ширина, висота, символ рамки, символ заповнення.
#  У функції мають бути параметри за замовчуванням.
def draw_rectangle(width, height, border_symbol, fill_symbol):
    print(border_symbol * width)
    for _ in range(height - 2):
        print(border_symbol + fill_symbol * (width - 2) + border_symbol)
    if height > 1:
        print(border_symbol * width)
draw_rectangle(14, 5, '+', ' ')

#3. Написати функцію, яка перевіряє, чи є передане їй число простим (і повертає True або False). Число називається простим, якщо воно ділиться без залишку
# тільки на себе і на одиницю.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(4))
print(is_prime(11))

#4. Написати функцію, яка отримує як параметри 2 цілі числа і повертає суму чисел із діапазону між ними.
def sum_range(a, b):
    start = min(a, b)
    end = max(a, b)
    return sum(range(start, end + 1))
result = sum_range(1, 5)
print(result)

#5. Написати функцію, що повертає середнє арифметичне елементів переданого їй списку.
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5]
result = average(numbers)
print(result) 

#6.Написати функцію, що показує на екрані мінімум і максимум (значення та індекс) серед елементів переданого їй списку.
def find_min_max(list):
    if len(list) == 0:
        print("Список порожній!")
        return 
    min_value = min(list)
    max_value = max(list)
    min_index = list.index(min_value)
    max_index = list.index(max_value)
    print("Мінімум: значення =", min_value, "індекс =", min_index)
    print("Максимум: значення =", max_value, "індекс =", max_index)
find_min_max([2, 14, 3, 9, 1, 18])
