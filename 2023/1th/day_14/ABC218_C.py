
def main():
    N = int(input())
    S = set()
    for i in range(N):
        s = list(map(str,input()))
        for j in range(N):
            if s[j] == '#':
                S.add((i,j))
                
    T = set()
    for i in range(N):
        t = list(map(str,input()))
        for j in range(N):
            if t[j] == '#':
                T.add((i,j))
                
    for i in range(4):
        #最も左の#を基準値にする
        mx,my = min(S)
        S = set((x-mx,y-my)  for x,y in S)
        
        mx,my = min(T)
        T = set((x-mx,y-my)  for x,y in T)    
        
        
        if S == T:
            print('Yes')
            exit()
        
        T = set((y,-x) for x,y in T)
              
    print('No')
if __name__ == '__main__':
    main()