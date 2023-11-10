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
    def check(a,b):
        for i in range(N):
            for j in range(N):
                if a[i][j] == 1 :
                    if b[i][j] == 0:
                        return False
                    
        return True
                    
    N = ii()
    A = [li() for _ in range(N)]
    B = [li() for _ in range(N)]
    
    if check(A,B):
        print('Yes')
        exit()
    for n in range(3):
        A_tmp = []
        for i in range(N):
            tmp = []
            for j in range(N):
                tmp.append(A[N-1-j][i])
            A_tmp.append(tmp)
        A = A_tmp
        if check(A,B):
            print('Yes')
            exit()
                
    
    print('No')
if __name__ == '__main__':
    main()