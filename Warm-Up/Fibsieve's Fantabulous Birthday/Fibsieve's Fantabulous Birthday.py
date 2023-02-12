import os
import sys
import time
from math import sqrt, ceil

DEBUG = os.getenv("_DEBUG")
if DEBUG:
    input = open("cmake-build-debug/input.txt", "r").readline
    # sys.stdout = open("output.txt", 'w')
else:
    input = sys.stdin.readline
    output = sys.stdout.write


def main(tc):
    n = int(input())
    a = int(ceil(sqrt(n)))
    if a * a < n:
        a += 1
    b = n - (a - 1) * (a - 1)
    x, y = -1, -1
    if a % 2 == 1:
        y = 1
        x = a
        b -= 1
        if b < a:
            y += b
        else:
            y = a
            b -= a -1
            x -= b
    else:
        x = 1
        y = a
        b -= 1
        if b < a:
            x += b
        else:
            x = a
            b -= a - 1
            y -= b
    print(x, y)





if __name__ == '__main__':
    start_time = time.time()
    T = 1
    T = int(input())
    for tc in range(1, T + 1):
        print("Case %d:" % tc, end=' ')
        main(tc)
    if DEBUG:
        print("\n--- %0.0f ms ---" % ((time.time() - start_time) * 1000))
