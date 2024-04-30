"""
- Problem:
    - Given a three gallon jug and a five gallon jug, measure out exactly four gallons of water.
        - Reformulate this as a graph and then get the answer by searching over it
    - Try to write it such that it can be reformulated as different sizes and numbers of jugs
    - Try to find the minimal number of operations

Understand:
- We have a set of values that represent the amount of water in our jugs:
    - (A, B), where A takes at most 3 gallons, and B at most 5
- We should specify this as a graph, whereby there are the following actions:
    - Pour Y liters of water into a Jug X -> X + Y < MAX_X
    - Pour Y litres of water out of a Jug X -> X - Y > 0
    - Pour Y litres of water out of Jug X into Jug Z -> X - Y > 0 & Z + Y < MAX_Z
- For each state of the jugs, we should consider every possible action taken at each state
    - To find the minimum number of steps, we BFS over this graph

Plan:
- We won't create an explicit graph, instead will build as we go, b/c we can get stuck in cycles
    - You could repeatedly just pour some water into and out of a given jug forever
    - Instead, we will consider via a BFS every action and thereby find the earliest point at which the end-state is found
- queue = [
    (
        (A,B), # State
        [(A,B)] # Path
    )
]
- finished = lambda a,b: any(x == 4 for x in (a,b))
- while queue:
    state, path = queue.pop()
    if finished(state):
        return path
    for neighbor in get_neighbors(state):
        queue.append((
            neighbor,
            path + neighbor
        ))

def get_neighbors(state: tuple[int,int], max_state: tuple[int,int]):
    'Reformulate as just one litre change per step'
    actions = [
        (1, 0),
        (-1, 0),
        (-1, 1),
        (1, -1)
        (0, 1),
        (0, -1)
    ]
    return [
        (s:= (state[0] + a[0], state[1] + a[1]))
        for a in actions
        is_valid(s)
    ]
"""

from collections.abc import Callable


def is_valid(state: tuple[int, int]) -> bool:
    return 0 <= state[0] <= 3 and 0 <= state[1] <= 5


def is_final(state: tuple[int, int]) -> bool:
    return any(x == 4 for x in state)


def jug_pouring(
    starting_state: tuple[int, int],
    is_valid: Callable[[tuple[int, int]], bool]
) -> list[tuple[int, int]] | None:
    queue = [
        (
            starting_state,
            [starting_state]
        )
    ]
    while queue:
        state, path = queue.pop(0)
        if is_final(state):
            return path
        neighbors = get_neighbors(state, is_valid)
        for neighbor in neighbors:
            queue += [(neighbor, path+[neighbor])]
    return None


def get_neighbors(
    state: tuple[int, int], is_valid: Callable[[tuple[int, int]], bool]
) -> list[tuple[int, int]]:
    #ISSUE - We can't measure out in just 1 liter
    actions = [(1, 0), (-1, 0), (-1, 1), (1, -1), (0, 1), (0, -1)]
    candidate_states = ((state[0] + a[0], state[1] + a[1]) for a in actions)
    return list(filter(is_valid, candidate_states))


if __name__ == '__main__':
    print(jug_pouring((0,0), is_valid))
