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
    grid = [[0] * (1500 + 1) for _ in range(1500 + 1)]

    for _ in range(N):
        a,b,c,d = mi()
        grid[a][b] += 1
        grid[a][d] -= 1
        grid[c][b] -= 1
        grid[c][d] += 1

    for i in range(1500+1):
        for j in range(1,1500+1):
            grid[i][j] += grid[i][j-1]
    
    for j in range(1500+1):
        for i in range(1,1500+1):
            grid[i][j] += grid[i-1][j]

    ans = 0
    for i in range(1500+1):
        for j in range(1500+1):
            if grid[i][j] >= 1:
                ans += 1
    
    print(ans)
    
    
    


if __name__ == '__main__':
    main()