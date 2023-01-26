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
    N = int(input())
    f = list(map(int,input().split()))
    ans = N
    UF = UnionFind(N)
    from collections import defaultdict
    cnt = defaultdict(int)
    for i in range(N):
        cnt[f[i]] += 1
        if cnt[f[i]] >1:
            ans -=1
    for i,fa in enumerate(f):
        if i > N//2 or i == fa-1:
            break
        if UF.same(i,fa-1):
       
            ans -=1
        UF.merge(i,fa-1)
    print(2**ans-1)
     
if __name__ == '__main__':
    main()