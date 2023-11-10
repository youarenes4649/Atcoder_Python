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
    def cost(s,g):
        a,b,c = town[s]
        p,q,r = town[g]
        return abs(p - a) + abs(q - b) + max(0,r - c)
    N = ii()
    town = []
    for _ in range(N):
        x,y,z = mi()
        town.append((x,y,z))
    dp = [[10 ** 20] * N for _ in range(2 ** N)]
    dp[0][0] = 0
    for S in range(2 ** N): #部分集合S
        for to in range(N):
            for now in range(N):
                if not (S >> now) & 1 and S != 0:
                    continue
                if dp[S][now] + cost(now,to) < dp[S|(1 << to)][to]:
                    dp[S|(1 << to)][to] = dp[S][now] + cost(now,to)
    print(dp[(1 << N) - 1][0])          
if __name__ == '__main__':
    main()
    