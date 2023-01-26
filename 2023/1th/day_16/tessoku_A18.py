
def main():
    N,S = map(int,input().split())
    A = list(map(int,input().split()))
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    
    for i in range(1,N+1):
        for j in range(S+1):
            dp[i][j] = dp[i][j] | dp[i-1][j] #とらなかったとき
            if j - A[i-1] >= 0:
                dp[i][j] = dp[i][j] | dp[i-1][j-A[i-1]]
                
    if dp[N][S] :
        
        print('Yes')
        
    else:
        print('No')
if __name__ == '__main__':
    main()