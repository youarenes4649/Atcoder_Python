import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

H,W = mi()
A = []
for _ in range(H):
    a = li()
    A.append(a)
    ans = 0
def dfs(x,i,j):
    global ans
    if i == H-1 and j == W-1:
        if len(x) == len(set(x)):
            ans += 1
            
    if i+1 < H:
        dfs(x + [A[i+1][j]],i+1,j)
    if j+1 < W:
        dfs(x + [A[i][j+1]],i,j+1)
        
dfs([A[0][0]],0,0)
print(ans)
