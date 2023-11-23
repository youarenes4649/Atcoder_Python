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
    X = []
    Y = []
    for _ in range(N):
        x,y = mi()
        X.append(x)
        Y.append(y)
    
    dp = [[float(inf)] * N for _ in range(1 << N)]

    dp[0][0] = 0
    for S in range(1 << N):
        for u in range(N):
            if dp[S][u] == float(inf):
                continue
            for v in range(N):
                if S & (1 << v)  == 0:
                    dist = (X[v] - X[u]) ** 2 + (Y[v] - Y[u]) ** 2
                    dist = dist ** 0.5
                    T = S | (1 << v)
                    dp[T][v] = min(dp[T][v],dp[S][u]+dist)

    
    print(dp[-1][0])


            
if __name__ == '__main__':
    main()