
def main():
    H,W,A,B = map(int,input().split())
    grid = [['0']*W for _ in range(H)]
    
    for i in range(B):
        for j in range(A):
            grid[i][j] = '1'
            
    for i in range(B,H):
        for j in range(A,W):
            grid[i][j] = '1'
            
            
            
    for i in range(H):
        print(''.join(grid[i]))
    
    
if __name__ == '__main__':
    main()