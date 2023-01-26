def main():
    import sys
    sys.setrecursionlimit(10**7)
    def dfs(x,c):
        global COUNT1,COUNT2
        seen[x] = c
        COUNT1 += 1
        for nx in edge[x]:
            if seen[nx] != 0:
                continue
            if seen[nx] == seen[x]:
                print(0)
                exit()
            seen[nx] = -c
            COUNT2 += 1
            dfs(nx,-c)
        return COUNT1,COUNT2
    
    N,M = map(int,input().split())
    edge = [[]*N for _ in range(N)]
    for i in range(M):
        v,u = map(int,input().split())
        v -= 1
        u -= 1
        edge[u].append(v)
        edge[v].append(u)
        
    seen = [0]*(N)
    for i in range(N):
        if seen[i] != 0:
            continue
        COUNT1 = 0
        COUNT2 = 0
        brack,white = dfs(i,-1)  
        ans = N*(N-1)//2 - M 
        ans -= brack*(brack-1)//2
        ans -= white*(white-1)//2

    
    
        
if __name__ == '__main__':
    main()