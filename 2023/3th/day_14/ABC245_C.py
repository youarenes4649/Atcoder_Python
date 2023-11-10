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
    N,K = mi()
    A = li()
    B = li()
    dp = [[False] * 2 for _ in range(N)]
    dp[0][0] = True
    dp[0][1] = True
    
    for i in range(N-1):
        if abs(A[i+1] - A[i]) <= K:
            dp[i+1][0] |= dp[i][0]
        if abs(B[i+1] - A[i]) <= K:
            dp[i+1][1] |= dp[i][0]
        if abs(A[i+1] - B[i]) <= K:
            dp[i+1][0] |= dp[i][1]
        if abs(B[i+1] - B[i]) <= K:
            dp[i+1][1] |= dp[i][1]
            
    if dp[-1][0] == True or dp[-1][1] == True:
        print('Yes')
    else:
        print('No')
             
             
                       
        
if __name__ == '__main__':
    main()