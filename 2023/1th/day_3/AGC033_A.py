
def main():
    from collections import deque
    def serch(x,y,dist):
        Dx = [0,0,1,-1]
        Dy = [1,-1,0,0]
        que = deque()
        que.append([x,y])
        dist[x][y] = 0
        while len(que) > 0:
            x,y = que.popleft()
            for dx,dy in zip(Dx,Dy):
                nx = x+dx
                ny = y+dy
                if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        que.append([nx,ny])
                
    H,W = map(int,input().split())
    grid = []
    for i in range(H):
        a = list(map(str,input()))
        grid.append(a)
    dist = [[10**10]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                serch(i,j,dist)
    ans = 0 
    for i in range(H):
        for j in range(W):
            ans = max(ans,dist[i][j])
    print(ans)
if __name__ == '__main__':
    main()