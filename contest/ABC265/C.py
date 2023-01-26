H,W=map(int,input().split())
grid=[]
next={'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
for i in range(H):
    g=list(map(str,input()))
    grid.append(g)

miti=[['.']*W for _ in range(H)]
seen=[[False]*W for _ in range(H)]
def check(x,y):
    return 0<=x<H and 0<=y<W and miti[x][y]=='.'

x,y=0,0
i=0
seen[x][y]=True
while check(x,y):
    dx,dy=next[grid[x][y]]
    x+=dx
    y+=dy
   
    if check(x,y)!=True:
        break
        
    if seen[x][y]==False:
        seen[x][y]=True

    else:
        print(-1)
        exit()
    

print(x-dx+1,y-dy+1)

