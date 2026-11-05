import random
import time

from merge_sort import merge_sort

DATA_SIZE = 10000
RANDOM_SEED = 42

if __name__ == "__main__":
    # Generate a larger, reproducible dataset of integers.
    random.seed(RANDOM_SEED)
    data = [random.randint(0, 100000) for _ in range(DATA_SIZE)]
    print("Original size:", len(data))
    print("Original (first 10):", data[:10])

    # Measure only the sorting call using a high-resolution monotonic clock.
    start_time = time.perf_counter()
    sorted_data = merge_sort(data)
    elapsed = time.perf_counter() - start_time

    print("sorted (first 10):", sorted_data[:10])
    print(f"merge sort execution time: {elapsed:.6f} seconds")
