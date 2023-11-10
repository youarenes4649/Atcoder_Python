import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
#有向グラフのサイクルを求める　例ABC296E
def scc(N,E):
    n = len(E)
    # rev_Eを作成
    r_E = [[] for i in range(n)]
    for u in range(n):
        for v in E[u]:
            r_E[v].append(u)
 
    # トポロジカルソート
    fin = [-1] * n
    topo = []
    for u in range(n):
        if fin[u] != -1:
            continue
        stack = [u]
        while stack:
            u = stack[-1]
            if fin[u] == -1:
                fin[u] = 0
                for v in E[u]:
                    if fin[v] != -1:
                        continue
                    stack.append(v)
            else:
                stack.pop()
                if fin[u] == 0:
                    fin[u] = 1
                    topo.append(u)
    # 逆辺でdfs
    res = []
    while topo:
        u = topo.pop()
        if fin[u] != 1:
            continue
        fin[u] = 2
        cur = [u]
        i = 0
        while i < len(cur):
            u = cur[i]
            for v in r_E[u]:
                if fin[v] == 2:
                    continue
                fin[v] = 2
                cur.append(v)
            i += 1
        res.append(cur)
 
    g_n = len(res)
    n_e = [[] for i in range(g_n)]
    roop = [0] * g_n
    index = [0] * n
    for u in range(g_n):
        for v in res[u]:
            index[v] = u
    for u in range(N):#Nは頂点の数1~N
        for v in E[u]:
            if index[u] != index[v]:
                n_e[index[u]].append(index[v])
            else:
                roop[index[u]] = 1
 
    # g_n: グループの個数
    # res: グループに属する頂点は何
    # index: 頂点iはどこに属するか
    # n_e: グループ同士のエッジ
    # roop: ループするか
    return g_n, res, index, n_e, roop
def main():
    N = ii()
    A = li()
    edge = [[] * N for _ in range(N)]
    for i in range(N):
        edge[i].append(A[i]-1)
    
    g_n,res,index,n_e,roop = scc(N,edge)
    ans = 0
    for i in range(g_n):
        if roop[i]:
            ans += len(res[i])
    print(ans)
if __name__ == '__main__':
    main()