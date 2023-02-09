import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

def main():
    def is_ok(x):
        S_mid = S[x:]
        if S_mid in T:
            return True
        else:
            return False
    cnt = defaultdict(int)
    N = ii()
    S = input()
    T = input()
    if S == T:
        print(0)
        exit()
    

    ok = N + 1
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2 
        
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
            
    print(ok)
if __name__ == '__main__':
    main()