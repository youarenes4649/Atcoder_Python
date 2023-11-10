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
    S = input()
    good = False
    not_good = False
    for s in S:
        if s == 'o':
            good = True
        if s == 'x':
            not_good = True
            
    if good == True and not_good == False:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()