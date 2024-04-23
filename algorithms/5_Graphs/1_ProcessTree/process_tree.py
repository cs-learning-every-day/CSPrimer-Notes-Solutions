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
from dataclasses import dataclass
from collections.abc import Iterable


@dataclass
class Process:
    pid: int
    ppid: int | None
    comm: str
    user: str
    children: list["Process"]

    def __str__(self):
        return f"{self.pid} {self.user} {self.comm}"


@dataclass
class ProcessTree:
    root: Process


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
        - Once structure is created, do a DFS of the node and print each node
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
        else:
            parent = find_parent(root, process)
            if parent:
                parent.children.append(process)
                processes.pop(i)
        i += 1
    return ProcessTree(root=root)


def find_parent(node: Process, curr: Process) -> Process | None:
    if node.pid == curr.ppid:
        return node
    if not node.children:
        return None
    for child in node.children:
        result = find_parent(child, curr)
        if result:
            return result


def convert_stdin_to_processes(stdin: Iterable[str] | None = None) -> list[Process]:
    return [convert_line_to_process(line) for idx, line in enumerate(stdin) if idx != 0]


def convert_line_to_process(line: str) -> Process:
    line_segments = line.split(maxsplit=3)
    return Process(
        pid=int(line_segments[1]),
        ppid=int(line_segments[2]),
        user=line_segments[0],
        comm=line_segments[3].strip("\n"),
        children=[],
    )


def render_process_tree(process_tree: ProcessTree):
    def _render(node: Process, indent: int):
        base_string = f"|{(indent-1)*2*'-'}"
        if node.children:
            print(f"{base_string}\- {node}")
            for child in node.children:
                _render(child, indent + 1)
        else:
            print(f"{base_string}-= {node}")

    _render(process_tree.root, 0)


def _traverse_test(node: Process):
    for child in node.children:
        if node.pid != child.ppid:
            print(f"Child {child.pid} is not a child of {node.pid}")
        _traverse_test(child)


if __name__ == "__main__":
    processes = convert_stdin_to_processes(sys.stdin)
    process_tree = create_process_tree(processes)
    render_process_tree(process_tree)
    _traverse_test(process_tree.root)
