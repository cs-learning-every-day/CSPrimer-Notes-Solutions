"""
Problem statement:
    - Find a way to move a knight on a chessboard such that it lands on every square precisely once

Understand:
    - Taking 8x8 chessboard for now (should be able to model such that number of dimensions are irrelevant)
    - Two possible cases to solve:
        - Take the start position as given (i.e. A1, (0,0))
        - Search over the starting position as well
            - Feels like this shouldn't matter since any solution will include every possible starting position
    - Stretch goals:
        - Closed Tour (starts and ends with the same square)
        - Larger / Irregular boards
    - Modelling as a graph search problem:
        - Given some state (x,y), the knight can state transition in 8 ways
            - (x+2, y-1)
            - (x+2, y+1)
            - (x+1, y-2)
            - (x+1, y+2)
            - (x-1, y-2)
            - (x-1, y+2)
            - (x-2, y-1)
            - (x-2, y+1)
        - These states are valid only if:
            - 0 <= x <= x_dim & 0 <= y < y_dim
        - While searching the graph, we need to maintain:
            - Set of visited states
                - Only states that haven't been visited should be considered as candidates
        - DFS or BFS?
            - DFS b/c we're not looking for shortest path, just a path

Plan:
def solve():
    seen = set()
    s = [((0,0), [(0,0)])]
    while s:
        pos, path = s.pop()
        if len(set(path)) == 64:
            return path
        for candidate in get_candidate_squares(pos):
            if is_valid(candidate) and candidate not in seen:
                s.append((candidate, path+candidate))
                seen.add(candidate)



def get_candidate_squares(pos: tuple[int,int]) -> list[tuple[int,int]]:
    return [
        (pos[0]+2, pos[0]-1),
        (pos[0]+2, pos[0]+1),
        (pos[0]+1, pos[0]-2),
        (pos[0]+1, pos[0]+2),
        (pos[0]-1, pos[0]-2),
        (pos[0]-1, pos[0]+2),
        (pos[0]-2, pos[0]-1),
        (pos[0]-2, pos[0]+1)
    ]

"""
from functools import reduce
from functools import lru_cache
import random
import time


def solve(
    start: tuple[int,int],
    dim: tuple[int, int]
) -> list[tuple[int, int]]:
    s = [(start, [start])]
    total_squares = get_total_squares(dim)
    it = 0
    while s:
        pos, path = s.pop()
        path_seen = set(path)
        path_length = len(path_seen)
        if path_length == total_squares:
            return path
        for candidate in get_candidate_squares(pos):
            if not is_valid(candidate, dim):
                continue
            if candidate not in path_seen:
                s.append((candidate, path+[candidate]))
            #elif path_length == total_squares-1 and candidate == start:
            #    return path+[candidate]
        it += 1
        if (it % 1000 == 0):
            print(f'{it} Iterations')
    return []


@lru_cache()
def is_valid(pos: tuple[int, int], dim: tuple[int,int]) -> bool:
    return all(0 <= i < v for i,v in zip(pos,dim))


def get_total_squares(dimensions: tuple[int, int]) -> int:
    return reduce(lambda x, y: x*y, dimensions)

def get_random_starting_point(dimensions: tuple[int, int]) -> tuple[int,int]:
    return tuple(
        random.randint(0, x-1)
        for x in dimensions
    )

@lru_cache()
def get_candidate_squares(pos: tuple[int,int]) -> list[tuple[int,int]]:
    return [
        (pos[0]+2, pos[1]-1),
        (pos[0]+2, pos[1]+1),
        (pos[0]+1, pos[1]-2),
        (pos[0]+1, pos[1]+2),
        (pos[0]-1, pos[1]-2),
        (pos[0]-1, pos[1]+2),
        (pos[0]-2, pos[1]-1),
        (pos[0]-2, pos[1]+1)
    ]


if __name__ == '__main__':
    dim = (5,5)
    start = time.perf_counter()
    starting_point = get_random_starting_point(dim)
    res = solve(
        starting_point, dim
    )
    end = time.perf_counter()
    print(starting_point)
    print(f"Elapsed: {end-start:.4f}")
    assert res

    for ix,step in enumerate(res):
        if ix == 0:
            continue
        assert step in set(
            x for x in get_candidate_squares(res[ix-1])
            if is_valid(x, dim)
        )
