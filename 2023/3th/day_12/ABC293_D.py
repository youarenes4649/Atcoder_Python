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
    N,M = mi()
    UF = UnionFind(2 * N)
    x,y = 0,0
    for i in range(N):#元から自分達は連結している
        UF.merge(2*i,2*i+1)
    for _ in range(M):
        a,b,c,d =  input().split()
        a = int(a) - 1
        c = int(c) - 1
        if b == 'R' and d == 'R':
            if UF.same(2*a,2*c):
                x += 1
            else:
                UF.merge(2*a,2*c)
        if b == 'R' and d == 'B':
            if UF.same(2*a,2*c+1):
                x += 1
            else:
                UF.merge(2*a,2*c+1)
        if b == 'B' and d == 'B':
            if UF.same(2*a+1,2*c+1):
                x += 1
            else:
                UF.merge(2*a+1,2*c+1)
        if b == 'B' and d == 'R':
            if UF.same(2*a+1,2*c):
                x += 1
            else:
                UF.merge(2*a+1,2*c)
                
    y = len(UF.groups()) - x
    print(x,y)
            
                
if __name__ == '__main__':
    main()