import sys
sys.setrecursionlimit(10**7)
def main():

    def makebipartile(x):
        que = deque()
        que.append([x,-1])
        seen[x] = -1
        white = 1
        brack = 0
        while len(que) > 0:
            x,c = que.popleft()
            
            for nx in edge[x]:
                if seen[nx] == c: #二部グラフでない
                    print(0)
                    exit()
                if seen[nx] != 0:
                    continue
                
                seen[nx] = -c
                que.append([nx,-c])
                
                if seen[nx] == 1:
                    brack += 1
                    
                if seen[nx] == -1:
                    white += 1
                    
        cnt = brack * (brack -1) // 2 + white * (white -1) // 2

        return cnt            
            
            
        
        
    from collections import deque
    N,M = map(int,input().split())
    edge = [[] * N for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
        
    ans = N * (N - 1) // 2  - M 
    seen = [0] * N
    for i in range(N):
        if seen[i] != 0: #既に見ていたら
            continue

        ans -= makebipartile(i)
    print(ans)
        
        
if __name__ == '__main__':
    main()