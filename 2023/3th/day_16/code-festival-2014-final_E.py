import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def main():
    N = ii()
    R = li()
    if N < 3:
        print(0)
        exit()
        
    dp = [[0] * 2 for _ in range(N)]
    for i in range(N):
        dp[i][0] = dp[i][1] = 1
        for j in range(i):
            if R[j] < R[i]:
                dp[i][0] = max(dp[i][0],dp[j][1] + 1)
            if R[j] > R[i]:
                dp[i][1] = max(dp[i][1],dp[j][0] + 1)
                
    if max(dp[-1]) >= 3:
        print(max(dp[-1]))
    else:
        print(0)
if __name__ == '__main__':
    main()

