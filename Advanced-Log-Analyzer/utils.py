# utils.py

import time

def tail_f(filepath):
    """
    Generator function that mimics 'tail -f' by yielding new lines as they are written to the file.
    """
    with open(filepath, "r") as f:
        # Move the pointer to the end of the file
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            yield line
