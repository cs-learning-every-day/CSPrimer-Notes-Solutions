# Practice using Stacks
## Queue
- FIFO
- Generally intuitive
- Why is it good for a router to use a queue for packets for example?
    - So that you don't have a packet that waits around forever
    - You get some level of consistency there

## Stacks
- LIFO
- Turns up in computing a lot
    - Stack Memory
- Another example: Back button in a browser
    - How about the forward button? Also a stack
- Deque is useful if you want to keep a limited size of a stack
    - B/c if the size hits some threshold you can remove from the "back", instead of pushing right

## Problem: Unix File Path
- Given a unix file path, simplify it to its simplest form
- "/etc/foo/../bar/baz.txt"
    - "/etc/bar/baz.txt"
