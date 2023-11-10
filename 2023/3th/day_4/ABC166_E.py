import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from collections import defaultdict
def main():
    N = ii()
    A = li()
    cnt = defaultdict(int)
    ans = 0
    for i in range(N - 1):
        a = i + 1
        b = i + 2
        cnt[a + A[a - 1]] += 1
        ans += cnt[b - A[b - 1]] 
        
    print(ans)
        
    
if __name__ == '__main__':
    main()