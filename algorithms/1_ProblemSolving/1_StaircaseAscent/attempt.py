"""
Problem:
- Staircase of N Steps
- Legs are long enough to go 1,2,3 steps at a time
- How many different ways can I go up the staircase?

# Polya Method:
## Understand the Problem
- Output
    - Integer of possible permutations of steps you can go up the staircase
- Inputs
    - N Steps
    - A = {a_0, a_1, ... a_m} = {1,2,3}
        - Possible actions
    - T = {t_0, t_1, t_2}
        - Possible number of times you can do an action
- Solve the equation
    - N = AT = a_0 * t_0 + a_1 * t_1 + a_2 * t_2
             = t_0 + 2*t_1 + 3*t_2
    - Find all possible combinations of t_0, t_1 and t_2
- If you had only 1 Option
    - There would only be one way (repeat option 1)

## Devise a Plan
-  Base Case(s):
    - If N == 0 -> Return 0
    - If N == 1 -> Return 1
- Take N and check what is the highest action it is divisible by
    - Then for that number of steps, calculate how many ways to go up it
    - Multiply this number by the number of ways it takes to go up (N - action)
"""

"""
max_action = 0
    for action in sorted(actions, reverse=False):
        if N // action != 0:
            max_action = action
    actions = [action for action in actions if action < max_action]

Possible Cases for 4 Steps:
1. 1,1,1,1
2. 1,1,2
3. 2,1,1
4. 1,2,1
5. 2,2
6. 1,3
7. 3,1



Possible Cases for 3 Steps:
1. 1,1,1
2. 1, 2
3. 2, 1
4. 3
"""
import time

def test_cases():
    #assert staircase_options(0) == 0
    assert staircase_options(1) == 1
    assert staircase_options(2) == 2
    assert staircase_options(3) == 4
    assert staircase_options(4) == 7
    assert staircase_options(5) == 13
    print('ok')


import functools

def memoize(f):
    lookup: dict[tuple, int] = {}
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        cached = lookup.get(args)
        if cached:
            return cached
        result = f(*args)
        lookup[args] = result
        return result
    return wrapper



@memoize
def staircase_options_(
    N: int,
) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 4
    return staircase_options(N-1) + staircase_options(N-2) +  staircase_options(N-3)


def staircase_options(n):
    a,b,c = (1,1,2)
    for _ in range(n):
        a,b,c = b, c, a + b + c
    return a



if __name__ == '__main__':
    test_cases()
    N = 10000

    start = time.perf_counter()
    #result = staircase_options(N, 'test')
    result = staircase_options(N)
    end = time.perf_counter()
    print('----------')
    print(f"N: {N}")
    print(f"Result: {result}")
    print(f"Time: {end - start}")

