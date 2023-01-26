
def main():
    N = int(input())
    S = [input() for i in range(N)]
    T = [input() for i in range(N)]
    
    grid_s = set()
    grid_t = set()
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                grid_s.add((i,j))
                
            if T[i][j] == '#':
                grid_t.add((i,j))
                
    print(min(grid_s)) 
    for i in range(4):
        mx,my = min(grid_s)
        grid_s = set((x-mx,y-my) for x,y in grid_s)
        
        mx,my = min(grid_t)
        grid_t = set((x-mx,y-my) for x,y in grid_t)
        
        if grid_s == grid_t:
            print('Yes')
            exit()
            
        grid_t = set((y,-x) for x,y in grid_t)
            
    print('No')
 
if __name__ == '__main__':
    main()