N,M=map(int,input().split())
edge=[[] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)


for i in range(1,N+1):
    edge[i].sort()

    print(len(edge[i]),*edge[i])
