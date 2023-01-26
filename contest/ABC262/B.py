N,M=map(int,input().split())
edge=[[] for _ in range(N)]
for i in range(M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    edge[u].append(v)
    edge[v].append(u)

ans=0
for a in range(N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            if b in edge[a] and c in edge[a] and c in edge[b]:
                ans+=1

print(ans)