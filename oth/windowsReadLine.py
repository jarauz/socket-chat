import msvcrt

def non_blocking_read():
    if msvcrt.kbhit():
        return input()
    else:
        return None

while True:
    line = non_blocking_read()
    if line is not None:
        print("Read:", line)
    # Do other work here
    print("Doing other work here...")