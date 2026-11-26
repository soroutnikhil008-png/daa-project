"""Run the demo and the performance comparison.
Usage: python main.py [capacity]
"""
import csv
import random
import sys
import time

from knapsack import Product, fractional_knapsack, knapsack_01


def load_products(path="data/products.csv"):
    with open(path, newline="") as f:
        return [Product(r["name"], int(r["weight"]), int(r["profit"]))
                for r in csv.DictReader(f)]


def demo(capacity):
    products = load_products()
    print(f"=== Warehouse capacity: {capacity} ===\n")

    profit, chosen = fractional_knapsack(products, capacity)
    print(f"[Greedy - Fractional Knapsack] Total profit: {profit:.2f}")
    for p, frac in chosen:
        print(f"   {p.name:<12} taken {frac*100:.0f}%")

    profit, chosen = knapsack_01(products, capacity)
    print(f"\n[Dynamic Programming - 0/1 Knapsack] Total profit: {profit}")
    for p in chosen:
        print(f"   {p.name:<12} weight={p.weight} profit={p.profit}")
    print(f"   Total weight used: {sum(p.weight for p in chosen)}")


def benchmark():
    print("\n=== Performance comparison (random data) ===")
    print(f"{'Items':>6} {'Capacity':>9} {'Greedy(ms)':>11} {'DP(ms)':>9} "
          f"{'Greedy profit':>14} {'DP profit':>10}")
    random.seed(42)
    for n in (10, 100, 500, 1000):
        capacity = n * 5
        items = [Product(f"P{i}", random.randint(1, 20), random.randint(1, 100))
                 for i in range(n)]
        t = time.perf_counter()
        gp, _ = fractional_knapsack(items, capacity)
        g_ms = (time.perf_counter() - t) * 1000
        t = time.perf_counter()
        dp_profit, _ = knapsack_01(items, capacity)
        d_ms = (time.perf_counter() - t) * 1000
        print(f"{n:>6} {capacity:>9} {g_ms:>11.3f} {d_ms:>9.3f} "
              f"{gp:>14.2f} {dp_profit:>10}")


if __name__ == "__main__":
    cap = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    demo(cap)
    benchmark()
