import time
import logging
from multiprocessing import Pool, current_process,cpu_count

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def factorize(*numbers):
    factors = []
    for num in numbers:
        factors.append([i for i in range(1, num + 1) if num % i == 0])
    return factors


if __name__ == '__main__':
    # Синхронне виконання функції 
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    logger.debug(f"Sync execution time: {end_time - start_time} seconds")
    logger.debug(f"a: {a}")
    logger.debug(f"b: {b}")
    logger.debug(f"c: {c}")
    logger.debug(f"d: {d}")
    # Паралельне виконання функції
    start_time = time.time()
    with Pool(processes=cpu_count()) as pool:
        a,b,c,d = pool.map(factorize, [128,255,99999,10651060])
    end_time = time.time()
    logger.debug(f"Parallel execution time: {end_time - start_time} seconds")
    logger.debug(f"a: {a}")
    logger.debug(f"b: {b}")
    logger.debug(f"c: {c}")
    logger.debug(f"d: {d}")
   