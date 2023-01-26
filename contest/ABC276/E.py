from collections import deque

DR=[0,1,0,-1]
DC=[1,0,-1,0]

def good(h,w,grid):
    for r in range(h):
        for c in range(w):
            if grid[r][c]=="S":
                sr,sc=r,c

    seen=[[-1] *w for _ in range(h)]
    q=deque()
    for i in range(4):#sr,scから４方向
        r,c=sr+DR[i],sc+DC[i]
        if 0<=r<h and 0<=c <w and grid[r][c]=='.':#Sは.じゃないから通らないのか
            q.append((r,c))
            seen[r][c]=i


    while len(q)>0:
        r,c=q.pop()
        for i  in range(4):
            r2,c2=r+DR[i],c+DC[i]
            if 0<=r2<h and 0<=c2<w and grid[r2][c2]=='.' and seen[r2][c2]!=seen[r][c]:
                if seen[r2][c2]==-1:
                    q.append((r2,c2))
                    seen[r2][c2]=seen[r][c]

                else:#もうすでにたどり着いたとき
                    return True


    return False


h,w=map(int,input().split())
grid=[input() for _ in range(h)]
print('Yes' if good(h,w,grid) else 'No' )

    
