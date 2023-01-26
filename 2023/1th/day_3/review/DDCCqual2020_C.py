
def main():
    H,W,K = map(int,input().split())
    straw = []
    for i in range(H):
        s = list(map(str,input()))
        straw.append(s)
        
    ans_grid = [[0]*W for _ in range(H)]
    k = 1
    for i in range(H):
        for j in range(W):
            if straw[i][j] == '#':
                ans_grid[i][j] = k
                k += 1
                
    for i in range(H):
        for j in range(W):
            if ans_grid[i][j] !=0:
                k = ans_grid[i][j]
                while j+1 < W and ans_grid[i][j+1] == 0:
                    ans_grid[i][j+1] =  k
                    j += 1
    for i in range(H):
        for j in range(W):
            if ans_grid[i][j] !=0:
                k = ans_grid[i][j]
                while 0<= j-1 and ans_grid[i][j-1] == 0:
                    ans_grid[i][j-1] =  k
                    j -= 1
    #上下
    for i in range(H):
        for j in range(W):
            if ans_grid[i][j] !=0:
                k = ans_grid[i][j]
                while 0<=i-1 and ans_grid[i-1][j] == 0:
                    ans_grid[i-1][j] =  k
                    i -= 1
                    
    for i in range(H):
        for j in range(W):
            if ans_grid[i][j] !=0:
                k = ans_grid[i][j]
                while i+1 < H and ans_grid[i+1][j] == 0:
                    ans_grid[i+1][j] =  k
                    i += 1
    for i in range(H):
        print(*ans_grid[i])   
        
                
                
if __name__ == '__main__':
    main()