import os
import sys
import time

DEBUG = os.getenv("_DEBUG")
if DEBUG:
    input = open("cmake-build-debug/input.txt", "r").readline
    # sys.stdout = open("output.txt", 'w')
else:
    input = sys.stdin.readline
    output = sys.stdout.write

cnt = [0] * 1001
a = []
def sieve():
    for i in range(1, 1001):
        for j in range(i, 1001, i):
            cnt[j] += 1
    for i in range(1, 1001):
        a.append((cnt[i], -i))
    a.sort()
def main(tc):
    n = int(input())
    print(-a[n-1][1])


if __name__ == '__main__':
    start_time = time.time()
    sieve()
    T = 1
    T = int(input())
    for tc in range(1, T + 1):
        print("Case %d:" % tc, end=' ')
        main(tc)
    if DEBUG:
        print("\n--- %0.0f ms ---" % ((time.time() - start_time) * 1000))
