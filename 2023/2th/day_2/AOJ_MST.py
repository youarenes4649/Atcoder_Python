
def main():
    N = int(input())
    edge = [[]*N for _ in range(N)]
    for i in range(N):
        for j,c in enumerate(map(int,input().split())):
            if c != -1: 
                edge[i].append((j,c))
                
            
            
    import heapq #計算量削減できる
    mst_ans = 0
    
    que = [(c,i) for i,c in edge[0]] # 最初のノード０からstart するとき０にある辺を全て追加
    heapq.heapify(que)
    seen = [False] * N
    seen[0] = True
    while len(que) > 0:
        cost,node = heapq.heappop(que)
        
        if seen[node]:#すでに見ていたらx
            continue
        seen[node] = True
        mst_ans += cost
        for nx,c in edge[node]:
            if seen[nx]:
                continue   
            heapq.heappush(que,(c,nx))
            
    print(mst_ans)
        

if __name__ == '__main__':
    main()