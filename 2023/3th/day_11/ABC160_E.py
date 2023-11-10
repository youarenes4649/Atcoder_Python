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
from collections import deque
def main():
    X,Y,A,B,C = mi()
    P = li()
    Q = li()
    R = li()
    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort(reverse=True)
    P = P[:X]
    Q = Q[:Y]
    All = P + Q
    All.sort()
    All = deque(All)
    ans = 0
    for r in R:
        r_idx = bisect.bisect_right(All,r)
        if r_idx == 0:
            break
        else:
            ans += r
            All.popleft()
            
    print(sum(All) + ans)
            
            
                
    
if __name__ == '__main__':
    main()