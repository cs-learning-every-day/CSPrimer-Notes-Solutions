"""
- You can only get so far with linear structures
    - Lots of data is organized hierarchically
- ps command
    - Retrieves processes running in your os
    - Each process, except for the root process (`/sbin/launchd`) has a parent process id
- We will implement pstree
    - Read the stdin of `ps -o pid,ppid,commm`
"""


