import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import defaultdict
import bisect
def main():
    N,K = mi()
    A = li()
    L = A[:K]
    R = A[K:]
    max_arr = [R[0]] #最短のでかい数を導入する
    location = defaultdict(int)
    for i in range(1,N - K):
        if max_arr[-1] < R[i]:
            max_arr.append(R[i])
        else:
            max_arr.append(max_arr[-1])
    for i in range(N - K):
        if location[R[i]] == 0:
            location[R[i]] = i + K
        #例外
    if min(A[:K]) >= max(A[K:]):
        print(-1)
        exit()
    ans = 10 ** 20
    for i in range(K):
        now = L[i]
        idx = bisect.bisect_right(max_arr,now)
        #もし大きくて動かせなかったら
        if idx == N - K:
            continue
        loc_r = location[R[idx]]
        ans = min(ans,loc_r - i)
    
    if ans == 10 ** 20:
        print(-1)
    else:
        print(ans)
        
if __name__ == '__main__':
    main()