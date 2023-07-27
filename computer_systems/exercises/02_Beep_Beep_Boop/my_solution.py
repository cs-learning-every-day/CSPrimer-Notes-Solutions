"""Planning
- Beep
- echo stdin
- beep n times
"""
import sys
import time
while True:
    test = sys.stdin.readline()
    print(test)
    try:
        n_beeps = int(test.strip())
    except ValueError:
        n_beeps = 0
    for _ in range(n_beeps):
        print("\07")
        #sys.stdout.buffer.write(b'\07')
        time.sleep(1)
