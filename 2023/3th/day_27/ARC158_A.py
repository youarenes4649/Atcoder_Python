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
    if (x1 + x2 + x3) % 3 != 0:
        print(-1)
    else:
        if x1 == x2 and x2 == x3:
            return print(0)
        arr = [x1,x2,x3]
        arr.sort()
        x1,x2,x3 = arr
        if x1 != x2 and x2 == x3:
            sub = x2 - x1
            if sub % 3 != 0:
                return print(-1)
            return print(sub // 3)
        
        if x1 != x2 and x2 != x3:
            #x1 == x2 にする
            if (x2 - x1) % 2 != 0:
                return print(-1)
            ope1 = (x2 - x1) // 2
            sub2 = (x3 - x1) - (ope1 * 4)
            if sub2 % 3 != 0:
                return print(-1)
            ope2 = sub2 // 3
            return print(ope1 + ope2)
            
                
            
        
def main():
    T = ii()
    for _ in range(T):
        solve()
if __name__ == '__main__':
    main()