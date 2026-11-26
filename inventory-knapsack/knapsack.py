"""Core algorithms for the Inventory Management (Knapsack) project."""
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    weight: int
    profit: int


def fractional_knapsack(products, capacity):
    """Greedy approach: pick items by highest profit/weight ratio.
    Items can be split. Time: O(n log n), Space: O(n)."""
    ordered = sorted(products, key=lambda p: p.profit / p.weight, reverse=True)
    total_profit = 0.0
    remaining = capacity
    chosen = []  # (product, fraction taken)
    for p in ordered:
        if remaining <= 0:
            break
        if p.weight <= remaining:
            chosen.append((p, 1.0))
            total_profit += p.profit
            remaining -= p.weight
        else:
            fraction = remaining / p.weight
            chosen.append((p, fraction))
            total_profit += p.profit * fraction
            remaining = 0
    return total_profit, chosen


def knapsack_01(products, capacity):
    """Dynamic Programming: each item is taken fully or not at all.
    Time: O(n * W), Space: O(n * W)."""
    n = len(products)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        p = products[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if p.weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - p.weight] + p.profit)

    # Backtrack to find which items were selected
    chosen = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(products[i - 1])
            w -= products[i - 1].weight
    chosen.reverse()
    return dp[n][capacity], chosen
