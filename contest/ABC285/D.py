
def main():
    from collections import defaultdict,deque
    N = int(input())
    set_s = set()
    S = []
    T = []
    change = defaultdict(int)
    for _ in range(N):
        s,t = map(str,input().split())
        set_s.add(s)
        set_s.add(t)
        S.append(s)
        T.append(t)
    
    for i,s in enumerate(set_s):
        change[s] = i
    L = len(set_s)
    edge = [[]*len(set_s) for _ in range(len(set_s))]
    indeg = [0] * L
    for _ in range(N):
        s,t = S[_],T[_]
        s = change[s]
        t = change[t]
        edge[s].append(t)
        indeg[t] += 1
    
    q = deque()
    for i in range(L):
        if indeg[i] == 0:
            q.append(i)
    ans = []
    while len(q) > 0:
        v = q.popleft()
        ans.append(v)
        for chi in edge[v]:
            indeg[chi] -= 1
            if indeg[chi] == 0:
                q.append(chi)
                
    if len(ans)  == L:
        print('Yes')
    else:
        print('No')
        
    
    
    
        
        
        
        

    
        
if __name__ == '__main__':
    main()