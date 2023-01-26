
def main():
    N,X = map(int,input().split())
    A = []
    B = []
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #dp[i][j][k] == i コメまで見て　j個とった時の　かちkが取れるか？
    dp = [[False]*(10**4+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = True
    
    for i in range(N):
        for j in range(B[i]):
            for k in range(10**4+1):
                
                dp[i+1][k] |= dp[i][k] #取らない時
                
                if k - A[i]*(j+1) >= 0:
              
                    dp[i+1][k] |= dp[i][k-A[i]*(j+1)]
                    
    
    if dp[N][X]:
        print('Yes')
        exit()
    print('No')

    
if __name__ == '__main__':
    main()