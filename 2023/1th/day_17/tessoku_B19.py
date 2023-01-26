
def main():
    N,W = map(int,input().split())
    we,va = [],[]
    for _ in range(N):
        w,v = map(int,input().split())
        we.append(w)
        va.append(v)
    
    dp = [[10**9+1] * (10**6+1) for _ in range(N+1)]
    for i in range(N):
        dp[i][0] = 0
        
    for i in range(N):
        for j in range(10**6+1):
            dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            
            if j - va[i] >= 0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j - va[i]] + we[i])
                
    ans = 0
    for j in range(10**6 + 1):
        if dp[N][j] <= W:
            ans = j
            
    print(ans)
        
if __name__ == '__main__':
    main()