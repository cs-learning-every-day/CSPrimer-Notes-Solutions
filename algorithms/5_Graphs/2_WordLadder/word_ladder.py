"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, changing only one letter at a time, where each transformed word must exist in the word list. Return 0 if there is no such transformation sequence.

Examples:
    - PIG -> STY
        - PIG
        - PIT
        - PAT
        - PAY
        - SAY
        - STY

- Humans are bad at methodical search
    - We tend to pattern matching
        - Which doesn't necessarily lead to the optimal solution
- Systematic Search
    - You don't ever want to go back to a word you've already seen
        - You can get stuck in a loop and it's computationally unnecessary
    - BFS
        - Then once you hit the word on any level, you will find the shortest path

- Consider:
    - This is a graph
        - How you represent this is up to you

Understand:
- We have a set of words
- We need to figure out how many transformations are requierd to get from on x-letter word to another x-letter word
- Therefore, for any given word, we should:
    - Find out how many characters, and limit our search to just those words
- Two strategies for building the graph:
    1. Build the graph on the basis of just the words that exist in the repository
        - I.e. For each letter in the word, mask that letter, and find the relevant words in the repository of words
            - Pop the word from the repository of words
    2. Build the graph by checking every permutation of a given letter and then verifying whether that exists in the repository of owrods
        - If it does, pop the word
- It feels like 1 is more apt, as we avoid having to run 27*n permutations for a n-letter word, if there are none available. 
    - Instead, we can mask the word, and just check m (m being the lenght of the repository). We expect this to decrease with each removal
    - The benefit of 2 is that we can get constant time lookups on the repository, so verification is cheap

Plan:
- Given some word of length n, consider only those words with length n
    - Iterate over length of words and filter out those that are len(x)!=n
- Node:
    word: str
    parent: Node | None
    children: list[Node]
- Generate the graph:
    - Given some word node
    - For each letter in a given word:
        - Mask the letter, then verify whether the unmasked part is equivalent for any other words in teh repository
            - For each match, remove the word from the repository
            - Add the word as a child to the graph with depth+1
    - Iterate over the children, and generate the graph, given the child and the updated repository
- Search the graph with DFS

UPDATED PLAN:
- BFS over the start word
    - Find every permutation of the word and create it as a node with parent to the start word if it is a valid word and has not yet been seen
    - Add the node to the queue
- Once the target word has been found:
    - Return the word ladder by recording each node value between the root and the leaf node
"""

import string
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: str
    parent: Optional["Node"] = None


class WordLadderSolver:
    def __init__(self, words: set[str]):
        self.words = words

    def get_shortest_word_ladder(self, start: str, end: str) -> list[str]:
        if not len(start) == len(end):
            raise ValueError("Start and end word must be of same length")
        start_node = Node(value=start)
        return self._get_shortest_word_ladder(start_node, end, self.words.copy())

    def _get_shortest_word_ladder(
        self, node: Node, target: str, words: set[str]
    ) -> list[str]:
        queue = [node]
        while queue:
            curr = queue.pop(0)
            if curr.value == target:
                return self._create_word_ladder_from_node(curr)
            for index in range(len(curr.value)):
                for letter in string.ascii_lowercase:
                    candidate = self._replace_char_in_string(curr.value, letter, index)
                    if candidate == curr.value or candidate not in words:
                        continue
                    child = Node(value=candidate, parent=curr)
                    queue.append(child)
                    words.remove(candidate)
        else:
            return []

    @classmethod
    def _create_word_ladder_from_node(cls, node: Node) -> list[str]:
        word_ladder = []
        while node is not None:
            word_ladder.insert(0, node.value)
            node = node.parent
        return word_ladder

    @classmethod
    def _replace_char_in_string(cls, s: str, char: str, index: int) -> str:
        return s[:index] + char + s[index + 1 :]

    def is_word_in_dictionary(self, word: str) -> bool:
        return word in self.words


def main(word_ladder_solver: WordLadderSolver):
    TEST_CASES = [
        ("pig", "sty"),
        ("head", "tail"),
        ("four", "five"),
        ("wheat", "bread"),
        ("pen", "ink"),
        ("chin", "nose"),
        ("wet", "dry"),
        ("hare", "soup"),
        ("eye", "lid"),
        ("hare", "soup"),
        ("eel", "pie"),
        ("poor", "rich"),
        ("raven", "miser"),
        ("oat", "rye"),
        ("wood", "tree"),
        ("grass", "green"),
        ("man", "ape"),
        ("cain", "abel"),
        ("flour", "bread"),
    ]
    for case, result in TEST_CASES:
        assert word_ladder_solver.is_word_in_dictionary(
            case
        ), f"{case} not in dictionary"
        assert word_ladder_solver.is_word_in_dictionary(
            result
        ), f"{result} not in dictionary"
        word_ladder = word_ladder_solver.get_shortest_word_ladder(case, result)
        print("-------")
        print(f"{case} -> {result}: {word_ladder}")
        assert len(word_ladder) > 0


if __name__ == "__main__":
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip().lower())

    word_ladder_solver = WordLadderSolver(words=set(words))
    main(word_ladder_solver)
