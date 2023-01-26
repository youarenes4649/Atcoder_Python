#unionfindでとける　交点を持っていたら無変更グラフに追加する
N=int(input())
import sys
import math
sys.setrecursionlimit(10**7)
sx,sy,tx,ty=map(int,input().split())
circul=[]
for i in range(N):
    x,y,r=map(int,input().split())
    circul.append([x,y,r])


edge=[[] for _ in range(N)]

for i in range(N-1):
    xi,yi,ri=circul[i]
    for j in range(i+1,N):
        xj,yj,rj=circul[j]

        d=math.sqrt((xi-xj)**2+(yi-yj)**2)
        if d**2>(ri+rj)**2:
            continue

        if d**2<abs(ri-rj)**2:
            continue

        edge[i].append(j)
        edge[j].append(i)

seen=[False]*N#startからそこにいけたらTrue
def dfs(x):
    seen[x]=True
    for nx in edge[x]:
        if seen[nx]==True:
            continue
        
        dfs(nx)


for s in range(N):#startの位置を確認
    xi,yi,ri=circul[s]
    if (sx-xi)**2+(sy-yi)**2==ri**2:
        start=s

for g in range(N):#goalの位置を確認
    xi,yi,ri=circul[g]
    if (tx-xi)**2+(ty-yi)**2==ri**2:
        goal=g

seen[start]=True
dfs(start)

if seen[goal]:
    print('Yes')

else:
    print('No')

