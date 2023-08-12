import sys
import tty
import time
import termios

tty.setcbreak(0)

while True:
    char = sys.stdin.read(1)
    try:
        n_times = int(char)
    except ValueError:
        n_times = 0
    for _ in range(n_times):
        sys.stdout.buffer.write(b'\x07')
    sys.stdout.buffer.flush()


