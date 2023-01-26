
def main():
    from collections import deque
    N,M = map(int,input().split())
    edge = [[]*N for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    
    ans = N*(N-1)//2 - M
    seen = [-1]*N
    for i in range(N):
        if seen[i] != -1:
            continue
        
        que = deque([])
        que.append(i)
        seen[i] =  1
        count1 = 0
        count2 = 0
        while len(que) > 0:
            now = que.popleft()
            if seen[now] == 1:
                count1 += 1
            else:
                count2 += 1
                
            for to in edge[now]:
                if seen[to] == seen[now] :
                    print(0)
                    exit()
                    
                if seen[to] == -1:
                    seen[to] = 1 - seen[now]
                    que.append(to)
        
        ans -= (count1*(count1-1)//2 + count2*(count2-1)//2)
        
    print(ans)
 
        
        
        
        
            
if __name__ == '__main__':
    main()