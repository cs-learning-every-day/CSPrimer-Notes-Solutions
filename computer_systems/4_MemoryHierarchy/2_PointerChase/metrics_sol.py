"""
What might jump out to most people:
    - Reducing superfluous casts (i.e casting dollars and cents to floats on each iteration of the loops)
    - Passing the mean value to stddev function directly instead of recomputing
- This exercise will show -> obvious things aren't necessarily most impactful
    - Replacing the superfluous casts cuts off maybe up to 5%
- Pointer Chasing
    - Our User object has payments attributes that is a list of pointers
    - By retrieving these values as pointers, we are almost guaranteed to have poor cache utilization, b/c they will likely be stored at different places in memory
        - Whether these pointers happen to be close to another depends on when they were malloc'ed (i.e. when they were allocated)
        - We're churning our caches quickly b/c most lookups will be misses
    - Point us towards -> put values we care about close together
- How to improve:
    - Reduce pointer jumps (i.e. move `dollars` and `cents` to live on `Payment`)
        - Avoids additional pointer lookups
    - Remove unnecessary fields
        - Brings data closer together in memory, so it is more likely to fit in cache line
"""


import csv
import math
import time



class Payment(object):
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents


class User(object):
    def __init__(self, user_id,  age, payments):
        self.user_id = user_id
        self.age = age
        self.payments = payments


def average_age(ages):
    return sum(ages) / len(ages)


def average_payment_amount(payments):
    return (
        sum(dollars + cents / 100 for dollars, cents in payments)
        / len(payments)
    )


def stddev_payment_amount(payments):
    mean = average_payment_amount(payments)
    squared_diffs = 0
    for dollars, cents in payments:
        amount = dollars + cents / 100
        diff = amount - mean
        squared_diffs += diff * diff
    return math.sqrt(squared_diffs / len(payments))


def load_data():
    ages = [] 
    payments = []
    with open('users.csv') as f:
        for line in csv.reader(f):
            _, _, age, _, _ = line
            ages.append(int(age))
    with open('payments.csv') as f:
        for line in csv.reader(f):
            amount, _, _ = line
            payment = (
                float(int(amount)//100),
                float(amount) % 100
            )
            payments.append(payment)
    return ages, payments


if __name__ == '__main__':
    t = time.perf_counter()
    ages, payments = load_data()
    print(f'Data loading: {time.perf_counter() - t:.3f}s')
    t = time.perf_counter()
    assert abs(average_age(ages) - 59.626) < 0.01
    assert abs(stddev_payment_amount(payments) - 288684.849) < 0.01
    assert abs(average_payment_amount(payments) - 499850.559) < 0.01
    print(f'Computation {time.perf_counter() - t:.3f}s')
