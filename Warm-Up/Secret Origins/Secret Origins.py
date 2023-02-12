import os
import sys
import time
from math import acos

DEBUG = os.getenv("_DEBUG")
if DEBUG:
    input = open("cmake-build-debug/input.txt", "r").readline
    # sys.stdout = open("output.txt", 'w')
else:
    input = sys.stdin.readline
    output = sys.stdout.write


def main(tc):
    n = int(input())
    cnt = 0
    for i in range(31):
        if n & (1 << i):
            cnt += 1
            n ^= (1 << i)
        elif cnt:
            n ^= (1 << i)
            break
    for i in range(cnt-1):
        n ^= (1 << i)

    print(n)

if __name__ == '__main__':
    start_time = time.time()
    T = 1
    T = int(input())
    for tc in range(1, T + 1):
        print("Case %d:" % tc, end=' ')
        main(tc)
    if DEBUG:
        print("\n--- %0.0f ms ---" % ((time.time() - start_time) * 1000))
