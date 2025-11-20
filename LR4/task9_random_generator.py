import random


def random_number_generator(start: int, end: int, count: int = None):
    generated = 0

    while count is None or generated < count:
        yield random.randint(start, end)
        generated += 1


print("10 случайных чисел от 1 до 100:")
random_numbers = list(random_number_generator(1, 100, 10))
print(random_numbers)

negative_nums = list(random_number_generator(-10, -1, 3))
print(f"\nОтрицательные (-10 до -1): {negative_nums}")

large_nums = list(random_number_generator(1000, 2000, 3))
print(f"\nБольшие числа (1000-2000): {large_nums}")

single_num = list(random_number_generator(42, 42, 3))
print(f"\nОдно число (42): {single_num}")

print("\nБесконечный генератор:")
generator = random_number_generator(1, 100)
i = 0
for num in generator:
    if i >= 10:
        break
    print(f"Число {i+1}: {num}")
    i+=1