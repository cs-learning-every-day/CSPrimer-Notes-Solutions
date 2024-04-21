"""
- You can only get so far with linear structures
    - Lots of data is organized hierarchically
- ps command
    - Retrieves processes running in your os
    - Each process, except for the root process (`/sbin/launchd`) has a parent process id
- We will implement pstree
    - Read the stdin of `ps -o pid,ppid,commm`
"""
import sys
import subprocess
from dataclasses import dataclass
from collections.abc import Sequence
from collections.abc import Iterable
from pprint import pprint


@dataclass
class Process:
    pid: int
    ppid: int | None
    comm: str
    user: str
    children: list['Process']

    def __str__(self):
        return f"{self.pid} {self.user} {self.comm}"

@dataclass
class ProcessTree:
    root: Process



def render_process_tree(process_tree: ProcessTree):
    def _render(node: Process, indent: int):
        base_string = f"|{(indent-1)*2*'-'}"
        if node.children:
            print(f"{base_string}\- {node}")
            for child in node.children:
                _render(child, indent+1)
        else:
            print(f"{base_string}-= {node}")
    _render(process_tree.root, 0)

def convert_stdin_to_processes(stdin: Iterable[str] | None = None) -> list[Process]:
    stdin = stdin or sys.stdin
    return [convert_line_to_process(line) for idx, line in enumerate(stdin) if idx != 0]


def convert_line_to_process(line: str) -> Process:
    line_segments = line.split(maxsplit=3)
    return Process(
        pid=int(line_segments[1]),
        ppid=int(line_segments[2]),
        user=line_segments[0],
        comm=line_segments[3].strip('\n'),
        children=[]
    )


def create_process_tree(processes: list[Process]) -> ProcessTree:
    """
    Understand:
        - We need to be able to create a structure that represents the tree structure of the processes
        - This means that we need to create the structure from what is passed into stdin, and then print it to stdout
        - There is only one root process with PID == 1
        - All other processes are derived from this process
        - As a tree, each process has only one parent

    Plan:
        - Define a Node structure, which specifies:
            - PID
            - PPID
            - COMM
            - Children
        - For each line in the stdin, create a node
            - If there is no existing root node, this new node becomes the root node
                - Continue
            - If the ppid of the new node is the pid of the root node:
                - Add the node as the child of the root node
            - If the PID of the new node is the PPID of the root node:
                - Add the root node to the children of the new node
                - The new node becomes the root node
            - Otherwise, traverse the root node to find the parent of the new node
                - traverse(node) 
                def traverse(node):
                    if node.pid == process.ppid:
                        node.children.append(process)
                        return
                    if not node.children:
                        return
                    for child in node.children:
                        traverse(child)
        - Once structure is created, to a DFS of the node and print each node
            - Retain an understanding of how deep you are, so you know how much to indent the information of that node
    """
    root = None
    i = 0
    while processes:
        try:
            process = processes[i]
        except IndexError:
            i = 0
            continue
        if not root:
            root = process
            processes.pop(i)
        elif process.ppid == root.pid:
            root.children.append(process)
            processes.pop(i)
        elif process.pid == root.ppid:
            process.children.append(root)
            root = process
            processes.pop(i)
        else:
            def traverse(node: Process) -> bool:
                if node.pid == process.ppid:
                    node.children.append(process)
                    return True
                if not node.children:
                    return False
                for child in node.children:
                    result = traverse(child)
                    if result:
                        return result
                return False
            added = traverse(root)
            if added:
                processes.pop(i)
        i += 1
    return ProcessTree(root=root)

def get_process_stdin() -> subprocess.CompletedProcess[bytes]:
    return subprocess.run('ps -e -o user,pid,ppid,comm')


if __name__ == '__main__':
    processes = convert_stdin_to_processes()
    assert len(processes)
    process_tree = create_process_tree(processes)
    assert process_tree.root
    render_process_tree(process_tree)



