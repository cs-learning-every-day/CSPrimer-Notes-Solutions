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
"""

import string
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Node:
    value: str
    parent: Optional["Node"] = None
    children: list["Node"] = field(default_factory=lambda: [])


class WordLadderSolver:
    def __init__(self, words: list[str]):
        self.words = words
        self._word_set = set(words)

    def get_shortest_word_ladder(self, start: str, end: str) -> int:
        if not len(start) == len(end):
            raise ValueError("Start and end word must be of same length")
        words = [w for w in self.words if len(w) == len(start)]
        start_node = Node(value=start)
        #self._create_graph(start_node, end, words)
        return self._get_shortest_word_ladder(start_node, end, set(words))

    @classmethod
    def _get_shortest_word_ladder(
        cls, node: Node, target: str, words: set[str]
    ) -> int:
        """
        Between two words, finds the shortest distance. If there is no connecting word
        ladder, return 0
        """
        return cls._get_shortest_word_ladder2(node,target, words)

    @classmethod
    def _get_shortest_word_ladder1(
        cls, node: Node, target: str
    ) -> int:
        """
        Between two words, finds the shortest distance. If there is no connecting word
        ladder, return 0
        """
        queue = [(0, node)]
        while queue:
            level, curr = queue.pop()
            if curr.value == target:
                break
            level += 1
            for child in curr.children:
                queue += [(level, child)]
        else:
            return 0
        return level

    @classmethod
    def _get_shortest_word_ladder2(
        cls, node: Node, target: str, words: set[str]
    ) -> int:
        queue: list[tuple[int, Node]] = [(0, node)]
        while queue:
            level, curr = queue.pop(0)
            if curr.value == target:
                break
            for index in range(len(curr.value)):
                for letter in string.ascii_lowercase:
                    test_string = cls._replace_char_in_string(curr.value, letter, index)
                    if test_string == curr.value or test_string not in words:
                        continue
                    child = Node(value=test_string, parent=node, children=[])
                    curr.children.append(child)
                    words.remove(child.value)
            level += 1
            queue.extend([(level, c) for c in curr.children])
        else:
            return 0
        return level


    def _create_graph(self, node: Node, target: str, words: list[str]) -> None:
        return self._create_graph2(node,target,set(words) - {node.value})

    @classmethod
    def _create_graph1(cls, node: Node, target: str, words: list[str]) -> bool:
        if target not in words or node.value == target:
            return True
        words_to_remove = set()
        for word in words:
            if cls.are_words_one_letter_away(node.value, word):
                child = Node(value=word, parent=node, children=[])
                node.children.append(child)
                words_to_remove.add(word)
        for child in node.children:
            res = cls._create_graph1(child, target, list(set(words) - words_to_remove))
            if res:
                return res
        return False

    def _create_graph2(self, node: Node, target: str, words: set[str]) -> None:
        if not words:
            return
        for index in range(len(node.value)):
            for letter in string.ascii_lowercase:
                test_string = self._replace_char_in_string(node.value, letter, index)
                if test_string == node.value or test_string not in words:
                    continue
                print(test_string)
                child = Node(value=test_string, parent=node, children=[])
                node.children.append(child)
                if test_string == target:
                    return
        for child in node.children:
            self._create_graph2(
                child,
                target,
                words - set(i.value for i in node.children)
            )

    

    @classmethod
    def _replace_char_in_string(cls, s: str, char: str, index: int) -> bool:
        return s[:index] + char + s[index+1:]



    @classmethod
    def are_words_one_letter_away(cls, word_a: str, word_b: str) -> bool:
        if not len(word_a) == len(word_b):
            raise ValueError("Words passed must be of the same length")
        return any(
            cls._get_masked_string(word_a, ix) == cls._get_masked_string(word_b, ix)
            for ix in range(len(word_a))
        )

    @classmethod
    def _get_masked_string(cls, s: str, mask_idx: int) -> str:
        return "".join([v for i, v in enumerate(s) if i != mask_idx])

    def is_word_in_dictionary(self, word: str) -> bool:
        return word in self._word_set


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
        assert word_ladder_solver.is_word_in_dictionary(case), f"{case} not in dictionary"
        assert word_ladder_solver.is_word_in_dictionary(result), f"{result} not in dictionary"
        distance = word_ladder_solver.get_shortest_word_ladder(case, result)
        print("-------")
        print(f"{case} -> {result}: {distance}")
        assert distance > 0


if __name__ == '__main__':
    words = []
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip().lower())

    word_ladder_solver = WordLadderSolver(words=words)
    main(word_ladder_solver)
