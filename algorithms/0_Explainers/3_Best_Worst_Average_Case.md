# Best, Worst, and Average Case
- We care about the characteristics of the input, not just the size when doing asymptotic analysis
- "Parochial" concerns:
    - Are numbers negative?
    - Is the data sorted?

## Motivating Example: Sort Algorithms
- Bubble Sort
    - Compare each pair of adjacent numbers
        - Swap them if they're out of order
    - Random integers 
        - O(n^2)
    - Sorted integers
        - O(n)
- Merge Sort
    - Consider the array as two arrays
    - Sort both halves and then merge them
    - How to sort a half? Recurse
    - Random Integers:
        - O(nlogn)
    - Sorted Integers:
        - O(nlogn)
- Average Case:
    - Empirical, case-by-case analysis depending on data inputs
    - Not so important for space, more useful for time
