"""
- Difficult to do actual optimization in Python b/c the performance overhead comes through the VM itself
- Pointer chasing is detrimental for pointer utilization
"""

import csv
import math
import time
from array import array
from typing import Sequence


def average_age(ages: Sequence[int]) -> float:
    return _average(ages)


def average_payment_amount(payments: Sequence[float]):
    return _average(payments)


def _average(x: Sequence[float] | Sequence[int]) -> float:
    return sum(x) / len(x)


def stddev_payment_amount(payments: Sequence[float], average_payment: float) -> float:
    return math.sqrt(
        sum(_get_squared_diff(p, average_payment) for p in payments) / len(payments)
    )


def _get_squared_diff(x: float, mean: float) -> float:
    diff = x - mean
    return diff * diff


def load_data():
    payments = array("f", [])
    ages = array("H", [])
    with open("users.csv") as f:
        for line in csv.reader(f):
            _, _, age, _, _ = line
            ages.append(int(age))
    with open("payments.csv") as f:
        for line in csv.reader(f):
            amount, _, _ = line
            payments.append(float(amount) / 100)
    return ages, payments


if __name__ == "__main__":
    t = time.perf_counter()
    ages, payments = load_data()
    print(f"Data loading: {time.perf_counter() - t:.3f}s")
    t = time.perf_counter()
    assert abs(average_age(ages) - 59.626) < 0.01
    average_payment = average_payment_amount(payments)
    assert abs(average_payment - 499850.559) < 0.01
    assert abs(stddev_payment_amount(payments, average_payment) - 288684.849) < 0.01
    print(f"Computation {time.perf_counter() - t:.3f}s")
