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
    from collections import defaultdict
    N,K,L = map(int,input().split())
    road = UnionFind(N)
    train = UnionFind(N)
    for _ in range(K):
        p,q = map(int,input().split())
        road.merge(p-1,q-1)
    for _ in range(L):
        r,s = map(int,input().split())
        train.merge(r-1,s-1)
        
    #同じ道路,鉄道で連結している者たちは根が等しい
    cnt = defaultdict(int)
    for i in range(N):
        a = road.leader(i)
        b = train.leader(i)
        cnt[(a,b)] += 1
    ans = []
    for i in range(N):
        a = road.leader(i)
        b = train.leader(i)
        ans.append(cnt[a,b])
    print(*ans)
        
    
        
if __name__ == '__main__':
    main()