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
from dataclasses import dataclass

@dataclass
class Node:
    value: str
    parent: "Node" | None
    children: list["Node"]

class WordDistance:
    def __init__(self, words: list[str]):
        self.words = words

    def get_min_distance(self, start:str , end:str) -> int:
        if not len(start) == len(end):
            raise ValueError("Start and end word must be of same length")
        words = [w for w in self.words if len(w) == len(start)]
        start_node = Node(value=start)
        end_node = Node(value=end)
        self._create_graph(start_node, end_node, words)

    @classmethod
    def _create_graph(cls, node: Node, end_node: Node, words: list[str]) -> None:
        if not words:
            return
        if node.value == end_node.value:
            return
        _words_to_remove: set[str] = {}
        for ix in range(len(node.value)):
            masked_val = cls._get_masked_string(node.value, ix)
            for word in words:
                if cls._get_masked_string(word, ix) == masked_val:
                    node.children.append(Node(
                        value=word, parent=node, children=[]
                    ))
                    _words_to_remove.add(word)
        words = list(set(words) - _words_to_remove)
        for child in node.children:
            cls._create_graph(child, end_node, words)

    @classmethod
    def _get_masked_string(cls, s: string, mask_idx: int) -> string:
        return ''.join([v for i,v in enumerate(s) if i != mask_idx])




def main(word_distance_solver: WordDistance):
    TEST_CASES = [
        ('head','tail'),
        ('pig','sty'),
        ('four','five'),
        ('wheat','bread'),
        ('pen','ink'),
        ('chin','nose'),
        ('tears','smile'),
        ('wet','dry'),
        ('hare','soup'),
        ('pitch','tents'),
        ('eye','lid'),
        ('hare','soup'),
        ('steal','coins'),
        ('eel','pie'),
        ('poor','rich'),
        ('raven','miser'),
        ('oat','rye'),
        ('wood','tree'),
        ('grass','green'),
        ('man','ape'),
        ('cain','abel'),
        ('flour','bread'),
    ]
    for case, result in TEST_CASES:
        distance = word_distance_solver.get_min_distance(case, result)
        print('-------')
        print(f'{case} -> {result}: {distance}')


