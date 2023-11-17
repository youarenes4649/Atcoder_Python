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
    H,W,N = mi()
    Z = [[0] * (W+1) for _ in range(H+1)]
    for _ in range(N):
        a,b,c,d = mi()
        a-=1
        b-=1
        c-=1
        d-=1
        Z[a][b] += 1
        Z[c+1][d+1] += 1
        Z[a][d+1] -= 1
        Z[c+1][b] -=1 

    for i in range(H+1):
        for j in range(1,W+1):
            Z[i][j] += Z[i][j-1]

    for j in range(W+1):
        for i in range(1,H+1):
            Z[i][j] += Z[i-1][j]

    
    for i in range(H):
        print(*Z[i][:-1])

if __name__ == '__main__':
    main()