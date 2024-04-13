import abc
from dataclasses import dataclass
from typing import TypeVar
from typing import Generic
from typing import Optional

T = TypeVar('T')


class Deque(Generic[T], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def push_front(self, o: T) -> None:
        pass

    @abc.abstractmethod
    def push_back(self, o: T) -> None:
        pass

    @abc.abstractmethod
    def pop_front(self) -> T:
        pass

    @abc.abstractmethod
    def pop_back(self) -> T:
        pass

    @abc.abstractmethod
    def back(self) -> T:
        pass

    @abc.abstractmethod
    def front(self) -> T:
        pass


"""
Plan:
- Linkedlist should wrap values in Nodes
- These nodes will link to one another as they are added

Node:
  val: T
  next: Node
  prev: Node


Push Front:
    - Accepts some generic T
    - Wrap this in a node wrapper
    - If there is a head node:
        - make this new node the head node
        - Point the "next" attribute of the new node to the head node
        - Point the "prev" attribute of the head node to the new node
    - If there is no head node and no tail node:
        - Set this to be both the head and tail node, no prev or next

Pop Front:
    - If there is no head:
        - Raise error
    - If there is no tail:
        - Raise InvalidDequeState
    - If there is a head:
        - Set the node set to next to the head from the current head
        - Remove the previous link from the existing head
        - Return the previous head

Push Back:
    - If there is a tail:
        - create the new node, and set the previous to the old tail
        - set the next of the old tail to the new node
        - set the current tail to be the new node
    - else if there is a head:
        - raise InvalidState
    - else:
        - Set the new node with no previous and current to be equal to both head and tail

Pop Back:
    - If there is no tail:
        Raise ValueError
    - else if there is no head:
        Raise invalid state error
    - Else:
        - Get reference to tail and the node before the tail
        - Set the next reference of the new tail to None
        - Return the value in the old tail

"""


@dataclass
class Node(Generic[T]):
    val: T
    next: Optional["Node"]
    prev: Optional["Node"]

class InvalidDequeState(Exception):
    pass


class LLDeque(Deque[T]):
    def __init__(self, node: Node | None = None):
        self.head = node
        self.tail = node


    def push_front(self, o: T) -> None:
        if self.head:
            node = Node(val=o,next=self.head,prev=None)
            self.head.prev = node
            self.head = node
        elif not self.tail:
            self.head = self.tail = Node(val=o,next=None,prev=None)
        else:
            raise InvalidDequeState("Only one of head and or tail are defined")

    def pop_front(self) -> T:
        if not self.head:
            raise ValueError('Cannot pop from front of Deque, as there is no head')
        if not self.tail:
            raise InvalidDequeState("Tail not defined when head is set")
        return_node = self.head
        self.head = return_node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = self.head
        return_node.next = None
        return return_node.val

    def push_back(self, o: T) -> None:
        if self.tail:
            node = Node(val=o,next=None, prev=self.tail)
            self.tail.next = node
            self.tail = node
        elif self.head:
            raise InvalidDequeState("Head is defined when tail isn't")
        else:
            self.tail = self.head = Node(val=o,next=None,prev=None)


    def pop_back(self) -> T:
        if not self.tail:
            raise ValueError("Deque is empty!")
        if not self.head:
            raise InvalidDequeState("Head is not defined when tail is")
        back_value = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = self.tail
        return back_value

            

    def front(self) -> T:
        if not self.head:
            raise ValueError("Deque is empty!")
        if not self.tail:
            raise InvalidDequeState("Head is not defined when tail is")
        return self.head.val

    def back(self) -> T:
        if not self.tail:
            raise ValueError("Deque is empty!")
        if not self.head:
            raise InvalidDequeState("Head is not defined when tail is")
        return self.tail.val


    def size(self) -> int:
        if not self.head:
            return 0
        elif not self.tail:
            raise InvalidDequeState("Tail is not defined when head is")
        n_elements = 1
        node = self.head
        while node != self.tail:
            node = node.next
            n_elements += 1
        return n_elements
            


IntLLDeque = LLDeque[int]


def main() -> None:
    deque = IntLLDeque()
    assert deque.size() == 0
    val_1 = 10
    val_2 = 20
    deque.push_front(val_1)
    deque.push_front(val_2)
    assert deque.size() == 2
    assert deque.front() is val_2
    assert deque.back() is val_1
    assert deque.pop_front() is val_2
    assert deque.size() == 1
    try:
        deque.pop_front()
    except ValueError:
        pass
    deque.push_back(10)
    assert deque.pop_back() == 10
    deque.push_front(23)
    assert deque.pop_back() == 23
    deque.push_back(25)
    assert deque.pop_front() == 25
    deque.push_front(100)
    deque.push_front(100)
    deque.push_front(100)
    assert deque.size() == 3
    print('done')

if __name__ == '__main__':
    main()

