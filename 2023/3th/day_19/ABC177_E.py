import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from math import gcd
def main():
    N = ii()
    A = li()
    GCD = A[0]
    for a in A:
        GCD = gcd(GCD,a)
        
    if GCD != 1:
        print('not coprime')
        exit()
        
    count = [0] * (10 ** 6 + 1)
    for a in A:
        count[a] += 1
    for i in range(2,10**6 + 1):
        cnt = 0
        for j in range(i,10**6+1,i):
            cnt += count[j]
            
        if cnt > 1:
            print('setwise coprime')
            exit()
            
    print('pairwise coprime')
if __name__ == '__main__':
    main()