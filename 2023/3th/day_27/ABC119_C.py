import sys
sys.setrecursionlimit(10 ** 7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def main():
    N,A,B,C = mi()
    take = []
    for _ in range(N):
        l = ii()
        take.append(l)
        
    def dfs(cnt,a,b,c):
        if cnt == N:
            # - 30 しているのは　竹を必ず１本以上は使用するため。 ０から１に増やすときに+10をしてしまっている分
            return abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(a,b,c) > 0 else 10 ** 9
        
        #竹を使用しないとき
        ans1 = dfs(cnt + 1,a,b,c)
        ans2 = dfs(cnt + 1,a + take[cnt],b,c) + 10
        ans3 = dfs(cnt + 1,a,b + take[cnt],c) + 10
        ans4 = dfs(cnt + 1,a,b,c + take[cnt]) + 10
        
        return min(ans1,ans2,ans3,ans4)
    
    print(dfs(0,0,0,0))
if __name__ == '__main__':
    main()