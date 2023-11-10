import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
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

import bisect
def main():
    N,M,Q = mi()
    uf = UnionFind(N)
    
    edges = []
    for i in range(M):
        a,b,c = mi()
        a -= 1
        b -= 1
        edges.append((c,a,b,i))
    for i in range(Q):
        u,v,w = mi()
        u -= 1
        v -= 1
        edges.append((w,u,v,M+i))
    edges.sort()
    ans = [False] * Q
    for edge in edges:
        cost,a,b,d = edge
        if d >= M:
            if uf.same(a,b):
                ans[d - M] = False
                
            else:
                ans[d - M] = True
                
        else:
            if uf.same(a,b):
                continue
            else:
                uf.merge(a,b)
 
    for a in ans:
        if a:
            print('Yes')
        else:
            print('No')
    
                
    
    
        
if __name__ == '__main__':
    main()