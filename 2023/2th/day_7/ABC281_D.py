
def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    dp = [[[-1] * (D) for _ in range(N + 1)] for i in range(N + 1)]
    #dp[i][j][k] 左からi番目でj個選んで　kの倍数　なら１
    for i in range(N+1):#初期条件は必要
        dp[i][0][0] = 0
        
    for i in range(1,N+1):
        for j in range(1,i+1):
            for d in range(D): #D の時は０と同値だからx
                if dp[i-1][j-1][d] == -1: #もしこれだったらむり
                    continue
                
                dp[i][j][d] = max(dp[i][j][d],dp[i-1][j][d])
                
                if i >= j: #操作できるよ
                    dp[i][j][(d + A[i-1]) % D] = max(dp[i][j][(d + A[i-1]) % D],dp[i-1][j-1][d] + A[i-1])
                    
    print(dp[N][K][0])    
                
        
    
        
if __name__ == '__main__':
    main()