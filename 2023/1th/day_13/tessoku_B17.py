
def main():
    N = int(input())
    H = list(map(int,input().split()))
    dp = [10**10]*N
    dp[0] = 0
    dp[1] = abs(H[1]-H[0])
    
    for i in range(2,N):
        dp[i] = min(dp[i],dp[i-1] + abs(H[i]-H[i-1]), dp[i-2] + abs(H[i]-H[i-2]))
    
    now = N-1
    P = [N]
    while now > 0:
        if dp[now] == dp[now-1] + abs(H[now]-H[now-1]):
            now -= 1
        else:
            now -= 2
            
        P.append(now+1)
    print(len(P))
    print(*P[::-1])
        
        
if __name__ == '__main__':
    main()