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
    def check(x):
        k = 0
        for i in range(N):
            if x <= A[i]:
                k += B[i]
        return k
    
    N,K = mi()
    
    AB = []
    for _ in range(N):
        a,b = mi()
        AB.append([a,b])
        
    AB.sort()
    A = []
    B = []
    for a,b in AB:
        A.append(a)
        B.append(b)
    ok = 10 ** 9 + 1
    ng = 0
    
    while ok - ng > 1:
        mid = (ok + ng) // 2
        
        if check(mid) > K:
            ng = mid
        else:
            ok = mid
            
    print(ok)
    
if __name__ == '__main__':
    main()