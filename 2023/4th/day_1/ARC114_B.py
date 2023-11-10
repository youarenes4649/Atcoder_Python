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

def main():
    N = ii()
    F = li()
    UF = UnionFind(N)
    for i in range(N):
        f = F[i] - 1
        UF.merge(i,f)
    
    ans = pow(2,len(UF.groups()),mod) - 1
    print(ans)
if __name__ == '__main__':
    main()