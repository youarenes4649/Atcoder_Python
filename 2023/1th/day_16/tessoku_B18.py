def main():
    N,S = map(int,input().split())
    A = list(map(int,input().split()))
    
    dp = [[False] * (S+1) for _ in range(N+1)]
    for i in range(N):
        dp[i][0] = True
 
    for i in range(1,N+1):
        for j in range(S+1):
            dp[i][j] = dp[i][j] | dp[i-1][j]
            
            if j - A[i-1] >= 0:
                dp[i][j] = dp[i][j] | dp[i-1][j-A[i-1]]
                
    now = S
    card = N
    from collections import deque
    use = deque([])
    if dp[N][S] :
        while card > 0:
            if now - A[card-1] >= 0: #これがないとREが出てしまう
                if dp[card-1][now - A[card-1]]  == True:
                    use.appendleft(card)
                    now -= A[card-1]
            card -= 1
                
        print(len(use))
        print(*use)
            
    else:
        print(-1)
        
    
            
if __name__ == '__main__':
    main()