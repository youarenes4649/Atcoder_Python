import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
 
def main():
    def is_ok(x):
        cand = []
        for i in range(N):
            w,p = W[i],P[i]
            cand.append((w * p - x * w)/100)
        cand.sort(reverse=True)
        return sum(cand[:K]) >= 0
    
    N,K = mi()
    W = []
    P = []
    for _ in range(N):
        w,p = mi()
        W.append(w)
        P.append(p)
    ok = 100
    ng = 0
    while ok - ng > 10 ** -6:
        mid = (ok + ng) / 2
        if is_ok(mid):
            ng = mid
            
        else:
            ok = mid
            
    print(ok)
if __name__ == '__main__':
    main()