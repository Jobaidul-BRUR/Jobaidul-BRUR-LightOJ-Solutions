import os
import sys
import time
from math import log10

DEBUG = os.getenv("_DEBUG")
if DEBUG:
    input = open("cmake-build-debug/input.txt", "r").readline
    # sys.stdout = open("output.txt", 'w')
else:
    input = sys.stdin.readline
    output = sys.stdout.write

csum = [0] * 1000001
def main(tc):
    n, base = map(int, input().split())
    print(int(csum[n] / log10(base) + (10 ** -9)) + 1)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(1, 1000001):
        csum[i] = csum[i - 1] + log10(i)
    T = 1
    T = int(input())
    for tc in range(1, T + 1):
        print("Case %d:" % tc, end=' ')
        main(tc)
    if DEBUG:
        print("\n--- %0.0f ms ---" % ((time.time() - start_time) * 1000))
