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
    actions = [
        (fill_jug_a, none),
        (empty_jug_a, none),
        (empty_jug_a, fill_contents_into_jug_b),
        (none, fill_jug_b),
        (none, empty_jub_b),
        (fill_contents_into_a, empty_jug_b),
    ]
    return [
        (s:= (state[0] + a[0], state[1] + a[1]))
        for a in actions
        is_valid(s)
    ]
"""

from pprint import pprint
from collections import namedtuple
Jug = namedtuple("Jug", ["content", "max"])


def jug_pouring(
    starting_state: tuple[Jug, Jug]
) -> list[tuple[Jug, Jug]] | None:
    queue = [(starting_state, [starting_state])]
    it = 0
    while queue:
        state, path = queue.pop(0)
        if any(x.content == 4 for x in state):
            return path
        neighbor_states = get_neighbor_states(state)
        for neighbor in neighbor_states:
            queue += [(neighbor, path + [neighbor])]
        it += 1
    return None


def get_neighbor_states(state: tuple[Jug, Jug]) -> list[tuple[Jug, Jug]]:
    return list(set((
        # FILL JUGS
        (fill_jug(state[0]), state[1]),
        (state[0], fill_jug(state[1])),
        # EMPTY JUGS
        (empty_jug(state[0]), state[1]),
        (state[0], empty_jug(state[1])),
        # POUR JUGS
        pour_one_jug_into_another(*state),
        tuple(reversed(pour_one_jug_into_another(state[1], state[0]))),
    )))


def fill_jug(j: Jug) -> Jug:
    return Jug(content=j.max, max=j.max)

def empty_jug(j: Jug) -> Jug:
    return Jug(content=0, max=j.max)

def pour_one_jug_into_another(source: Jug, dest: Jug) -> tuple[Jug, Jug]:
    pour_amount = max(min((source.content, dest.max - dest.content)), 0)
    return (
        Jug(content=source.content - pour_amount, max=source.max),
        Jug(content=dest.content + pour_amount, max=dest.max),
    )


if __name__ == "__main__":
    state = (Jug(content=0, max=3), Jug(content=0, max=5))
    result = jug_pouring(state)
    assert result and len(result) == 7
    print("------------------------")
    print("RESULT:")
    pprint(jug_pouring(state))
