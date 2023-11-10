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
    S = input()
    cnt = defaultdict(int)
    K = 0
    for s in S:
        cnt[s] += 1
    
    for d in cnt:
        if cnt[d] % 2 == 1:
            K += 1
    if K == 0: #すべて偶数の時
        print(len(S))
        exit()
        
    print(1 + 2 * ((len(S) - K)//(2 * K)))
if __name__ == '__main__':
    main()