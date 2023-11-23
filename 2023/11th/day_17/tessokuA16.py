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
    A = li()
    B = li()

    dp = [inf] * (N+1)
    dp[0] = 0 #部屋１
    dp[1] = A[0] #部屋２

    for i in range(2,N):
        dp[i] = min(dp[i], dp[i-1] + A[i-1], dp[i-2]+B[i-2])

    print(dp[N-1])
    

if __name__ == '__main__':
    main()