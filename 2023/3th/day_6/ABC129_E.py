import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 10 ** 9 + 7
 
def main():
    L = input()
    dp = [[0] * 2  for _ in range(len(L) + 1)]
    dp[0][0] = 1
    dp[0][1] = 0
    for i in range(len(L)):
        now_c = L[i]
        # a,b = (0,0)
        if now_c == '0':
            dp[i+1][0] += dp[i][0]
            dp[i+1][0] %= mod
            dp[i+1][1] += dp[i][1]
            dp[i+1][1] %= mod
            
        else:
            dp[i+1][1] += dp[i][0] + dp[i][1] 
            dp[i+1][1] %= mod
            
        #a,b = (1,0) or (0,1)
        if now_c == '0':
            dp[i+1][1] += dp[i][1] * 2
            dp[i+1][1] %= mod
            
        else:
            dp[i+1][0] += dp[i][0] * 2
            dp[i+1][0] %= mod
            dp[i+1][1] += dp[i][1] * 2
            dp[i+1][1] %= mod
            
    
    print((dp[len(L)][0] + dp[len(L)][1])% mod)
              
if __name__ == '__main__':
    main()