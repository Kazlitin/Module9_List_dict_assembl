def square_and_filter(lst):
    # Возведение каждого элемента в квадрат с помощью map
    squared_list = list(map(lambda x: x ** 2, lst))

    # Фильтрация списка квадратов, оставляя только нечетные значения
    odd_squares = list(filter(lambda x: x % 2 != 0, squared_list))

    return odd_squares


# Исходный список
input_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# Получаем список нечетных квадратов
result = square_and_filter(input_list)
print(result)

