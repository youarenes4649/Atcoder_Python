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
    A,B = mi()
    a = li()
    b = li()
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    
    for l in range(A,-1,-1):
        for r in range(B,-1,-1):
            if l == A and r == B:
                continue
            if (l + r) % 2 == 0: #先手の時
                if l == A:
                    dp[l][r] = max(dp[l][r],dp[l][r+1] + b[r])
                elif r == B:
                    dp[l][r] = max(dp[l][r],dp[l+1][r] + a[l])
                else:
                    dp[l][r] = max(dp[l][r],dp[l+1][r] + a[l],dp[l][r+1]+b[r])    
            else:
                if l == A:
                    dp[l][r] = dp[l][r+1]
                elif r == B:
                    dp[l][r] = dp[l+1][r] 
                else:
                    dp[l][r] = min(dp[l+1][r],dp[l][r+1])  
                    
    print(dp[0][0]) 
if __name__ == '__main__':
    main()