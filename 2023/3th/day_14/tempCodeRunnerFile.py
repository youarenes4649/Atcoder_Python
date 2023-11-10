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
    N,K = mi()
    A = li()
    B = li()
    check1 = True
    check2 = True
    ans = True
    for i in range(N):
        if abs(A[i] - B[i+1]) > K and abs(A[i] - A[i+1]) > K:
            check1 = False
        if abs(B[i] - B[i+1]) > K and abs(B[i] - A[i+1]) > K:
            check1 = False   
            
        if check1 ^ check2 == False:
            ans = False
        
    print('Yes' if ans == True else 'No')
            
        
            
        
if __name__ == '__main__':
    main()