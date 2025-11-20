def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_generator(limit: int = None):
    n = 2
    count = 0

    while limit is None or count < limit:
        if is_prime(n):
            yield n
            count += 1
        n += 1


def demonstrate_prime_generator():

    print("Первые 20 простых чисел:")
    primes = []
    for prime in prime_generator(20):
        primes.append(prime)
    print(primes)

    print("\nПростые числа до 100:")
    primes_under_100 = []
    for prime in prime_generator():
        if prime > 100:
            break
        primes_under_100.append(prime)
    print(primes_under_100)

    print("\nПростые числа от 50 до 100 (через filter):")
    numbers = range(50, 101)
    primes_filtered = list(filter(is_prime, numbers))
    print(primes_filtered)


demonstrate_prime_generator()
