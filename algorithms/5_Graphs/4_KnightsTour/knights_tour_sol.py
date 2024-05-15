"""
- Think of the chessboard as a graph of 64 nodes
- A knight's tour is a path of length 64 with unique vertices
- BFS or DFS?
    - BFS
        - We work level by level
        - Not ideal, because we're going to have to search through dead ends
        - We are forced to search through every single valid path
            - This is computationally infeasible
    - DFS
        - We want to get to the leaves as quickly as possible
        - Naive DFS may still take too long, if we use a heuristic to prioritize moves, we can complete signifiantly faster
            - Warndorf's Rule
                - Always prioritize the move with the fewest subsequent options (i.e. go to the edges of the board)
            - Intuition?
                - You want to prioritize the outside paths to that you leave the flexible inside squares last
""" 


def tour(start=(0,0)):
    """
    Do a DFS of the graph formed by the valid moves of a knight on a standard chessboard.
    Find a path of unique vertices of length 63.

    Prioritize edges which have fewest possible next options

    Model the path as a Python dict, since ordering is maintained,
    and we can use it for O(1) membership testing.
    """
    s = [(start, {start: None})]

    while s:
        current_square, path = s.pop()
        if len(path) == 64:
            return path
        for c in candidates(current, path):
            pass

