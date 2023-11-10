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
    a,b,x,y = mi()
    if a == b:
        print(x)
    else:
        if a < b:
            ans1 = x + (b - a) * y
            ans2 = (2 * (b - a) + 1) * x
            print(min(ans1,ans2))
        else:
            ans1 = x + (a - b - 1) * y
            ans2 = (2 * (a - b) - 1) * x
            print(min(ans1,ans2))
if __name__ == '__main__':
    main()