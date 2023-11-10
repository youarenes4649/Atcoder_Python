import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
 
def main():
    N,X = mi()
    A = []
    B = []
    for _ in range(N):
        a,b = mi()
        A.append(a)
        B.append(b)
    dp = [[False] * (X + 1) for _ in range(N + 1)]
    for i in range(N):
        dp[i][0] = True
    
    for i in range(N):
        for j in range(B[i] + 1):
            for x in range(X + 1):
                if x - A[i] * j >= 0:
                    dp[i+1][x] = dp[i][x - A[i] * j ] | dp[i+1][x]
   
    if dp[N][X]:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()