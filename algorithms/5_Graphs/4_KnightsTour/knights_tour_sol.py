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
BOARD_SIZE = 5
DELTAS = (
    (-2, -1),
    (-2,  1),
    ( 2, -1),
    ( 2,  1),
    (-1, -2),
    (-1,  2),
    ( 1, -2),
    ( 1,  2),
)


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
        current, path = s.pop()
        if len(path) == BOARD_SIZE**2:
            return path
        candidates = find_next(current, path)
        candidates.sort(
            key=lambda c: len(find_next(c,path)), reverse=True
        )
        for c in candidates:
            next_path = path.copy()
            next_path[c] = None
            s.append((c, next_path))


def find_next(current, path):
    """
    Given the current position and path so far, return a list of possible next steps.

    TODO Prioritize edges which have fewest possible options.

    Return those in reverse order, for convenience of pushing to stack
    """
    out = []
    for dx, dy in DELTAS:
        cx, cy = current[0] + dx, current[1] + dy
        if 0 <= cx < BOARD_SIZE and 0 <= cy < BOARD_SIZE and (cx,cy) not in path:
            out.append((cx, cy))
    return out


if __name__ == '__main__':
    



