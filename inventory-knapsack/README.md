# Intelligent Inventory Management Using Knapsack Optimization

A warehouse manager has limited storage capacity and many products, each with a
weight and a profit. This project selects products to **maximize total profit**
without exceeding the capacity, using two approaches:

| Approach | Algorithm | Items splittable? | Time | Space |
|---|---|---|---|---|
| Greedy | Fractional Knapsack | Yes | O(n log n) | O(n) |
| Dynamic Programming | 0/1 Knapsack | No | O(n * W) | O(n * W) |

## Project structure
```
knapsack.py        # both algorithms
main.py            # demo + performance comparison
test_knapsack.py   # unit tests (pytest)
data/products.csv  # sample inventory
```

## How to run
```bash
python main.py          # default capacity = 30
python main.py 40       # custom capacity
pip install pytest && pytest
```

## How it works
- **Fractional (Greedy):** sort by profit/weight ratio, take the best items
  first, and take a fraction of the last item if it doesn't fit.
- **0/1 (DP):** build a table `dp[i][w]` = best profit using first `i` items
  with capacity `w`, then backtrack to find the chosen items.

## Observations
- Greedy is much faster, but its profit is only an *upper bound* for real
  products, because it assumes items can be split.
- DP gives the true optimal answer for whole items, but time and memory grow
  with `n * capacity`.
- Use Greedy for bulk or divisible goods (grain, liquids); use DP for
  indivisible goods (laptops, phones).

Run `python main.py` to see the benchmark table for 10 to 1000 items.
