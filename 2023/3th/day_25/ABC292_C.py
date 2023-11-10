import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
def yakusu(n):#少し遅い
    res=set()
    i=1
    while i*i<=n:
        if n%i==0:
            res.add(i)

            res.add(n//i)
            
        i+=1
    res.add(n)
    return res

def main():
    N = ii()
    ans = 0
    for i in range(1,N):
        A = len(yakusu(i))
        B = len(yakusu(N - i))
        ans += A * B
        
    print(ans)
            
if __name__ == '__main__':
    main()