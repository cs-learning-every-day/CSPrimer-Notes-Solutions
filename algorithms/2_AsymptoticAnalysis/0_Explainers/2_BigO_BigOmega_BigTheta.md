# Big O, Big Omega, Big Theta
## Big Theta
- Given some function that generally looks linear with noise during small N, how would you characterize it>
    - O(n) out of your gut
- You could also say, if you're happy to declare this function as growing O(n), that it is also limited by O(n log n)
- Technically, if we're happy to say O(n) is the asymptotic characterization that is the asymptotically tightest limit to the actual function
    - Called Big Theta -> θ(N)
- Summary:
    - O(n) >= f(n)
    - θ(N) ~=/= f(n)
- In practice, we use O(n) to mean the lowest limit for the function
    - Why? Its not interesting to talk about a limit that is not the lowest
    - Technically, all O(n_i) where O(n_i) > O(n) are technically also the limit

## Big Omega
- Ω(N)
- The asymptotic lower bound for the function
    - If O(N) == θ(N)
    - Then O(N) == θ(N) == Ω(N)


