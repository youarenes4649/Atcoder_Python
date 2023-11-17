import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

def main():
    H,W = mi()
    matrix = [0 * (W+2)]
    for i in range(H):
        x = li()
        matrix.append([0] + x + [0])
    
    matrix.append([0]*(W+2))
    for i in range(H+2):
        for j in range(1,W+2):
            matrix[i][j] += matrix[i][j-1]

    for j in range(W+2):
        for i in range(1,H+2):
            matrix[i][j] += matrix[i-1][j]

    
    Q = ii()
    for _ in range(Q):
        a,b,c,d = mi()
        ans = matrix[c][d] - matrix[c][b-1] - matrix[a-1][d] + matrix[a-1][b-1]
        print(ans)




    

if __name__ == '__main__':
    main()