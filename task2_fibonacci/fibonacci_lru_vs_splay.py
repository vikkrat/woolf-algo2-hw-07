import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
from splay_tree import SplayTree


@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n, tree):
    cached = tree.search(n)
    if cached is not None:
        return cached
    if n <= 1:
        tree.insert(n, n)
        return n
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


def benchmark():
    ns = list(range(0, 1000, 50))
    lru_times = []
    splay_times = []

    print(f"{'n':<10}{'LRU Cache Time (s)':<20}{'Splay Tree Time (s)':<20}")
    print("-" * 50)

    for n in ns:
        lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=3) / 3
        tree = SplayTree()
        splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=3) / 3

        lru_times.append(lru_time)
        splay_times.append(splay_time)

        print(f"{n:<10}{lru_time:<20.8f}{splay_time:<20.8f}")

    plt.plot(ns, lru_times, label="LRU Cache")
    plt.plot(ns, splay_times, label="Splay Tree")
    plt.xlabel("n")
    plt.ylabel("Time (s)")
    plt.title("Порівняння часу обчислення чисел Фібоначчі")
    plt.legend()
    plt.grid(True)
    plt.savefig("task2_fibonacci/screenshots/task2_fibonacci_comparison.png")
    plt.show()


if __name__ == "__main__":
    benchmark()
