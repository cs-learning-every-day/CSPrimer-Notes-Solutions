import math



def square_root(y: int):
    """
    Understand:
        - Given some integer x, find the value y that is the square root
    Plan:
        - Brute Force (sqrt(n) runtime):
            - For i in range(x):
                if i * i == range(x):
                    break
        - Divide and Conquer (logn)
            hi, lo = y, 0
            while hi > lo:
                m = (hi + lo)/2
                m_pow = m*m
                if m_pow == y:
                    return m
                if m_pow > m:
                    hi = m
                else:
                    lo = m
            return lo

        - Potential problem: Poor branch prediction
            - CPU needs to guess whether candidates are too high or too low
            - Is there a better performance possibilities or do you just let your CPU loop?
            - You can measure branch prediction hit rate in perf
    """
    hi, lo = y, 0
    while hi > lo:
        m = (hi + lo)/2
        m_pow = m*m
        if m_pow == y:
            return m
        if m_pow > y:
            hi = m
        else:
            lo = m
    raise Exception("out of bounds")
    

if __name__ == '__main__':
    x = 132
    res = square_root(x)
    expected = math.sqrt(x)
    try:
        assert res == expected
    except AssertionError:
        print(f"Result: {res}")
        print(f"Expected: {expected}")
