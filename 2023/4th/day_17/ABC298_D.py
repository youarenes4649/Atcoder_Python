import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import deque
def main():
    Q = ii()
    #文字と答えを別々で持っておけばよかった
    #やり方はあってた
    ans = 1
    S = deque([])
    S.append(1)
    for _ in range(Q):
        query = li()
        
        if query[0] == 1:
            ans = ans * 10 + query[1]
            ans %= mod
            S.append(query[1])
        if query[0] == 2:
            ans -= S[0] * pow(10,len(S)-1, mod)
            S.popleft()
        if query[0] == 3:
            print(ans % mod)
if __name__ == '__main__':
    main()