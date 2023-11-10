import sys
sys.setrecursionlimit(10 ** 7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

H,W,A,B = mi()
ans = 0
tile = [[0] * W for _ in range(H)]
#左から右に見ていく
#最初にBで全て埋めてみる　なかったらタイルを一枚削ってAで埋めてみるそのあとBで埋める
def dfs(i,j,a,b):
    global ans
    if a < 0 or b < 0:#使っているタイルが-1になるのはありえないので戻る
        return
    if j == W: #全て見た
        j = 0
        i += 1#この時にi == H だったら全て見ていることになるのか
        
    if i == H: #全て見た
        ans += 1
        return
    
    #使用されている時
    if tile[i][j] == 1:
        dfs(i,j+1,a,b)
        
    tile[i][j] = 1
    #Bとして使用するとき
    dfs(i,j+1,a,b-1)
    if j+1 < W and tile[i][j+1] == 0:
        tile[i][j+1] = 1
        dfs(i,j+1,a-1,b)
        tile[i][j+1] = 0
    if i+1 < H and tile[i+1][j] == 0:
        tile[i+1][j] = 1
        dfs(i+1,j,a-1,b)
        tile[i+1][j] = 0
        
    tile[i][j] = 0
    return ans


     
    
        
    
    
        
    
