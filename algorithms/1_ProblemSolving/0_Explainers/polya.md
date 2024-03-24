# What a programmer can learn from Polya
## Polya Structure
1. Understand the problem
2. Devise a plan
3. Implement the plan
4. Reflect / revise

## How it's relevant
- If you do 1 & 2 well, you should be able to basically delegate 3
- People tend to overindex on element 3 for skill acquisition
- 4 encompasses refactoring and retrospectives

## How to apply to programming
- Understand the problem
    - What do the stakeholders need
    - What is the input / output API
    - What are the intended side effects
    - What are the inputs and outputs
- Devise a plan
    - Polya's heuristics (tools)
        - Draw a figure/diagram
        - Be systematic
            - Example: When thinking of possible inputs/outputs
                - Start from the beginning and go up
                - Problem that SWEs have is that they take random sample of possible inputs, not looking at boundaries
        - Is this similar to another problem I know?
            - From NP Hard problems we know that problems that look quite dissimilar can be expressed as part of each other
            - Postgres algorithm for sorting data that doesn't fit into memory is adapted from a Knuth algorithm for tape sorting
                - https://github.com/postgres/postgres/blob/2673ebf49acfd83b09c777ced8f21eacd27b51ce/src/backend/utils/sort/tuplesort.c#L14-L29
                - They were able to reformulate their out-of-memory sort problem as sorting tape
        - Induction
            - Can we generalize from specific cases?
        - Decomposing/Recomposing
        - Solve an easier (auxiliary) problem
        - Definition
            - Give names to things, give them formal definitions
        - Work backwards from the solution


