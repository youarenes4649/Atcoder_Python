import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def main():
    N,M = mi()
    AB = []
    C = []
    for i in range(M):
        a,b = mi()
        c = li()
        AB.append((a,b))
        C.append(c)
    
    dp = [10 **20] * (2 ** N)
    #空集合の時　
    dp[0] = 0
    for S in range(2 ** N):
        for j in range(M):
            now = 0
            for c in C[j]:
                now |= 1 << (c-1)
            dp[S|now] = min(dp[S|now],dp[S] + AB[j][0])
    
    print(dp[(1 << N) - 1 ] if not dp[(1 << N) - 1] == 10 ** 20 else -1)
if __name__ == '__main__':
    main()