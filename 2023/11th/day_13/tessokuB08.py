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
    grid = [[ 0 for _ in range(1500+2)] for _ in range(1500+2)]

    for _ in range(N):
        x,y = mi()
        grid[x][y] += 1
    
    for i in range(1500+2):
        for j in range(1,1500+2):
            grid[i][j] += grid[i][j-1]
    for j in range(1500+2):
        for i in range(1,1500+2):
            grid[i][j] += grid[i-1][j]

    Q = ii()
    for _ in range(Q):
        a,b,c,d = mi()
        ans = grid[c][d] + grid[a-1][b-1] - grid[a-1][d]-grid[c][b-1]
        print(ans)


if __name__ == '__main__':
    main()