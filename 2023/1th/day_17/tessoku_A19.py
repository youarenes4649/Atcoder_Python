
def main():
    N,W = map(int,input().split())
    we,va = [],[]
    for _ in range(N):
        w,v = map(int,input().split())
        we.append(w)
        va.append(v)
    dp = [[0] * (W+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(W+1):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j]) #取らないとき
            
            if j - we[i] >= 0:
                dp[i+1][j] = max(dp[i][j-we[i]] + va[i],dp[i+1][j])
    
    print(max(dp[N]))
            
if __name__ == '__main__':
    main()