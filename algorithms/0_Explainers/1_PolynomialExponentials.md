# Enormous difference between polynomial and exponential
- Polynomial -> O(n^2)
    - Reasonable for computers to do
    - n = 10 -> 100 operations
    - n = 20 -> 400 operations
    - n = 30 -> 900 operations
    - n = 40 -> 1600 operations
- Exponential -> O(2^n)
    - Completely unreasonable for computers
    - n = 10 -> 1024 operations
    - n = 20 -> 1,048,576 operations
    - n = 30 -> 1,073,741,824 operations
    - n = 40 -> 1,099,511,627,776 operations


## Implications
- 2^48 are the bits in a pointer in Intel's virtual table address table
- 64 bit IDs are insanely large
- @ n = 300 for exponential time you are far beyond the number of atoms in the universe


