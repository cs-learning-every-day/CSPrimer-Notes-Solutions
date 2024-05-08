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


class Jug:
    """
    A jug, perched on a fountain, ready for pouring.
    All contents assumed to be in litres.
    """

    def __init__(self, max: int):
        if max <= 0:
            raise ValueError("Please provide a non-negative value for max")
        self.max = max
        self._content = 0

    def __eq__(self, o: "Jug") -> bool:
        if not isinstance(o, self.__class__):
            return False
        return self.max == o.max and self.content == o.content


    def __repr__(self) -> str:
        return f"Jug(content={self._content}, max={self.max})"

    @property
    def content(self) -> int:
        """The current fill of the jug"""
        content = self._content
        if not self.is_valid:
            raise RuntimeError(
                f"current fill must be bounded by 0 and {max}.\n"
                f"current: {content}"
            )
        return content

    def is_valid(self) -> bool:
        return 0 <= self._content <= self.max

    def fill(self, amount: int) -> "Jug":
        """Fills the jug according to some provided amount"""
        self._content = min((self.max, self._content + amount))
        return self

    def pour_out(self, amount: int) -> "Jug":
        self._content -= amount
        return self

    def fill_up(self) -> "Jug":
        """Fills up the jug entirely"""
        self._content = self.max
        return self

    def empty(self) -> "Jug":
        """Empties the Jug of its contents"""
        return self.pour_out(self.content)


class JugFactory:
    @classmethod
    def fill_up(cls, j: Jug) -> Jug:
        nj = Jug(max=j.max)
        nj.fill_up()
        return nj

    @classmethod
    def fill(cls, j: Jug, amount: int) -> Jug:
        nj = Jug(max=j.max)
        nj.fill(amount)
        return nj

    @classmethod
    def empty(cls, j: Jug) -> Jug:
        return Jug(max=j.max)

    @classmethod
    def pour_out(cls, j: Jug, amount: int) -> Jug:
        nj = Jug(max=j.max)
        nj.fill(j.content)
        nj.pour_out(amount)
        return nj

class State:
    def __init__(self, *jugs: Jug):
        self.jugs = jugs

    def __repr__(self) -> str:
        return f"State(jugs={self.jugs})"

    def __hash__(self) -> int:
        return hash((j for j in self.jugs))

    def __eq__(self, o: "State") -> bool:
        if not isinstance(o, self.__class__):
            return False
        return (
            len(self.jugs) == len(o.jugs) and
            all(sj == oj for sj, oj in zip(self.jugs, o.jugs))
        )

    @property
    def is_final(self) -> bool:
        return any(x.content == 4 for x in self.jugs)

    @property
    def is_valid(self) -> bool:
        return all(j.is_valid for j in self.jugs)


def jug_pouring(
    starting_state: State,
) -> list[State] | None:
    queue = [
        (
            starting_state,
            [starting_state]
        )
    ]
    it = 0
    while queue:
        pprint("---------------------------------------------------------")
        pprint(f"Iteration: {it}")
        state, path = queue.pop(0)
        print("State:")
        pprint(state)
        if state.is_final:
            return path
        neighbors = get_neighbors(state)
        print("Neighbors:")
        pprint(neighbors)
        for neighbor in neighbors:
            queue += [(neighbor, path+[neighbor])]
        it += 1
    return None


def fill_jug__leave_jug(fill: Jug, leave: Jug) -> State:
    return State(JugFactory.fill_up(fill), leave)

def order_state(state: State) -> State:
    jugs = state.jugs
    return State(jugs[1], jugs[0])


def empty_jug__leave_jug(empty: Jug, leave: Jug) -> State:
    return State(JugFactory.empty(empty), leave)


def pour_one_jug_into_another(source: Jug, dest: Jug) -> State:
    pour_amount = max(min((
        source.content, dest.max - dest.content
    )), 0)
    return State(JugFactory.pour_out(source, pour_amount), JugFactory.fill(dest, pour_amount))


def get_neighbors(state: State) -> list[State]:
    jugs = state.jugs
    unique_states = set((
        fill_jug__leave_jug(jugs[0], jugs[1]),
        empty_jug__leave_jug(jugs[0], jugs[1]),
        pour_one_jug_into_another(jugs[0], jugs[1]),
        order_state(fill_jug__leave_jug(jugs[1], jugs[0])),
        order_state(empty_jug__leave_jug(jugs[1], jugs[0])),
        order_state(pour_one_jug_into_another(jugs[1], jugs[0])),
    ))
    return [s for s in unique_states if s.is_valid and s != state]


if __name__ == '__main__':
    state = State(Jug(max=3), Jug(max=5))
    pprint(jug_pouring(state))
