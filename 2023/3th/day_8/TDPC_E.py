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
    digits = len(str(N))
    dp = [[[0] * (D) for _ in range(2)] for _ in range(digits + 1)]
    dp[0][0][0] = 1
    
    for i in range(digits):
        for j in range(2):
            for k in range(D):#現在の桁までの和
                for l in range(10):#次の桁に選ぶ数字
                    if j == 0 and l < int(str(N)[i]):
                        dp[i+1][1][(k + l) % D] += dp[i][j][k] % mod
                        
                    elif (j == 0 and l == int(str(N)[i])) or j == 1:
                        dp[i+1][j][(k + l) % D] += dp[i][j][k] % mod
                        
    print((dp[digits][0][0] + dp[digits][1][0] - 1)%mod)
                        
                         
            
                
                
        
            
if __name__ == '__main__':
    main()