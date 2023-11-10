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
    N,K,D = mi()
    A = li()
    dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N+1) ]
    
    for i in range(N):
        dp[i][0][0] = 0
    for i in range(N):
        for j in range(K+1):#すでにKこ撮ってる時ある
            for d in range(D):
                if dp[i][j][d] == -1:
                    continue
                dp[i+1][j][d] = max(dp[i+1][j][d],dp[i][j][d]) #Kは増えないからk+1にしないと
                if j < K :
                    dp[i+1][j+1][(d + A[i])% D] = max(dp[i+1][j+1][(d + A[i]) % D],dp[i][j][d] + A[i])
    
    print(dp[N][K][0])
if __name__ == '__main__':
    main()