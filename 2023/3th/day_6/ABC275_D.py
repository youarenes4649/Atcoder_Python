import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from functools import lru_cache
def main():
    N = ii()
    @lru_cache(maxsize = 1024)
    def func(x):
        if x == 0:
            return 1
        return func(x // 2) + func(x // 3)
    print(func(N))
if __name__ == '__main__':
    main()