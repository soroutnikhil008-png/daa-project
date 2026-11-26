from knapsack import Product, fractional_knapsack, knapsack_01

ITEMS = [Product("A", 10, 60), Product("B", 20, 100), Product("C", 30, 120)]


def test_fractional_classic():
    profit, _ = fractional_knapsack(ITEMS, 50)
    assert round(profit, 2) == 240.0


def test_01_classic():
    profit, chosen = knapsack_01(ITEMS, 50)
    assert profit == 220
    assert sorted(p.name for p in chosen) == ["B", "C"]


def test_greedy_is_upper_bound():
    g, _ = fractional_knapsack(ITEMS, 50)
    d, _ = knapsack_01(ITEMS, 50)
    assert g >= d


def test_capacity_zero():
    assert knapsack_01(ITEMS, 0)[0] == 0
    assert fractional_knapsack(ITEMS, 0)[0] == 0
