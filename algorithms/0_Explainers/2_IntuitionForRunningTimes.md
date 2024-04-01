# Building an inuition for common running times
- Four separate types that determine whether a different running time is material:
    - Constant-ish
        - Perfect
        - No matter how much input, we maintain constant runtime
        - Runtimes: O(1), O(logn)
    - Linear-ish
        - Straightforward
        - We scale proportionally with our input
        - Runtimes: O(n), O(nlogn)
    - Polynomial-ish
        - Doable, maybe tricky
        - With a decent size n, you will need to do some work to make it feasible
            - You may need to invest into creating a data structure that can help you reduce running time
        - Runtimes: O(n^2), O(n^3),...
    - Exponential-ish
        - Impossible
        - So hard that it is impossible for a computer of any size to solve this problem
        - Examples
            - Travelling salesman
        - Can sometimes be approximated with heuristics
        - Runtimes: O(2^n), O(3^n), ...

## Examples
A table that shows the running time of different algorithms for different input sizes:
| Input Size | O(1) | O(log n) | O(n) | O(n log n) | O(n^2) | O(2^n) |
|------------|------|----------|------|------------|--------|--------|
| 10         | 1    | 3        | 10   | 30         | 100    | 1024   |
| 100        | 1    | 6        | 100  | 600        | 10000  | 2^100  |
| 1000       | 1    | 9        | 1000 | 9000       | 1000000| 2^1000 |
| ...        | ...  | ...      | ...  | ...        | ...    | ...    |
| 1,000,000  | 1    | 20       | 1M   | 20M        | 1T     | 2^1M   |

- You can see from the above that there are four clear classes of algorithms
    - O(1) & O(logn) do not diverge massively as the size of input increases
    - When deciding between algorithms of these kinds, constant factors would start to play a role in your decision, let alone ease of implementation
    - Example: Postgres
        - You can pick whether you want a tree or hash based index
        - Until very recently, the tree-based index, despite being log running time to access an index, it was slower to access an index than the hash-based index
            - Asymptotically, its slow b/c its log-based rather than constant time
        - Constant factors in the implementation of the hash index, and the opp to support concurrency in B trees, meant that B trees were preferable

