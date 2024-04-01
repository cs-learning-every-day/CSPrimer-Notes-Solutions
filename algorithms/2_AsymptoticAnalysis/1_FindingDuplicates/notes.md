# Finding Duplicates
## Intro
- You want to see analysis as a way of speaking theoretically about tradeoffs between approaches that are independent of the system you'er running on
    - In practice: You can't avoid the specifics of the system
    - But if you did this above, you wouldn't be able to speak generally about the running times of algorithms


## Problem: 
- Description
    - Array of integers
    - They may or may not be unique integers
    - We want to write a function that returns whether there is a duplicate in there
- Engineers provide solutions:
    1. Nested loop: For each n in array, check every other n (other than itself) for equality
    2. Sort & search: Sort the array, iterate through checking adjacent pairs
    3. Hashing: Iterate once through, building a hash map / hashset as we go
- Evaluating each approach
    - Nested Loop:
        - Space: O(1)
        - Time: O(n**2)
        - When to use? Ideally never
    - Sort & Search:
        - Space: O(1) if in-place or O(n)
        - Time: O(nlogn) [merge sort] + O(n) -> O(nlogn)
        - When to use? Also if you are low on space
    - Hashing (Favorite):
        - Space: O(n)
        - Time: O(n) 
        - When to use? If you don't care about space considerations and want fastest option


## Solution Notes
- Nested Loop   
    - The enumeration of pairs forms a triangle structure
        - In practice you may only do half of n**2 comparisons
    - But the way that the algorithm grows proportionally to the area of the triangle
        - I.e. via n**2 (polynomial time)
    - Why do we not care about the symmetry?
        - If usage of symmetry is 2x faster:
            - A person with a computer that is 2 units fast using the non-symmetry algo will be as fast as computer that is 1 unit fast using symmetry
        - There is a meaningful difference in terms of immediate performance, but the time to compute the answer will still grow according to the same dynamics
    - Applications  
        - Join algorithms in databases are a lot like this (they compare everything in one table to everything in another table)
- Sort & Search
    - Quicksort & Merge Sort are O(nlogn)
        - This is much closer to O(n) than O(n**2)
        - Consider n = 10**9
            - O(n) = 10**9
            - O(nlogn) = 10**9 * log2(10**9) -> 10**9 * 30 -> 3*10 **10
            - O(n**2) = 10**18
