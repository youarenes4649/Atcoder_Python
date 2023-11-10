import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def solve():
    x1,x2,x3 = mi()
    if x1 == x2 and x2 == x3:
        return 0
        
    A = [x1,x2,x3]
    A.sort()
    x1,x2,x3 = A
    sa1 = x2 - x1
    sa2 = x3 - x2
    if sa1 < sa2:
        now = sa1
    else:
        now = sa2
        
    if now % 2 == 1:
        return -1
    else:
        ope1 = now // 2
        x1 += ope1 * 7
        x2 += ope1 * 5
        x3 += ope1 * 3
        if sa1 < sa2:
            #今x1 == x2
            now = x3 - x2
            if now % 6 != 0:
                return -1
            else:
                ope2 = 2 * (now // 6)
        else:
            now = x2 - x1
            if now % 6 != 0:
                return -1
            
            else:
                ope2 = 2 * (now // 6)
                
        return ope1 + ope2
                
                
        
        
        
def main():
    T = ii()
    for _ in range(T):
        ans = solve()
        print(ans)
        
if __name__ == '__main__':
    main()