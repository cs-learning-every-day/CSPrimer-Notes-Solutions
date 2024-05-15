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
from typing import Iterator
import random
import time


def main():
    dim = (6,6)
    start = time.perf_counter()
    starting_point = (0,0) #get_random_starting_point(dim)
    print(f"Starting Point: {starting_point}")
    res = solve(starting_point, dim, end_at_start=False, debug=True)
    end = time.perf_counter()
    print(f"Elapsed: {end-start:.4f}")
    assert len(res) == get_total_squares(dim), res
    print(f"Path: {res}")

    # Test path validity
    for ix,step in enumerate(res):
        if ix != 0:
            assert step in set(get_possible_moves(res[ix-1], dim))

def solve(
    start: tuple[int,int],
    dim: tuple[int, int],
    end_at_start: bool = False,
    debug: bool = False
) -> list[tuple[int, int]]:
    s = [(start, [start])]
    total_squares = get_total_squares(dim)
    it = 0
    while s:
        pos, path = s.pop()
        path_seen = set(path)
        path_length = len(path_seen)
        if not end_at_start and path_length == total_squares:
            return path
        for candidate in get_possible_moves(pos, dim):
            if candidate not in path_seen:
                s.append((candidate, path+[candidate]))
            if path_length == total_squares-1:
                if candidate == start:
                    return path+[candidate]
        if debug:
            it += 1
            if (it % 100000 == 0):
                print(f'{it} Iterations')
                print('Path Length:', path_length)
    return []


@lru_cache()
def is_valid(pos: tuple[int, int], dim: tuple[int,int]) -> bool:
    return all(0 <= i < v for i,v in zip(pos,dim))


def get_total_squares(dimensions: tuple[int, int]) -> int:
    return reduce(lambda x, y: x*y, dimensions)

def get_random_starting_point(dimensions: tuple[int, int]) -> tuple[int,int]:
    return tuple(random.randint(0, x-1) for x in dimensions)

def get_possible_moves(pos: tuple[int,int], dim: tuple[int,int]) -> Iterator[tuple[int,int]]:
    candidates = [
        (pos[0]+2, pos[1]-1),
        (pos[0]+2, pos[1]+1),
        (pos[0]+1, pos[1]-2),
        (pos[0]+1, pos[1]+2),
        (pos[0]-1, pos[1]-2),
        (pos[0]-1, pos[1]+2),
        (pos[0]-2, pos[1]-1),
        (pos[0]-2, pos[1]+1)
    ]
    for c in candidates:
        if is_valid(c, dim):
            yield c

if __name__ == '__main__':
    main()

