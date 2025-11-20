def map_squares():
    numbers = list(range(1, 11))
    print(f"Исходный список: {numbers}")

    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Квадраты чисел: {squares}")


map_squares()
