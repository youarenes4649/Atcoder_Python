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
    N = ii()
    A,B,C = [],[],[]
    for _ in range(N):
        a,b,c = mi()
        A.append(a)
        B.append(b)
        C.append(c)
    dp = [[-10**10] * 3 for _ in range(N+1)]
    for i in range(3):
        dp[0][i] = 0
        
    for i in range(N):
        for yesterday in range(3):
            for today in range(3):
                if yesterday == today:
                    continue
                dp[i+1][today] = max(dp[i+1][today],dp[i][yesterday]+)
if __name__ == '__main__':
    main()