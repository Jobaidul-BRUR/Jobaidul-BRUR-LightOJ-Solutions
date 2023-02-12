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


def main(tc):
    a, b = map(int, input().split())
    print(a + b)


if __name__ == '__main__':
    start_time = time.time()
    T = 1
    T = int(input())
    for tc in range(T):
        print("Case %d:" % (tc + 1), end=' ')
        main(tc)
    if DEBUG:
        print("\n--- %s ms ---" % ((time.time() - start_time) * 1000))
