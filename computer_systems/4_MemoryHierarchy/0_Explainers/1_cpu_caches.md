# Understanding CPU Caches
## Motivation
- Being aware of how CPU Caches work and how to lay out your programs has a major impact on performance
- How computers have changed over time
    - CPU Clock speeds have increased a lot
        - From 100 ns in 1990 to 1ns per op today
    - RAM Latency has not decreased significantly
    - Comparable amount of time to retrieve data over time
        - Compute has gotten much much faster
- If we did not have CPU Caches
    - Most time would be spent retrieving data
        - This became unacceptable in the late 90s b/c of the disparity b/w compute and retrieval time
## Example: Adding together integers in an array
- `num = [ ... ]`
- Algorithm
    ```
    total = 0
    for n in nums:
        total += n
    return total
    ```
- What does disassembly look like? (particularly O(n) stuff)
    - We have conditional branch instruction
        - Are we at the end of an array
    - May need to increment instruction
    - Mov instruction (getting data into register from RAM)
    - An add instruction
        - General expectation -> You spent 25% of loop adding
- Assume 4GHZ Processor
    - 4GHZ -> 4 Billion Hertz (times / second) 
    - 0.25ns / Op
- We can assume every operation above therefore takes:
    - Branch -> 0.25ns (assuming good branch prediction)
    - Inc -> 0.25ns
    - Mov -> 100ns (w/o CPU cache)
    - add -> 0.25ns
-  Suppose 64 Byte Cache Lines
    - 16 ints per cache line (4 Byte Integers)
    - Assuming a compiled language, where arrays are layed out in contiguous areas of memory
    - Everytime we get a cache miss, a new cache line (next 64 bytes) will be pulled into cache
        - We're going to get 15 hits per miss
- What improvement are we going to get?
    - L1 Cache Latency: 4 Cycles -> 1ns
    - Cost of looking up 16 integers:
        - (100 (miss) + 15 * 1 (cache hits)) / 16 =~ 7 ns
- It's likely that data you just accessed will be accessed again
    - Common access patterns
        - Sequential iteration
        - Alternating between data
- There is no API to the CPU Cache -> this happens under the hood

## Implications
### Use smaller data types
- If you use smaller ints (16 bit), you would get 35:1 hits:miss ratio 
- Therefore -> a lot of the time, space is time
    - If something is smaller, it fits into Cache better, therefore you get quicker retrieval
    - Principle applies over the entire memory hierarchy
        - Even if you extend this to DRAM, Disk, Network, etc.
            - It is faster to retrieve something in RAM than from Disk

### Reduce Spacing
- Example
    - User struct (age, name, address)
    - You can look up an array of users in constant time in compiled language
        - As struct is nicely laid out in memory
    - What if you want to iterate over and retrieve the `age` value (32 bit integer)?
        - The cache line is populated with all of the User information
    - If you had a bunch of ages together, you would get good cache utilization on retrieving age values
- Array of Structs vs. Struct of Arrays problem
    - Array of Structs: `list[User]`
    - Struct of Arrays: User Data
        - ```UserData {
                ages: list[int],
                names: list[str]
            }```
        - Better cache utilization
        - Useful if you're looking at aggregates 
- Analog Problem in Databases:
    - Aggregation queries over databases motivate columnar storage of data
    - B/c we want a lot of a given thing (i.e. age)
        - When going to disk, and we retrieve one block from disk, that block (4K) is going to be populated with as many ages as possible

### Avoid Pointer Chasing
```
class Address:
    street: str

class User:
    ...
    address: Address
```
- Everytime you dereference a pointer
    - You end up at a different space in memory
    - Will what you're dereferencing in a cache line you've already pulled into Cache?
        - Unlikely
- In non-compiled languages
    - Arrays are not laid out contiguously in memory
        - b/c arrays contain whatever types they like, i.e. `d = [1, "foo", [], ... ]`
        - Therefore, its implemented as an array of pointers (64 bits)
            - You get constant time indexing this way
        - Implication for CPU Caches?
            - Worse cache utilization on python lists vs. C/Go/Rust arrays
            - 7 cache hits for every cache miss
                - But when you do get a cache hit, you need to follow the resulting pointer
                - This is likely not in a cache line you've already pulled
        - Python has an optimization
            - Pre-construct small numbers for you, but not large numbers (< 256)
                - So that you're constantly and destructing small numbers that are in frequent use
            - You get good cache utilization for these
    - Main reason that Python and dynamic languages are slow
        - Data structures are heterogeneous, and use pointers as the data retrieval interface
            - Destroys your cache utilization
        - One of the main reasons to use numpy is that it has better cache utilization

### Linked Lists can be expensive
- There are a lot of situations where in algorithms two situations seem viable
    - Same asymptotic runtime
    - But one has much better cache utilization than the other
- Hash Map collision resolution
    - Chaining -> Using a linked list to provide a pointer to the value that would have collieded
    - Open addressing -> Putting the colliding value somehwere nearby in memory
- Naively using linked lists 
    - End up in a situation where you are constantly pointer chasing
    - Unless you make sure to pre-allocate the data
- Linked lists were more popular in the 90s


