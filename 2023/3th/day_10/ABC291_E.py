import sys
sys.setrecursionlimit(10 ** 7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
def main():
    from collections import deque
    def topological_sort(G, into_num):
        #入ってくる有向辺を持たないノードを列挙
        q = deque()
        #V: 頂点数
        for i in range(N):
            if into_num[i]==0:
                q.append(i)
        
        #以下、幅優先探索
        ans = []
        while q:
            if len(q) >= 2:
                print("No")
                exit()
            v = q.popleft()
            ans.append(v+1)
            for adj in G[v]:
                into_num[adj] -= 1 #入次数を減らす
                if into_num[adj]==0:
                    q.append(adj) #入次数が0になったら、キューに入れる
        
        return ans

            
    N,M = mi()
    edge = [[] * N for _ in range(N)]
    cand = []
    into_num = [0] * N
    for _ in range(M):
        u,v = mi()
        u -= 1
        v -= 1
        edge[u].append(v)
        into_num[v] += 1
    
    seen = [False] * N
    change = [0] * N
    anss = topological_sort(edge,into_num)
    for i,a in enumerate(anss):
        change[a-1] = i + 1
        
    print('Yes')
    print(*change) 
    
if __name__ == '__main__':
    main()