
def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    dp = [10**10]*N
    dp[0] = 0
    dp[1] = A[0]
    for i in range(N-2):
        dp[i+2] = min(dp[i+2],dp[i+1] + A[i+1], dp[i] + B[i])
    
    P = [N]
    now = N
    while now > 0:
        if dp[now-1] == dp[now-2] + A[now-2]:
            now -= 1
            
        else:
            now -= 2
        P.append(now)
        
    print(len(P)-1)
    print(*P[::-1][1:])
        
            
        
if __name__ == '__main__':
    main()