# Benefits and Limitations of Asymptotic Analysis
- Some people argue that asymptotic analysis is gatekeeping
    - Kind of bullshit
- Pros
    - Benefit of learning this is that you can take part of the multi decade conversation on algorithmic complexity, irrespective of system specifics
    - "Core truth" / essence of an algorithm
- Hazards
    - Constants factors sometimes matter
        - For O(n), half of this can be seriously faster in practice
    - n is often small
    - Complexity classes are quite close to one another in practice
        - O(1) ~ O(logn)
        - O(n) ~ O(nlogn)
        - You should see algorithms as constant-ish, linear-ish, polynomial-ish
    - Maintenance cost
        - Getting some performance benefit may be secondary to making sure this is maintainable
    - You're not always trading off space for time, in fact SPACE IS TIME
        - Often by having something take less time, it will be faster
            - B/c of CPU Caching

