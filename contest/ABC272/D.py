
import heapq
N,M=map(int,input().split())
dist=[[10**7]*N for _ in range(N)]
zx_cand=[]
zy_cand=[]
for i in range(N+1):
    for j in range(N+1):
        if i**2+j**2==M:
            zx_cand.append(i)
            zy_cand.append(j)

dist=[[10**7]*N for _ in range(N)]

def judge(x,y):
    return 0<=x<N and 0<=y<N 

def seach(x,y,dx,dy):
    
    que=[(0,x,y)]
    dist[x][y]=0
    while len(que)>0:
        d,now_x,now_y=heapq.heappop(que)
        if d>dist[now_x][now_y]:
            continue
        for nx,ny in zip(dx,dy):
            new_x=now_x+nx
            new_y=now_y+ny
            if judge(new_x,new_y)==True:
                if dist[new_x][new_y]>d+1:
                    dist[new_x][new_y]=d+1
                    heapq.heappush(que,(dist[new_x][new_y],new_x,new_y))
    return dist

for zx,zy in zip(zx_cand,zy_cand):#ここ　sqrtMになるやつならどれでもいい
    dx=[zx,zx,-zx,-zx,zy,zy,-zy,-zy]
    dy=[zy,-zy,zy,-zy,zx,-zx,zx,-zx]
    ans=seach(0,0,dx,dy)

for i in range(N):
    for j in range(N):
        if dist[i][j]==10**7:
            dist[i][j]=-1
for i in range(N):
    print(*dist[i])