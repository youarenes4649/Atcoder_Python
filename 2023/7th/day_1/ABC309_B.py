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
    N = ii()
    A = []
    for _ in range(N):
        a = list(map(str,input()))
        A.append(a)
        
    right = []
    left = []
    
    up = A[0]
    down = A[-1]
    for i in range(N):
        right.append(A[i][-1])
        left.append(A[i][0])
        
    up = [A[1][0]] + up[:-1]
    down = down[1:] + [A[-2][-1]]
    right = [A[0][-2]] + right
    left = left[1:] + [A[-1][1]]
    A[0] = up
    A[-1] = down
    for i in range(N):
        A[i][-1] = right[i]
        A[i][0] = left[i]
        ans = ''.join(A[i])
        print(ans)
    
if __name__ == '__main__':
    main()