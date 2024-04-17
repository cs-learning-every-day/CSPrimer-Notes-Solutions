"""
exp(a, n) -> a * a * a * ... * a (n times)
less than complexity O(n)

Understand:
    - Naive implementation:
            - Iterate over the range of exponents and multiply the value by itself- Return
    - Divide and Conquer:
            - splitting the problem up in two until you get to a sub set that you can assemble to get to your answer

Plan:
- if n == 0:
    return 1
- if n == 1:
    return a
- m = a // 2
- x = n - m if 2*m != n else m
- return f(a, m) * f(a, n)
"""


def fast_exp(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * fast_exp(a,n-1)
    res = fast_exp(a, n // 2)
    return res * res
    

def fast_exp_iter_sol(a, n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= a
            n -= 1
        else:
            a *= a
            n //= 2
    return res






def fast_exp_iter(a,n):
    """TODO: Implement iteratively
    - We want to implement iteratively to avoid:
        - Function calling overhead
        - Stack depth (there's a limited number of stack frames we can use)
        - In practice:
            - This isn't actually a problem for us, b/c even to the power of a billion will take ~30 ops
        - In theory:
            - Could be a problem in security and number theoretic applications, where you might have insane exponents

    Understand:
        - What do we need to iterate over?
            - If we iterate over length of n -> O(n)
        - We need an iterative divide and conquer approach
            - I.e. we need to reduce the size of the problem each time
        - Start from the base case, iteratively run the same logic but in reverse
            - We can't square our accumulator as we go
            - We'll square the power as we go
                - 3 ** 8 = (3 ** 2) ** 4

    Plan:
        - if n == 0:
            retrun 1
        - if n == 1:
            return a
        - acc = a * a
        - power = 2
        - while power <= n:
            acc *= acc
            power *= 2
        - if power == n:
            return acc
        - while power > n:
            acc /= a
            power -= 1
          return acc


    """
    if n == 0:
        return 1
    if n == 1:
        return a
    acc = a * a
    power = 2
    while power <= n:
        acc *= acc
        power *= 2
    while power > n:
        acc //= a
        power -= 1
    return acc



if __name__ == "__main__":
    TEST_CASES = [
        (3, 1000),
        (4, 1022)
    ]
    for a, n in TEST_CASES:
        assert fast_exp(a, n) == a ** n
        assert fast_exp_iter(a, n) == a ** n
        assert fast_exp_iter_sol(a, n) == a ** n
    print('done')
