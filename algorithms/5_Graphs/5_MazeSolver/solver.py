"""
- You're programming an AI to do a search of the maze
- With A* you can find the optimal path quickly
- Optimal path:
    - Minimizes some cost
- Think of some hierarchy of costs for the different fields:
    - ' ' -> Low Cost (1)
    - '.' -> Medium Cost (3)
    - '#' -> High Cost (10)
- If you can make it run quickly on large you're doing well
- What is a step? Perhaps parametrizable
    - Any 8 directions including diagonals
    - Or 4 directions
- Easy to find out what the neighbors are
- Weights are encoded in the ascii characters


Understand:
    - We get a text file that encodes the map
    - We load the map as a file and encode it as a matrix
    - As you parse the file into the matrix, remember the position of the X and O
    - Alternative:
        - Create a lookup table for looking up particular coordinates to see what type they are
        - Not sure if this is better, we should still get "theoretical" constant time lookups with a matrix
    - Dijkstra:
        - BFS with Priority Queue, minimized total cumulative cost
    - A*:
        - Dijkstra, also minimizing value of heuristic indicating total estimated cost -> f(n) = g(n) + h(n)

Plan (Text):
- Read the map into a data structure
- Create the priority queue (just a normal queue)
    - Place the start point on the queue
- While the queue is not empty:
    - Sort the queue according to the cost of each value
    - Pop the best value off of the queue
    - If you've reached the end, return!
    - Generate the set of valid neighbor coordinates
        - In 8 Directions where no step exceeds the bounds
    - For each neighbour, add them to the queue with their cost, plus the path they would imply
        - Cost Function: minimize -> x.cumulative_cost + euclidean_distance(end_coord - x.coord)
"""

import enum
from dataclasses import dataclass
from pprint import pprint
import typing as t
import sys

FILE = "maze-solver/small.txt"

POSSIBLE_MOVES = [
    (1, -1),
    (1, 0),
    (1, 1),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]

@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

Path = t.NewType('Path',list[tuple[Coordinate, float]])

@dataclass
class Map:
    start: Coordinate
    end: Coordinate
    dimensions: tuple[int, int]
    values: list[str]

    def get_coordinate_value(self, coordinate: Coordinate) -> str:
        return self.values[coordinate.y][coordinate.x]

    def has_coordinate(self, coordinate: Coordinate) -> bool:
        return (
            0 <= coordinate.x < self.dimensions[0]
            and 0 <= coordinate.y < self.dimensions[1]
        )

    def render_path(self, path: Path) -> None:
        temp_values = self.values.copy()
        for c,_ in path:
            temp_values[c.y] = temp_values[c.y][:c.x] + "Z" + temp_values[c.y][c.x+1:]
        print(f"Total Cost: {path[-1][-1]}")
        for values in temp_values:
            print(values)



@dataclass
class Position:
    coordinate: Coordinate
    cost: float
    path: Path



def main():
    map = load_map(sys.argv[1])
    path = solve(map)
    map.render_path(path)

def load_map(file) -> Map:
    values = []
    x_dim = 0
    y_dim = 0
    start = None
    end = None
    with open(file, "r") as f:
        while f.readable():
            row = f.readline().strip('\n')
            if row == '':
                break
            if x_dim == 0:
                x_dim = len(row)
            for i, x in enumerate(row):
                if x == "O":
                    start = Coordinate(x=i, y=y_dim)
                elif x == "X":
                    end = Coordinate(x=i, y=y_dim)
            values.append(row)
            y_dim += 1
    if not start or not end:
        raise ValueError("Could not find start or end")
    return Map(
        start=start, end=end, dimensions=(x_dim, y_dim), values=values
    )

def solve(map: Map) -> Path:
    queue: list[Position] = [
        Position(map.start, 0, Path([(map.start, 0)])),
    ]
    total_cost = {map.start: 0.}

    while queue:
        queue = sorted(queue, key=lambda position: position.cost, reverse=False)
        position = queue.pop(0)
        if position.coordinate == map.end:
            return position.path
        for neighbor in get_neighbors(position.coordinate, map):
            cost = compute_cost(neighbor, position.path, map)
            if neighbor not in total_cost or cost < total_cost[neighbor]:
                queue.append(
                    Position(
                        coordinate=neighbor,
                        cost=cost,
                        path=Path(position.path + [(neighbor, cost)])
                    )
                )
                total_cost[neighbor] = cost


    return Path([])


def get_neighbors(
    coordinate: Coordinate, map: Map
) -> t.Iterable[Coordinate]:
    return list(
        coord for coord in  
        (Coordinate(coordinate.x + x, coordinate.y + y) for x,y in POSSIBLE_MOVES)
        if map.has_coordinate(coord)
    )

def compute_cost(
    coordinate: Coordinate, path: Path, map: Map
) -> float:
    coordinate_value = map.get_coordinate_value(coordinate)
    coordinate_cost = _get_square_cost(coordinate_value)
    _, last_cost = path[-1]
    return coordinate_cost + last_cost + distance(coordinate, map.end) * 0

def _get_square_cost(value: str) -> int:
    if value == "#":
        return 10
    if value == ".":
        return 3
    if value == " ":
        return 1
    if value == "X":
        return 0
    if value == "O":
        return 100
    raise ValueError(
        f"Provided square value must be in ('#', '.', ' ')\n" f"Provided value: {value}"
    )

def distance(start: Coordinate, end: Coordinate) -> float:
    return _manhattan_distance(start, end)

def _manhattan_distance(start: Coordinate, end: Coordinate) -> float:
    return abs(start.x - end.x) + abs(start.y - end.y)


if __name__ == '__main__':
    main()
