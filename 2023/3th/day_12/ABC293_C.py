H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
ans = 0
def dfs(x,i,j):
    global ans 

    if i == H - 1 and j == W - 1:
        if len(x) == len(set(x)):
            ans += 1
            
    if i + 1 < H:
        dfs(x + [A[i+1][j]],i+1,j)
    if j + 1 < W:
        dfs(x + [A[i][j+1]],i,j+1)
        
dfs([A[0][0]],0,0)
print(ans)
    