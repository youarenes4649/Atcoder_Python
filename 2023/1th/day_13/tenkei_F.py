
def main():
    N,M = map(int,input().split())
    edge = [[]*N for _ in range(N)]
    for _ in range(M):
        u,v,c = map(int,input().split())
        edge[u].append((c,v))
        edge[v].append((c,u))
        
    import heapq
    
    mati = [False]*N #こいつを全部見たらおしまい
    mati_cnt = 1
    mati[0] = True
    
    que = []
    for c,i in edge[0]:
        heapq.heappush(que,(c,i))
    total = 0
    
    while mati_cnt < N:
        c,i = heapq.heappop(que)
        
        if mati[i] :
            continue
        mati[i] = True
        mati_cnt += 1
        
        total += c
        for c,j in edge[i]:
            if mati[j]:
                continue
            heapq.heappush(que,(c,j))
        
    print(total)        
        
        
if __name__ == '__main__':
    main()