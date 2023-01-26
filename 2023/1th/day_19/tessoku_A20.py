
def main():
    S = input()
    T = input()
    lS = len(S)
    lT = len(T)
    dp = [[0]*(lT+1) for _ in range(lS+1)]

    for i in range(lS):
        for j in range(lT):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
            if S[i] == T[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+1 , dp[i+1][j],dp[i][j+1])
                
    print(dp[lS][lT])
                
            
if __name__ == '__main__':
    main()