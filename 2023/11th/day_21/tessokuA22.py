#２つの選択肢系のDP なぜか苦手
def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    dp = [-10**12]*(N+1)  #いけないところから　いけてそれがmaxになってしまうことがある
    dp[1] = 0
    for i in range(1,N):
        dp[A[i-1]] = max(dp[A[i-1]],dp[i]+100)
        dp[B[i-1]] = max(dp[B[i-1]],dp[i]+150)
    print(dp[-1])
if __name__ == '__main__':
    main()