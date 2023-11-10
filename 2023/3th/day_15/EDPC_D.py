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
    N,We = mi()
    W = []
    V = []
    for _ in range(N):
        w,v = mi()
        W.append(w)
        V.append(v)
    dp = [[-10 ** 10] * (We + 1) for _ in range(N+1)]
    for i in range(N):
        dp[i][0] = 0
        
    for i in range(N):
        for j in range(We+1):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j]) #選ばない時
            if j - W[i] >= 0: #選べる時
                dp[i+1][j] = max(dp[i+1][j],dp[i][j - W[i]]+V[i])
                
    print(max(dp[N]))
                
if __name__ == '__main__':
    main()