# Analysis Practice
## Introduction
- We want a way to discuss algorithms independently of implementation detail
    - Implementation detail is important, but by having this way of describing algorithms, we are able to take part of the multi-decade conversation

## Cube Problem
- It's impossible to cut the cube into 1x1x1 cubes from 3x3x3
- Why?
    - Any cut I make, will create a 3x3x1
    - Its equivalent to rotating the square and making any other arbitrary cut
- Any stacking or organizing I can do will not reduce the number of cuts
- Ater cutting off one piece, we can just consider the 3x3x2 cube, and treat it as a subproblem where you would need to cut this in <5 cuts
    - You could then stack this cube such that you take the 3x3x1 into account when making the cuts on the larger cube
- Key problem solving technique:
    - What can we ignore here and how to create subproblems?
- Another intuitive way:
    - Imagine the inner 1x1x1 cube
        - It has 6 cuts along it, which gives you a minimum of that many that you need to do

## Notes
- Is it the case that if my RPI is using an algorithm which has a lower running time than your supercomputer, it will perform faster?
    - Yes - at some n (assuming it can handle the size) the RPI will perform better
    - As N -> infinity, constant factors are irrelevant
- Is it possible to fundamentally say that O(1) is always better than O(logn)?
    - Hard to say
    - As a mathematician -> constant time
    - As a systems programmer
        - Log time is basically constant. 40 ops for log(1e12) is trivial
        - Therefore, you need to know the constant factor differentiating these two
            - If the operation is constant but it takes a long time, it may not be preferable to the logn approach which is much faster on a per-op basis, and you expect small n most of the time
            - You'll still be happy that worst case time won't be terrible
- For time analysis
    - We can specify this as operations, instead of time
    - B/c if we're discarding constant factors, the actual performance is bounded by the substrate on which the algorithm is implemented and the cost of each operation to get a real sense of the time taken
        - Considering just operations gets to the root of the issue
- For space analysis
    - You need a unit of space (bytes, stack frames, etc.)

### Complexity Zoo
```python3
def f1(n):
    return n * n
```
- Assumption -> we're assuming each operation takes a constant unit of time
- We're assuming we're not operating over cryptographically large primes
- We don't want to pattern match necessarily, always be clear about your assumptions
    - This is implicit to statically typed programming languages via typing
    - In dynamic languages, this isn't possible b/c all types are created as objects and therefore input can be anything

```python3
def f2(n):
    return sqrt(n)
```
- Depends on:
    - Implementation of square root under the hood
        - You could technically implement binary search for perfect squares
    - Depends on input -> unbounded irrational numbers are generators

```python3
def lin_sqrt(n):
    // for k in 1 to n-1
    // if k * k <= n
    // and (k + 1) * (k + 1) > n
    // return k
```
- Limits:
    - O(n)
    - O(sqrt(n))
- Considerations from a system perspective:
    - This has a branch - hard for a branch predictor to get at
- You'd want to benchmark for small n
    - In an interview, you'd want to explain why you want to benchmark
        
    
```python3
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```
- Limits:
    - Time -> O(n)
        - Counting functions as the measure of operations
            - Primitive operations are going to be the same irrespective of input
    - Space -> O(n)
        - Unit we're counting: Stack frames
            - This always grows the same amount by which you call the function
            - x * <pointer_size>


```python3
def iter_fact(n):
    k = 1
    loop 1,n times:
        k *= n
        n -= 1
    return k
```
- Same time asymptotically
- Assuming that linear is faster b/c of:
    - Fewer function calls, which means fewer allocations to the stack 
- Possibly recursion is as fast b/c of tail call optimization (TCO)
    - Tail calls are when you convert a straightforward iterative problem into recursion
    - This create a factorial function as above, where the recursive call is at the "tail"
        - But you need to pass an accumulator, and the last call needs to just be a call to the function
    - The compiler for some languages (i.e. Lisp) will interpret tail call recursion as the iterative solution, and save on the stack frame overhead
        - Will also use constant space, as the accumulator is overwritten continuously


```python3
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```
- How many nodes at the bottom of the call tree, assuming that same amount of splits made?
    - 2^n
    - There would be 2^n nodes above it as well
- What is the tighter bound than 2^n of the fibonacci sequence?
    - On the fact that it terminates early?
- It is linear in space
    - B/c you go DFS through the call stack, so the space hits the base case, then shrinks all the way to the top
    - Then goes into the next branch
- "Magic Cache" Version
    - Linear Time (assuming cache lookup is low cost)
    - Linear Space


