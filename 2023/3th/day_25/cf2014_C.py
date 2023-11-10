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
    A = ii()
    for n in range(10,10000+1):
        n = str(n)
        tmp = 0
        for i in range(len(n)):
            tmp +=  int(n[::-1][i]) * (int(n) ** i)
        
        if A == tmp:
            print(n)
            exit()
    print(-1)
if __name__ == '__main__':
    main()