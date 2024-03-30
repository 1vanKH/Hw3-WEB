import time
from multiprocessing import Pool, cpu_count

def factorize(*numbers):
    factors_list = []
    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        factors_list.append(factors)
    return factors_list

# Тестування функції
if __name__ == '__main__':
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"Sync execution time: {end_time - start_time} seconds")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")

    # Покращення продуктивності з використанням паралельних обчислень
    start_time_parallel = time.time()
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(factorize, [128, 255, 99999, 10651060])
    a, b, c, d = results
    end_time_parallel = time.time()
    print(f"Parallel execution time: {end_time_parallel - start_time_parallel} seconds")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")