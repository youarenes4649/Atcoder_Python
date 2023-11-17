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
    N = ii()
    S = {}
    S_que = []
    for i in range(N):
        s,c = mi()
        S[s] = c
        S_que.append(s)
    list = sorted(S.items(), key=lambda x: x[0], )
    S.clear()
    S.update(list)
    S_que.sort()
    S_que = deque(S_que)
    while len(S_que) > 0:
        now = S_que.popleft()
        if S[now] % 2 == 1:
            if now *2 not in S:
                S[now * 2] = 0

            S[now * 2] += S[now] //2
            S[now] = 1
        else:
            if now *2 not in S:
                S[now * 2] = 0

            S[now * 2] += S[now] //2     
            S[now] = 0

        
        if S[now * 2] != 0:
            S_que.append(2*now)

    ans = 0
    for v in S.values():
        ans += v

    print(ans)



if __name__ == '__main__':
    main()