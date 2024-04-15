"""
    - push_right
    - push_left
    - pop_right
    - pop_left
    - size

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push_right(self, val):
        n = Node(val)
        if self.size == 0:
            self.tail = n
        else:
            self.head.next = n
        n.prev = self.head
        self.head = n
        self.size += 1

    def pop_right(self):
        n = self.head
        if n is None:
            raise ValueError
        self.head = n.prev
        if self.head:
            self.head.next = None
        self.size -= 1
        return n.value

    def push_left(self, val):
        n = Node(val)
        if self.size == 0:
            self.head = n
        else:
            self.tail.prev = n
        n.next = self.tail
        self.tail = n
        self.size += 1

    def pop_left(self):
        n = self.tail
        if n is None:
            raise ValueError
        self.tail = n.next
        if self.tail:
            self.tail.prev = None
        self.size -= 1
        return n.value


if __name__ == '__main__':
    d = Deque()
    assert d.size == 0
    val1 = 'first'
    val2 = 'second'
    d.push_right(val1)
    assert d.size == 1
    d.push_right(val2)
    assert d.size == 2
    assert d.pop_right() == val2
    assert d.size == 1
    assert d.pop_right() == val1
    assert d.size == 0
    

    d.push_left(val1)
    assert d.size == 1
    d.push_left(val2)
    assert d.size == 2
    assert d.pop_left() == val2
    assert d.size == 1
    assert d.pop_left() == val1
    assert d.size == 0
 
    
    d.push_right(val1)
    d.push_right(val2)
    assert d.pop_left() == val1
    assert d.pop_left() == val2
    assert d.size == 0

    d.push_left(val1)
    d.push_left(val2)
    assert d.pop_right() == val1
    assert d.pop_right() == val2
    assert d.size == 0

    print('ok')
