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
def main():
    N,T = mi()
    C = li()
    R = li()
    cnt = defaultdict(list)
    number = 0
    for c,r in zip(C,R):
        cnt[c].append((r,number))
        number += 1
    if len(cnt[T]) != 0:
        cnt[T].sort()
        print(cnt[T][-1][1]+1)
    else:
        cnt[C[0]].sort()
        print(cnt[C[0]][-1][1]+1)
        
    
if __name__ == '__main__':
    main()