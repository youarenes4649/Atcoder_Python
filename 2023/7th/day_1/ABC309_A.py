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
    A,B = mi()
    if B == A + 1:
        if B == 4 or B == 7:
            print('No')
        else:
            print('Yes')
        exit()
        
    print('No')
            
    
if __name__ == '__main__':
    main()
    