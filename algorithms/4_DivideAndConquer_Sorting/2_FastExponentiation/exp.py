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
    

def fast_exp_iter(a,n):
    """TODO: Implement iteratively"""



if __name__ == "__main__":
    fast_exp(3, 100000)
    print('done')
