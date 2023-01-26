
def main():
    import sys
    sys.setrecursionlimit(10**7)
    def dfs(x,cnt,arr,C):

        seen[x] = True
        if cnt[C[x]] + 1 > 1: #２食ある
            arr[x] = False
        cnt[C[x]] += 1
        for nx in edge[x]:
            if seen[nx] == False:
                seen[nx] = True
                dfs(nx,cnt,arr,C)
                cnt[C[nx]] -= 1
        
                
        
    from collections import defaultdict,deque
    N = int(input())
    C = list(map(int,input().split()))
    edge = [[]*N for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    seen = [False]*(N)
    cnt = defaultdict(int)
    arr = [True]*(N)
    for i in range(N):
        if seen[i] == False:
            dfs(i,cnt,arr,C)
    for i in range(N):
        if arr[i]:
            print(i+1)
            
            
    
    
    
if __name__ == '__main__':
    main()