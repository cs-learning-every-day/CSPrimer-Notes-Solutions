# Divide and Conquer 
## Intuition Building - 20 Questions
- You have to guess a noun within 20 questions
- If you perfectly bisect the space, you can cover ~1,000,000 nouns
    - There are 80,000 nouns in the english language
        - You should expect to get it in 16 guesses
- Analysis of algorithms
    - Even if you're not bisecting the space completely, you're still doing better than n^2 algorithms
        - I.e. it may take you 40 questions, not 20
        - You still have a log time algorithm to find the noun
- Imagine you ask questions that carve off a quarter of the search space
    - And each time it turns out that its not in the quarter that you ask for, but in the three quarters you didn't ask for
- Quicksort vs Mergesort
    - Mergesort
        - You're always picking pretty much exactly half of the array
        - Then doing n merges 
    - Quicksort
        - The choice of pivot doesn't perfectly bisect the space, but it isn't actually that important
        - B/c even if you're off by a constant factor, you're still firmly in nlogn time
