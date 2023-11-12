import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
import bisect
def main():
    N,Q = mi()
    S = input()
    next_ls = []
    for i in range(N-1):
        if S[i] == S[i+1]:
            next_ls.append(i)
    print(next_ls)
    for _ in range(Q):
        l,r = mi()
        l -= 1
        r -= 1
        ans_l = bisect.bisect_left(next_ls,l)
        ans_r = bisect.bisect_left(next_ls,r)
        print(ans_r-ans_l)
if __name__ == '__main__':
    main()