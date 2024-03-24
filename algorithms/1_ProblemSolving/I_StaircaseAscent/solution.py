"""
- Analogous problem
    - Number of unique substrings adding up to n
- Auxiliary Problem
    - How would you go up 1 or 2 steps at a time
- Think inductively
    - Do our examples fit together in a general pattern?
    - What is the relationship between a small and larger problem?
    - Enumerating N =0, N=1, N=2, N=3 etc

# Understand the problem
- Find a function F(n) where n >= 0
- Returns a set of actions x where x >= 0
- Is this a solvable problem?
    - If there is a finite number of steps, it should be countable to figure out number of steps

# Devise a Plan
- Solve for something easier (actions == 2) --> g(n)
    - Essentially boils down to the fibonacci sequence

"""


def f(n):
    a,b,c = (1,1,2)
    for _ in range(n):
        a,b,c = b, c, a + b + c
    return a




