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
    S = list(map(str,input()))
    arr = []
    cnt = 1
    for i in range(N-1):
        if S[i] == S[i+1] and S[i] == 'o':
            cnt += 1
        else:
            if S[i] == 'o':
                arr.append(cnt)
                cnt = 1
            else:
                cnt = 1
    cnt = 1
    for i in range(N-1,0,-1):
        if S[i] == S[i-1] and S[i] == 'o':
            cnt += 1
        else:
            if S[i] == 'o':
                arr.append(cnt)
                cnt = 1
            else:
                cnt = 1

    if len(arr) == 0 :
        print(-1)
        exit()
    print(max(arr))
if __name__ == '__main__':
    main()