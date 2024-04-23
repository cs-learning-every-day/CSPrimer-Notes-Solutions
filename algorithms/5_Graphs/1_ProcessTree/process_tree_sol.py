"""
- Read from stdin
- use first line to determine/validate pid, ppid, etc fields
- for each subsequent line
    - Tokenize by splitting
    - Extract pid, ppid, [etc]
    - Create instance of Process (effectively a tree node) with "children" attribute
    - Recursively check if ppid is pid of any process in our tree
        - If so, add as child
        - Else, add this process to root, aand check if any root process should be parented under this one
- For each process in root:
    - Print that process' info, then recursively run this print routine

Loop:
    echo pstree.py 'ps -a -x -c -o pid,ppid,comm' | python process_tree_sol.py
"""
import sys

class Process:
    def __init__(self, pid, ppid, info):
        self.pid = pid
        self.ppid = ppid
        self.info = info
        self.children = []


def find(node, test):
    if test(node):
        return proc
    for child in node.children: # avoid doing two loops: should be able to formulate the recurrence better
        parent = find(child, test)
        if parent:
            return parent
    return None

def print_tree(processes):
    for p in processes:
        print(p.pid, p.info)
        print_tree(p.children)


if __name__ == "__main__":
    header = sys.stdin.readline().split()
    try:
        pid_idx = header.index("pid")
        ppid_idx = header.index("ppid")
        comm_idx = header.index("comm")
    except ValueError:
        print("usage: ps -o pid,ppid,comm,[etc] | python process_tree_sol.py", file=sys.stderr)
        exit(1)
    # Tokenize process info and group into a tree
    root = []
    for line in sys.stdin:
        parts = line.split()
        pid = parts[pid_idx]
        ppid = parts[ppid_idx]
        info = ' '.join(x for i,x in enumerate(parts) if i != pid_idx and i not in {ppid_idx, pid_idx})
        proc = Process(pid, ppid, info)

        for node in root:
            parent = find(node, lambda x: x.pid == ppid)
            if parent:
                parent.children.append(proc)
                break
        else:
            for i, p in enumerate(root):
                if p.ppid == pid:
                    proc.children.append(p)
                    root.pop(i)
                    break
            root.append(proc)

    # Print tree
    print_tree(root)

