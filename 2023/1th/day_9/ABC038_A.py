
def main():
    H,W,A,B = map(int,input().split())
    
    gyou = [0] * H
    retu = [0] * W
    grid = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if gyou[h] < A and retu[w] < B:
                grid[h][w] = 1
                gyou[h] += 1
                retu[w] += 1
                
    for i in range(H):
        print(*grid[i])
                
            
                
if __name__ == '__main__':
    main()