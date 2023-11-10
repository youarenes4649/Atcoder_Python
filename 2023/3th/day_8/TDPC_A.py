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
    P = li()
    P_sum = sum(P)
    dp = [[False] * (P_sum + 1) for _ in range(N + 1)]
    for i in range(N):
        dp[i][0] = True
        
    for i in range(N):
        for j in range(P_sum + 1):
            dp[i+1][j] = dp[i][j]
            if j - P[i] >= 0:
                dp[i+1][j] = dp[i][j - P[i]]|dp[i][j]#1個目まで見たやつがTrueになるから02 -> 04 はTrueにならない
                
                
    print(sum(dp[N]))
                
                
    
                
    
                
    
if __name__ == '__main__':
    main()