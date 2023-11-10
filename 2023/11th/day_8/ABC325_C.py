import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))


def main():
    def search(x,y):
        for dx,dy in dpos8: 
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W :
                if S[nx][ny] == "#":
                    S[nx][ny] = "."
                    search(nx,ny)
    

    H,W = mi()
    S = []
    for i in range(H):
        s = list(map(str,input()))
        S.append(s)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
                S[i][j] = "."
                search(i,j)
    print(ans)

                
if __name__ == '__main__':
    main()