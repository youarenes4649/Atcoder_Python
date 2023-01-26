H,W,rs,cs=map(int,input().split())
grid=[['.']*W for _ in range(H)]
grid_p=[['.']*W for _ in range(H)]
N=int(input())
for i in range(N):
    r,c=map(int,input().split())
    r-=1
    c-=1
    grid[r][c]='#'#かべ
    grid_p[c][r]='#'

Q=int(input())
from collections import defaultdict
ope=defaultdict(list)
ope['L']=-1
ope['R']=1
ope['U']=1
ope['D']=1
for i in range(Q):
    d,l=input().split()
    if d=='L':
        if '#' in set(grid[rs]) and if 


