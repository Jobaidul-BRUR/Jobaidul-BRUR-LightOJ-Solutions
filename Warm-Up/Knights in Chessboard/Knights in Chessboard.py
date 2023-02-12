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
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n
    if n == 1:
        print(m)
    elif n == 2:
        ans = m // 4 * 4
        m -= ans
        if m == 1:
            ans += 2
        elif m >= 2:
            ans += 4
        print(ans)
    else:
        print((n*m+1)//2)


if __name__ == '__main__':
    start_time = time.time()
    T = 1
    T = int(input())
    for tc in range(1, T + 1):
        print("Case %d:" % tc, end=' ')
        main(tc)
    if DEBUG:
        print("\n--- %0.0f ms ---" % ((time.time() - start_time) * 1000))
