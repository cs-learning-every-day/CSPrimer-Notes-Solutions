"""
strategy
- Do Dijkstra's over small.txt
- Switch to A* (maybe suboptimally, e.g. how we store the path of what's visited)
- refactor
- maybe: animate
"""
import heapq
import math

def print_maze(M, path=None):
    MM = [list(line) for line in M]
    for i, j in path:
        MM[i][j] = '*'
    print()
    print('\n'.join(''.join(line) for line in MM))

COSTS = dict(zip('#. X',(10,3,1,0)))

def solve(M, start, end):
    pq = [(0, 0, start, [start])]
    visited = {start}
    
    while pq:
        _, cost, node, path = heapq.heappop(pq)
        if node == end:
            return path 
        print_maze(M,path)
        visited.add(node)
        for i, j in get_neighbors(M, node):
            if (i,j) in visited:
                continue
            new_cost = cost + COSTS[M[i][j]]
            heapq.heappush(pq, (
                new_cost + heuristic((i,j), end),
                new_cost,
                (i,j),
                path + [(i,j)]
            ))
    return None

def heuristic(start, end):
    i,j = start
    ii, jj = end
    return math.sqrt((i - ii) **2 + (j -jj)**2)

DELTAS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def get_neighbors(M, node):
    i, j = node
    out = set()
    for di, dj in DELTAS:
        ii, jj = i + di, j + dj
        if 0 <= ii < len(M) and 0 <= jj < len(M[0]):
            out.add((ii,jj))
    return out

if __name__ == '__main__':
    with open('maze-solver/small.txt', 'r') as f:
        M = f.read().splitlines()
    strat, end = None, None
    for i, row in enumerate(M):
        for j, x in enumerate(row):
            if x == 'O':
                start = (i, j)
            elif x == 'X':
                end = (i,j)
    path = solve(M, start, end)
    print_maze(M, path)



