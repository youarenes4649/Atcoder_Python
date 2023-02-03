# 得られる報酬を最大にしたまま木を保たないといけない　＝　つないだとき得られる報酬を最小化するときMSTを作ればok

def main():
    import heapq
    N,M = map(int,input().split())
    edge = [[] * N for _ in range(N)]
    mst_total = 0
    for i in range(M):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        if c < 0:  
            c = 0
        edge[a].append((b,c))
        edge[b].append((a,c))
            
        mst_total += c
    
    que = [(c,i) for i,c in edge[0]]
    heapq.heapify(que)
    seen = [False] * N 
    seen[0] = True
    while len(que) > 0:
        cost,x = heapq.heappop(que)
        
        if seen[x]:
            continue
        seen[x] = True
        mst_total -= cost
        for nx,nc in edge[x]:
            if seen[nx]:
                continue
            heapq.heappush(que,(nc,nx))
            
    
    print(mst_total)
        
        
        
    
        
if __name__ == '__main__':
    main()