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
import  bisect
def main():
    N,K = mi()
    A = li()
    L = A[:K]
    R = A[K:]
    
    #例外
    if min(A[:K]) >= max(A[K:]):
        print(-1)
        exit()
    A_max = [R[0]]
    for i in range(1,N - K):
        if A_max[-1] < R[i]:
            A_max.append(R[i])
        else:
            A_max.append(A_max[-1])
            
    R_loc = defaultdict(int)
    for i in range(N - K):
        if R_loc[R[i]] == 0:
            R_loc[R[i]] = K + i
    
    ans = 10 ** 20
    
    for l in range(K):
        al = A[l]
        idx_l = bisect.bisect_right(A_max,al)
        if idx_l == N - K:
            continue
        
        ans = min(ans,R_loc[A_max[idx_l]] - l)
        
    
    if ans == 10 ** 20:
        print(-1)
    else:
        print(ans)
        
    
if __name__ == '__main__':
    main()