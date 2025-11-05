class MathOperations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * MathOperations.factorial(n - 1)

    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":

    print("Базовые операции:")
    print(f"5 + 3 = {MathOperations.add(5, 3)}")
    print(f"5 * 3 = {MathOperations.multiply(5, 3)}")
    print(f"Факториал 6 = {MathOperations.factorial(6)}")

    print("\nПроверка простых чисел:")
    numbers = [2, 3, 4, 5, 17, 25, 29]
    for num in numbers:
        prime_status = "простое" if MathOperations.is_prime(num) else "составное"
        print(f"Число {num} - {prime_status}")
