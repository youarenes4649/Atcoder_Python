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
    N,S = mi()
    A = li()
    dp = [False] * (S+1)
    dp[0] = True

    for i in range(N):
        for s in range(S,-1,-1):
            if s - A[i] >= 0:
                dp[s] = dp[s-A[i]] | dp[s] 

    if dp[S]:
        print('Yes')
    else:
        print('No')
        

if __name__ == '__main__':
    main()