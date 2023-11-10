import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
def solve():
    n,m,a,b = mi()
    ans = ((n - 1) * n * a )//2 + n * b 
    print(ans//m)
def main():
    T = ii()
    for _ in range(T):
        solve()
if __name__ == '__main__':
    main()