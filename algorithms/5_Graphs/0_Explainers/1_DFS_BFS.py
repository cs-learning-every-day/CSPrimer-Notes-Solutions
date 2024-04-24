"""
- Consider the following binary tree:
    {
        'A': {
            'B' : {
                'D': {}, 
                'E': {}
            },
            'C': {
                'F': {},
                'G': {}
            }
        }
    }
- Traversing recursively (DFS):
    - A, B, D, E, C, F, G
    - Going as deep as we can, and then backtracking
    - Feels more natural if you can think recursively
    - Better choice if you're trying to quickly exhaust the tree
        - If your answer is near the leaves, you want to check there
        - Also good for programming languages (you want to evaluate inner pieces of AST before outer)
- Traversing each row at a time (BFS):
    - A, B, C, D, E, F, G
    - There are graph search problems where we care about the minimum distance between things
        - I.e. finding shortest path betwen C & E
    - It's straightforward to figure this out with BFS:
        - Once you hit the highest level one (e.g. C), you just diff C's depth to E's depth
        - Particularly if your graph is too large, or growing
    - Essentially, DFS ensures that you traverse no more of the tree than you need to
"""
tree = [ 'A', [['B', [['D', []], 
                      ['E', []]]],
               ['C', [['F', []],
                      ['G', []]]]]]

def dfs_rec(t):
    data, children = t
    print(data)
    for c in children:
        dfs(c)

def dfs(t):
    """
    Better performance typically:
        - Avoids function overhead
        - Fewer stack frames

    Difference to recursive:
        - We actually add B & C to the stack before going down the C route before we go down B
        - Whereas in the recursive calls we don't even add B to our (call) stack until we're done searching over the C route
    """
    stack = [t]
    while stack:
        data, children = stack.pop()
        print(data)
        for c in reversed(children):
            stack.append(c)

def bfs(t):
    """
    We add the next layer's nodes to the queue for each iteration
    Then pop an entry on the current layer
    """
    queue = [t]
    while queue:
        data, children = queue.pop(0)
        print(data)
        for c in children:
            queue.append(c)




if __name__ == "__main__":
    print("DFS")
    dfs(tree)
    print("BFS")
    bfs(tree)

