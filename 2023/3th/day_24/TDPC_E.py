import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 10 ** 9 + 7
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def main():
    D = ii()
    N = ii()
    len_N = len(str(N))
    #dp[i][j][d] 左からi桁まで見た時N未満かどうか(jflag)かつdの倍数なら0
    dp = [[[0] * (D) for _ in range(2)] for _ in range(len_N + 1)]
    dp[0][0][0] = 1
    #j == 1 未満を示している
    for i in range(len_N):
        now_n = int(str(N)[i])
        for j in range(2):
            for d in range(D):
                for l in range(10):
                    if j == 0 and l < now_n:
                        dp[i+1][1][(d + l) % D] += dp[i][j][d] % mod
                    if j == 0 and l == now_n:
                        dp[i+1][0][(d + l) % D] += dp[i][0][d] % mod
                    if j == 1:
                        dp[i+1][1][(d + l) % D] += dp[i][1][d] % mod
                        
    print((dp[-1][0][0] + dp[-1][1][0] - 1)% mod)
                    
                
        
if __name__ == '__main__':
    main()