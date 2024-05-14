# Weighted Graph Algorithms
- Most interesting graphs tend to have weights
    - E.g. maps -> we need to take into account the length of roads (i.e. edges) to find the shortest path
- Basic BFS/DFS is not taking into account the weights of the edges
    - You optimize for fewest number of vertices visited, the cost of travelling to each vertex is assumed to be equivalent

## Dijkstra's Algorithm
- Motivating Example: Local Area Network
    - You have a number of routers
        - Connected to one another, and other autonomous systems (i.e. one ISP connected to another ISP)
    - Within a given autonomous system, we'd like to find one of the shortest paths from one of the nodes to an exit node
        - With BFS -> this would give us the lowest number of hops
        - Treating it as a weighted graph makes sure that we are truly looking for the quickest way
- General Explanation (Pathfinding from A -> B)
    - Graph search, but you use a priority queue
        - Priority queue returns the node that represents the shortest cumulative distance so far
    - Consider following:
                     ------(20)----> D ---------(30)----------
                    /                                         \
        - A -(5)-> B -(6)-> E -(4)-> F -(2)-> G -(3)-> H -(5)-> I
           \              /
            -(4)-> C -(9)-
        - You would BFS over this, but the queue selects the values with lowest cumulative distance:
            - Step 1: [(C,4), (B,5)]
            - Step 2: [(B,5), (E,13)]
            - Step 3: [(E,13), (D,25)]
            - Step 4: [(F,17), (D,25)]
            - Step 5: [(G,19), (D,25)]
            - Step 6: [(H,22), (D,25)]
            - Step 7: [(D,25), (I,27)]
            - Step 8: [(I,27), (I,55)]
            - Step 9: DONE -> (I,27)
        - This should always get us to the destination via the shortest path
- Also known as uniform cost search

## A*
- Downside of Dijkstra's Algorithm  
    - You're not using any of your knowledge of where the desintation might be
    - We are guarantee to find the shortest path, but we will have searched paths that are not optimal
- Optimization
    - Include our approximation of what the total remaining cost might be
        - Minimize the function `f(n) = g(n) + h(n)`
            - g(n) -> Cumulative incurred cost
            - h(n) -> Heuristic for approximation remaining cost
    - Possible heuristics
        - Euclidean distance  (as the crow flies - straight line)
            - sum((x[i] - y[i])**2 for i in len(x))**0.5
        - Manhattan Distance (taxicab geometry)
            - sum(abs(x[i] - y[i]) for i in len(x))
        - Other sophisticated heuristic function
            - But it should not be so intensive to compute that it takes orders of magnitude longer than simpler heuristics
        - We need an "admissible heuristic function"
            - This will ensure that we're not searching parts of the graph that are further away from our goal
- Theoretically as good as you can do
- Can be memory hungry
    - In Google Maps they will preprocess the graph to make this viable
- Advantage of ignoring the heuristic funciton
    - You get the shortest path of the starting node to every other node
- A-star is useful if you just care about one destination
    - Intuition, if your starting point and destination is dynamic (map path finding)
        - If your starting point and distance to other nodes is static, then you'd just want to find shortest paths to all nodes (i.e. in the autonomous system case)
- Optimistic vs. Pessimistic heuristic
    - Optimistic -> Our heuristic is underestimating the cost 
    - Pessimistic -> Our heuristic is overestimating the cost
- Dijkstra is A-star without a heuristic function
- [A* Explainer](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

