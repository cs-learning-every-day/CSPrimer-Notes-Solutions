"""
Problem:
    - Medieval town
    - We want to leave all houses included within our wall
    - We want to minimize the amount of wall to be built
    - Essentially, we want to build a convex shape that includes all of the points
- Convex Hull Problem
    - Applied to animal movements
        - They don't move outside of the convex hull of their previous furthest movements
- Applications:
    - By finding the convex hull of a car in a 3d simulation, you can greatly reduce the complexity of your collision detection logic, b/c you only need to verify for collisions against that convex hull
- Brute Force:
    - Current_solution = 0, []
    - Starting from some point A:
        - Enumerate all possible others points in the space, and count the distance between all of them
        - If distance < current_solution AND all points contianed in fence:
            solution = distance
      return list_of_min_distance
- Baseline Polynomial (n**3) solution:
    - Draw a line between any two points:
        - If all other points are on one side of the line:
            - It is part of the convex hull
        - If there are point on both sides of the line:
            - It is not part of the convex hull
    - There are n**2 possible lines
        - And for each line we have to check n points
    - Therefore n**3 performance
- Divide and Conquer Approach:
    - Divide the set of points in half
        - Recurse until you get a trivial convex hull of at most three points
        - Merge each half together 
"""

