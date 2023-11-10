import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 

h,w,a,b = mi()

used = [[0] * w for _ in range(h)]
res = 0

def dfs(i,j,a,b):
    global res
    if a < 0 or b < 0:
        return 
    if j == w:
        j = 0
        i += 1
    if i == h:
        res += 1
        return
    if used[i][j] == 1:
        return dfs(i,j+1,a,b)
    
    used[i][j] = 1
    dfs(i,j+1,a,b-1)
    if j+1 < w and used[i][j+1] == 0:
        used[i][j+1] = 1
        dfs(i,j+1,a-1,b)
        used[i][j+1] = 0
    
    if i+1 < h and used[i+1][j] == 0:
        used[i+1][j] = 1
        dfs(i+1,j,a-1,b) 
        used[i+1][j] = 0
    used[i][j] = 0
    
    return res
    
