import timeit
from typing import Sequence
from matplotlib import pyplot as plt
import random


def binsearch(nums: Sequence[int], n: int):
    lo, hi = 0, len(nums)
    while hi > lo:
        mid = (lo + hi) // 2
        x = nums[mid]
        if x == n:
            return mid
        elif x < n:
            lo = mid + 1
        else:
            hi = mid
    return None


def linearsearch(nums: Sequence[int], n: int) -> int | None:
    for i, x in enumerate(nums):
        if x == n:
            return i
    return None


if __name__ == "__main__":
    LENGTH = 1_000_000_000_000_000
    RANDOM_DATA = {
        10: sorted(random.choices(range(LENGTH), k=10)),
        100: sorted(random.choices(range(LENGTH), k=100)),
        1_000: sorted(random.choices(range(LENGTH), k=1_000)),
        10_000: sorted(random.choices(range(LENGTH), k=10_000)),
        100_000: sorted(random.choices(range(LENGTH), k=100_000)),
        1_000_000: sorted(random.choices(range(LENGTH), k=1_000_00)),
        10_000_000: sorted(random.choices(range(LENGTH), k=10_000_00)),
        100_000_000: sorted(random.choices(range(LENGTH), k=100_000_00))
    }

    LINEAR_SEARCH_TIMES = {}
    BIN_SEARCH_TIMES = {}

    for k, nums in RANDOM_DATA.items():
        n = random.choice(nums)
        LINEAR_SEARCH_TIMES[k] = timeit.timeit(
            lambda: linearsearch(nums, n), number=100
        )
        BIN_SEARCH_TIMES[k] = timeit.timeit(lambda: binsearch(nums, n), number=100)

    from pprint import pprint

    pprint(dict(LINEAR_SEARCH_TIMES))
    pprint(dict(BIN_SEARCH_TIMES))

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    line1 = ax.plot(
        BIN_SEARCH_TIMES.keys(), BIN_SEARCH_TIMES.values(), label="binary", color="blue"
    )
    line2 = ax.plot(
        LINEAR_SEARCH_TIMES.keys(),
        LINEAR_SEARCH_TIMES.values(),
        label="linear",
        color="red",
    )
    ax.set_xscale("log")
    ax.legend(["binary", "linear"])
    ax.set_title("Binary vs Linear Search")
    ax.set_xlabel("Number of Elements (log)")
    ax.set_ylabel("Time (s)")

    plt.show()
