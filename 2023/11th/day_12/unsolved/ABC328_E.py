import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from itertools import combinations
#　全域木になっているか判定はUnionFindで行ける
class UnionFind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n

    def merge(self, a, b):#a,bを同じグループとして記録
        x, y=self.leader(a), self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y] 
        self.parent_size[y]=x
        return 

    def same(self, a, b):#a,bが同じグループならTrueを返す
        return self.leader(a) == self.leader(b)

    def leader(self, a):#aのリーダー（元の根を返す）
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]

    def size(self, a):#aが所属しているグループのサイズを返す
        return abs(self.parent_size[self.leader(a)])

    def groups(self):#groupをリストで返す
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

def main():
    N,M,K = mi()
    g = []
    for i in range(M):
        u,v,w = mi()
        u -= 1
        v -= 1
        g.append([u,v,w%K])
    ans = inf

    for comb in combinations(g,N-1):
        uf = UnionFind(N)
        ok = True #全域木かどうか判定する
        tmp_ans = 0

        for u,v,w in comb:
            if uf.same(u,v):
                ok = False
            else:
                uf.merge(u,v)
                tmp_ans += w
                tmp_ans %= K


        if ok and (tmp_ans < ans) :
            ans = tmp_ans

        
    print(ans)


    
    
if __name__ == '__main__':
    main()