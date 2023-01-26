def main():
    N = int(input())
    S = input()
    dp = [[0]* (N+1) for _ in range(N+1)]
    
    for l in range(1,N):
        for r in range(N,l,-1):
            if S[l-1] == S[r-1]:
                dp[l][r] = max(dp[l+1][r],dp[l][r-1],dp[l+1][r-1]+2)
                
            else:
                dp[l][r] = max(dp[l+1][r],dp[l][r-1],dp[l][r])
                
    ans = 0
    for i in range(1,N+1):
        ans = max(ans,dp[i][i])
    print(ans)

                
if __name__ == '__main__':
    main()