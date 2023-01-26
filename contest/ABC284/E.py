# g : グラフの隣接リスト。ただし頂点の番号はすべて真の番号から 1 を引いている
            
N,M = map(int,input().split())
edge = [[]* N for _ in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
    
vis = [False] * N
path = []
limit = 1000000
path = []

answer = 0

def dfs(c):
    global answer
    vis[c] = True
    path.append(c)
    print('append')
    print(path)
    answer += 1
    if answer == limit:
        return
    for d in edge[c]:
        if vis[d] == False:
            dfs(d)

    vis[c] = False
    path.pop()
    print('pop')
    print(path)
    
dfs(0)

print(answer)


    