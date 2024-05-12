"""
Notes:
    - Model problem as set of finite states (a,b) representing how much in 3 & 5 gallon jugs, respectively
    - Starting state: (0,0)
    - Goal State: (x,4) for any x
    - State transitions:
        - empty left  : (a,b) -> (0,b)
        - empty right : (a,b) -> (a,0)
        - fill left   : (a,b) -> (3,b)
        - fill right  : (a,b) -> (a,5)
        - transfer LR : (a,b) -> (max(0, a+b-5), min(5, a+b))
        - transfer RL : (a,b) -> (min(3, a+b), max(0, a+b-3))
    - Do BFS, build graph as we go
    - No need to revisit nodes we've visited already
"""
from collections import deque

def solve(left, right, goal):
    q = deque()
    q.append(((0, 0), []))
    visited = set()
    while q:
        (a,b), ops = q.popleft()
        if a == goal or b == goal:
            return ops
        candidates = (
            ((0,b) , 'empty left'), 
            ((a, 0), 'empty right'),
            ((left,b), 'fill left'),
            ((a, right), 'fill right'),
            (
                (max(0, a+b-right), min(right, a+b)),
                'transfer L->R'
            ), 
            (
                (min(left, a+b), max(0, a+b-left)),
                'transfer L<-R'
            )
        )
        for c, op in candidates:
            if c not in visited:
                q.append((c, ops + [f'{op}\t{c}']))
                visited.add(c)
    return -1

if __name__ == "__main__":
    print('\n'.join(solve(3, 5, 4)))
